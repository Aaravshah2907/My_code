import yt_dlp
import os
import sys
import subprocess
import json

def sanitize_filename(name):
    if not name: return "Unknown"
    invalid_chars = ['\\', '|', '*', '?', '"', '<', '>', ':', '/']
    for char in invalid_chars:
        name = name.replace(char, '.')
    return name.strip()

def expand_path(path):
    return os.path.expanduser(path)

def load_archive(archive_path):
    if os.path.exists(archive_path):
        try:
            with open(archive_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_archive(archive_path, data):
    with open(archive_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def convert_remaining_files(directory, target_ext):
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
            except: pass

def download_youtube(url, media_type):
    path_video = expand_path('~/Documents/Personal/Yt-Videos/')
    path_audio = expand_path('~/Documents/Personal/Yt-Music/')
    os.makedirs(path_video, exist_ok=True)
    os.makedirs(path_audio, exist_ok=True)

    archive_json = os.path.join(path_audio, 'download_history.json')
    history = load_archive(archive_json)

    def cleanup_hook(d):
        if d['status'] == 'finished':
            # Update JSON history once finished
            info = d.get('info_dict', {})
            video_id = info.get('id')
            if video_id and video_id not in history:
                history[video_id] = {
                    "title": info.get('title'),
                    "file": info.get('_filename') or info.get('filepath'),
                    "date_downloaded": info.get('upload_date')
                }
                save_archive(archive_json, history)

            if d.get('postprocessor') == 'FFmpegMetadata':
                filename = info.get('filepath') or info.get('_filename')
                if filename:
                    base = os.path.splitext(filename)[0]
                    for ext in ['.info.json', '.jpg', '.webp', '.png', '.jpeg', '.description']:
                        f_path = base + ext
                        if os.path.exists(f_path):
                            try: os.remove(f_path)
                            except: pass

    blur_filter = 'split[v1][v2];[v1]scale=1000:1000:force_original_aspect_ratio=increase,crop=1000:1000,boxblur=20:10[bg];[v2]scale=1000:-1[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2'

    ydl_opts = {
        'ignoreerrors': True,
        'writethumbnail': True,
        'overwrites': False,
        # We still use the internal archive for speed, but our JSON will store the readable details
        'download_archive': os.path.join(path_audio, 'archive.txt'), 
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': 'https://www.google.com/',
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
        'postprocessor_hooks': [cleanup_hook],
        'nocheckcertificate': True,
        'postprocessors': [
            {'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg', 'when': 'before_dl'},
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata', 'add_metadata': True}
        ],
        'postprocessor_args': {
            'thumbnailsconvertor': ['-vf', blur_filter],
        },
    }

    if media_type in ["1", "3"]:
        ydl_opts.update({
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(path_video, '%(playlist_title)s/%(title)s.%(ext)s' if media_type == "3" else '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': media_type == "1",
        })
    elif media_type in ["2", "4"]:
        ydl_opts.update({
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(path_audio, '%(playlist_title)s/%(title)s.%(ext)s' if media_type == "4" else '%(title)s.%(ext)s'),
            'noplaylist': media_type == "2",
        })
        ydl_opts['postprocessors'].insert(0, {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        target_ext = "mp3" if media_type in ["2", "4"] else "mp4"
        root_dir = path_audio if media_type in ["2", "4"] else path_video
        convert_remaining_files(root_dir, target_ext)
        print('\n[*] Download sequence completed.')
    except Exception as e:
        print(f"\n[!] Error: {e}")

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else None
    media_type = sys.argv[2] if len(sys.argv) > 2 else None
    if not url: url = input("Enter URL:\n>> ").strip()
    if not media_type:
        print("\n1: Video | 2: Audio | 3: Playlist Video | 4: Playlist Audio")
        media_type = input(">> ").strip()
    download_youtube(url, media_type)

if __name__ == "__main__":
    main()
