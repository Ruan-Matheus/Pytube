from change_files_extension import convert_ext as cext
import os
from pytubefix import YouTube, Channel
from pytubefix.exceptions import VideoUnavailable
from pytubefix.cli import on_progress
import re
from subprocess import run


# TODO: Subtitles
def download_youtube(url, path = '.', mp3 = False, hd = True, caption = None, ffmpeg_path="ffmpeg") -> None:
    """Download a single video/music from YouTube with flexible FFmpeg path and unique file naming.

    Args:
        url (string): The URL of the YouTube video
        path (str, optional): The download folder path. Defaults to '.'.
        mp3 (bool, optional): Convert video to mp3. Defaults to False.
        hd (bool, optional): Download the highest resolution available. Defaults to True.
        caption (str, optional): Language code for captions. Defaults to None.
        ffmpeg_path (str, optional): Path to ffmpeg executable, defaults to "ffmpeg" in system path.
    """

    old_path = os.getcwd()
    os.chdir(path)
   
    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        # TODO: There is an error here. If there's no substituiton re.sub throws an error!
        # Windows doesnt allow files with certain characters
        pattern = re.compile(r"[\\/:*?\"<>|\.,#]")
        video_title = yt.title
        video_title = re.sub(pattern, "", video_title)
        
        # Downloading the caption
        if caption:
                try:
                    caption = yt.captions[caption]
                    caption.xml_captions
                    caption = caption.generate_srt_captions()

                    with open(video_title + '.srt', 'w', encoding= 'UTF8') as f:
                        f.write(caption)
                except KeyError:
                    print("Caption not available for the mentioned code!")
        

        print(f"\nVideo name: {yt.title}\n".center(35))

        if mp3:
            yt.streams.get_audio_only().download()
            cext(".mp4", ".mp3")

        elif hd:
            # Video and audio comes separately, if needed a higher resolution
            video_stream = yt.streams.get_highest_resolution(progressive=False)
            audio_stream = yt.streams.get_audio_only()

            video_stream.download(filename='video.mp4')
            audio_stream.download(filename='audio.mp4')

            # Using ffmpeg to merge the video and audio files
            ffmpeg_command = f'{ffmpeg_path} -i "video.mp4" -i "audio.mp4" -c copy "{video_title}.mp4"'
            run(ffmpeg_command, shell= True)

            os.remove('video.mp4')
            os.remove('audio.mp4')

        else:
            yt.streams.get_highest_resolution().download()
    
    # Catching errs of download to show to the user
    # TODO: Refine the errors catching, age restriction, video unavailable, etc
    except VideoUnavailable:
        print(f"Video {url} is unavailable.")
    except Exception as err:
        print(f"An error occurred: {err}")
    finally:
        print("\nProcesso finalizado")
        os.chdir(old_path)