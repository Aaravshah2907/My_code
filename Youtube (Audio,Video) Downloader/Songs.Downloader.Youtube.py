import yt_dlp
import os
import sys

def sanitize_filename(name):
    invalid_chars = ['\\', '|', '*', '?', '"', '<', '>', ':', '/']
    for char in invalid_chars:
        name = name.replace(char, '.')
    return name.strip()

def expand_path(path):
    return os.path.expanduser(path)

def download_youtube(url, media_type):
    path_video = expand_path('~/Documents/Personal/Yt-Videos/')
    path_audio = expand_path('~/Documents/Personal/AudioBooks/')
    os.makedirs(path_video, exist_ok=True)
    os.makedirs(path_audio, exist_ok=True)

    ydl_opts = {}
    if media_type == "1":  # Video with audio, best mp4 720p or highest available
        ydl_opts = {
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(path_video, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
        }
    elif media_type == "2":  # Audio only mp3 best quality
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path_audio, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        print("Invalid media type selection.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f'Download complete: {sanitize_filename(info["title"])}')

def main():
    if len(sys.argv) > 3:
        print("Usage: python Youtube.py [<YouTube URL> <media type>]")
        print("Media type: 1 for video with audio (.mp4), 2 for audio only (.mp3)")
        return
    
    if sys.argv[1] in ['-h', '--help']:
        print("Usage: python Youtube.py [<YouTube URL> <media type>]")
        print("Media type: 1 for video with audio (.mp4), 2 for audio only (.mp3)")
        return
    
    url_sysarg = sys.argv[1] if len(sys.argv) > 1 else None
    if url_sysarg:
        url = url_sysarg
        media_type = sys.argv[2] if len(sys.argv) > 2 else "1"
    else:
        url = input("Enter the YouTube video URL:\n>> ").strip()
        print("Select download format:")
        print("1: Video file with audio (.mp4)")
        print("2: Audio only (.mp3)")
        media_type = input(">> ").strip()
    download_youtube(url, media_type)

if __name__ == "__main__":
    main()
