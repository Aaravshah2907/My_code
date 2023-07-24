from pytube import YouTube
import os

yt = YouTube(
    url=str(input("Enter the URL of the video you want to download: \n>> ").strip()))

print("Select download format:")
print("1: Video file with audio (.mp4)")
print("2: Audio only (.mp3)")
media_type = input()
path1 = r'E:\Others\Youtube_Downloaded_Videos'
path2 = r'E:\Others\Songs_Downloaded'
path_exist1 = os.path.exists(path1)
path_exist2 = os.path.exists(path2)


if media_type == '1':
    if path_exist1:
        pass
    else:
        os.mkdir(path1)

elif media_type == '2':
    if path_exist2:
        pass
    else:
        os.mkdir(path2)
else:
    pass

if media_type == "1":
    video = yt.streams.get_highest_resolution()
    name = yt.title.replace("/", ".")
    name = name.replace("\\", ".").replace("|", ".").replace("*", ".").replace(
        "?", ".").replace('"', ".").replace('<', ".").replace('>', ".").replace(':', ".")

    video.download(output_path=path1, filename=name+'.mp4')

elif media_type == "2":
    video = yt.streams.filter(only_audio=True).first()
    name = yt.title.replace("/", ".")
    name = name.replace("\\", ".")
    name = name.replace("|", ".")
    name = name.replace("*", ".")
    name = name.replace("?", ".")
    name = name.replace('"', ".")
    name = name.replace('<', ".")
    name = name.replace('>', ".")
    name = name.replace(':', ".")

    video.download(output_path=path2, filename=name+"."+yt.author+".mp3")

else:
    print("Invalid selection.")


print(f'{yt.title} has been downloaded.')
