from pytube import Playlist
from youtube import downlaod_youtube

# TODO: Number of videos in a playlist, playlist name

def download_playlist(url, path = '.', mp3 = False, hd = True, caption = None):
    playlist_object = Playlist(url)
    playlist_object_name = playlist_object.title
    

    for video_url in playlist_object.url_generator():
        downlaod_youtube(video_url, path, mp3, hd, caption)





def main():
    url = "https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg"
    path = r'C:\Users\Ruan\Videos\Python'
    caption = 'en-IN'
    download_playlist(url, path, caption= caption)


if __name__ == '__main__':
    main()