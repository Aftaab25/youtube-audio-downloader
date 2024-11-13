import yt_dlp as youtube_dl

global path
def get_mp3():
  video_info = youtube_dl.YoutubeDL().extract_info (
    url = input("Enter video URL: "), download = False
  )


  path = ""
  path_ = input("Select Destination: ")
  if path_=="":
    path = "~/Music"
  else:
    path = path_
          
  print("Selected Path: ", path)
  print(video_info['title'])
  file_rename = input(f"Rename File? {video_info['title']}: ")
  if (file_rename != ""):
    path = path + "/" + file_rename + ".mp3"
  else: path = path + f"/{video_info['title']}.mp3"
  options = {'format': 'bestaudio/best', 'keepvideo': False, 'outtmpl': path}
  print("Final audio file path: ", path)
  with youtube_dl.YoutubeDL(options) as ydl:
      ydl.download([video_info['webpage_url']])

get_mp3()
