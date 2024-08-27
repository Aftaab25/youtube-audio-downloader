# print("Hello World")

import yt_dlp as youtube_dl

global path
def get_mp3():
  video_info = youtube_dl.YoutubeDL().extract_info (
    url = input("Enter video URL: "), download = False
  )


  path = ""
  path_ = input("Select Destination")
  if path_=="":
    path = "~/Music"
  else:
    path = path_
          
  options = {'format': 'bestaudio/best', 'keepvideo': False, 'outtmpl': path + f"/{video_info['title']}.mp3"}
  print(path)
  path = path + f"/{video_info['title']}.mp3"
  print(path)
  with youtube_dl.YoutubeDL(options) as ydl:
      ydl.download([video_info['webpage_url']])

get_mp3()
