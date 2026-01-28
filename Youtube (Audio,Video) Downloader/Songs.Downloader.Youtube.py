import yt_dlp
import os
import sys
import subprocess

def sanitize_filename(name):
    if not name: return "Unknown"
    invalid_chars = ['\\', '|', '*', '?', '"', '<', '>', ':', '/']
    for char in invalid_chars:
        name = name.replace(char, '.')
    return name.strip()

def expand_path(path):
    return os.path.expanduser(path)

def convert_remaining_files(directory, target_ext):
    """Fallback to convert any stray webp/webm to target format or delete if image."""
    if not os.path.exists(directory): return
    codec_map = {
        'mp3': ['-vn', '-ab', '320k', '-ar', '44100', '-f', 'mp3'],
        'mp4': ['-c:v', 'libx264', '-preset', 'fast', '-crf', '22', '-c:a', 'aac', '-b:a', '192k']
    }
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        ext = ext.lower()
        if ext in ['.webp', '.webm', '.mkv', '.m4a']:
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, f"{name}.{target_ext}")
            if os.path.exists(output_path):
                try: os.remove(input_path)
                except: pass
                continue
            ffmpeg_cmd = ['ffmpeg', '-i', input_path] + codec_map.get(target_ext, []) + [output_path, '-y']
            try:
                res = subprocess.run(ffmpeg_cmd, capture_output=True, text=True)
                if res.returncode == 0: os.remove(input_path)
                elif ext in ['.webp', '.jpg']: os.remove(input_path)
            except: pass

def download_youtube(url, media_type):
    path_video = expand_path('~/Documents/Personal/Yt-Videos/')
    path_audio = expand_path('~/Documents/Personal/Yt-Music/')
    os.makedirs(path_video, exist_ok=True)
    os.makedirs(path_audio, exist_ok=True)

    # Hook to clean up files after post-processing
    def cleanup_hook(d):
        if d['status'] == 'finished' and d['postprocessor'] == 'FFmpegMetadata':
            info = d.get('info_dict', {})
            filename = info.get('filepath') or info.get('_filename')
            if filename:
                base = os.path.splitext(filename)[0]
                for ext in ['.info.json', '.jpg', '.webp', '.png', '.jpeg', '.description']:
                    f_path = base + ext
                    if os.path.exists(f_path):
                        try: os.remove(f_path)
                        except: pass

    # Base options for all downloads to bypass 403 Forbidden
    ydl_opts = {
        'writethumbnail': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': 'https://www.google.com/',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
        'postprocessor_hooks': [cleanup_hook],
        'nocheckcertificate': True,
    }

    if media_type == "1":  # Single Video
        ydl_opts.update({
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(path_video, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': True,
            'postprocessors': [{'key': 'EmbedThumbnail'}, {'key': 'FFmpegMetadata', 'add_metadata': True}],
        })
    elif media_type == "2":  # Single Audio
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path_audio, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegMetadata', 'add_metadata': True},
            ],
        })
    elif media_type == "3":  # Playlist Video
        ydl_opts.update({
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(path_video, '%(playlist_title)s/%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': False,
            'postprocessors': [{'key': 'EmbedThumbnail'}, {'key': 'FFmpegMetadata', 'add_metadata': True}],
        })
    elif media_type == "4":  # Playlist Audio
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path_audio, '%(playlist_title)s/%(title)s.%(ext)s'),
            'noplaylist': False,
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'},
                {'key': 'EmbedThumbnail'},
                {'key': 'FFmpegMetadata', 'add_metadata': True},
            ],
        })
    else:
        print("Invalid selection.")
        return

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Post-download sweep to convert strays or clean up
        target_ext = "mp3" if media_type in ["2", "4"] else "mp4"
        root_dir = path_audio if media_type in ["2", "4"] else path_video
        convert_remaining_files(root_dir, target_ext)
        if media_type in ["3", "4"]: # If playlist, check subdirs
            for item in os.listdir(root_dir):
                item_path = os.path.join(root_dir, item)
                if os.path.isdir(item_path):
                    convert_remaining_files(item_path, target_ext)

        print('\n[*] Download sequence completed.')
    except Exception as e:
        print(f"\n[!] Error: {e}")
        print("Tip: If 403 persists, try updating: pip install -U yt-dlp")

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() in ['-h', '--help', 'help']:
        print("Usage: python Songs.Downloader.Youtube.py [URL] [TYPE]")
        print("Types: 1 (Video), 2 (Audio), 3 (Playlist Video), 4 (Playlist Audio)")
        return
    
    url = sys.argv[1] if len(sys.argv) > 1 else None
    media_type = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not url:
        url = input("Enter the YouTube URL:\n>> ").strip()
        if not url: return
    
    if not media_type:
        print("\nSelect format:")
        print("1: Single Video (.mp4)")
        print("2: Single Audio (.mp3)")
        print("3: Playlist Video (.mp4)")
        print("4: Playlist Audio (.mp3)")
        media_type = input(">> ").strip()
    
    download_youtube(url, media_type)

if __name__ == "__main__":
    main()
