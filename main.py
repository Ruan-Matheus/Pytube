from youtube import download_youtube
  
def main():
    path = r'' # Your path of download
    ffmpeg_path = r'' # Path to your ffmpeg
    url = r'' # Path to your video/music to download  

    download_youtube(url, path, ffmpeg_path=ffmpeg_path)


if __name__ == '__main__':
    main()
