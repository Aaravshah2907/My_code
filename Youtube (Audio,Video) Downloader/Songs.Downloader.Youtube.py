from pytube import YouTube
import os

yt = YouTube(url=str(
    input("Enter the URL of the video you want to download: \n>> ").strip()))

print("Select download format:")
print("1: Video file with audio (.mp4)")
print("2: Audio only (.mp3)")
media_type = input()
path1 = r'~/Documents/Personal/Yt-Videos/'
path2 = r'~/Documents/Personal/AudioBooks/'
path_exist1 = os.path.exists(path1)
path_exist2 = os.path.exists(path2)

if media_type == "1":
    video = yt.streams.get_by_resolution('720p')
    name = yt.title()
    # name = name.replace("\\", ".").replace("|", ".").replace("*", ".").replace( "?", ".").replace('"', ".").replace('<', ".").replace('>', ".").replace(':', ".")

    video.download(output_path=path1, filename=name+'.mp4')
    size = video.filesize/1048576
    print(f'{yt.title} downloaded in {video.resolution}, space consumed is {size} mb')

elif media_type == "2":
    video = yt.streams.filter(only_audio=True).first()
    size = video.filesize_approx/1048576
    name = yt.title()
    #name = name.replace("\\", ".").replace("|", ".").replace("*", ".").replace("?", ".").replace('"', ".").replace('<', ".").replace('>', ".").replace(':', ".")

    video.download(output_path=path2, filename=name+"."+yt.author+".mp3")
    print(f'{yt.title} by {yt.author} downloaded in {size} mb')

else:
    print("Invalid selection.")
