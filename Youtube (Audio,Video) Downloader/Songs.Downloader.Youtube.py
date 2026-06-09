import yt_dlp
import os
import sys
import subprocess
import json
import argparse
import shlex

def sanitize_filename(name):
    if not name: return "Unknown"
    invalid_chars = ['\\', '|', '*', '?', '"', '<', '>', ':', '/']
    for char in invalid_chars:
        name = name.replace(char, '.')
    return name.strip()

def expand_path(path):
    return os.path.expanduser(path)

def fetch_android_po_token():
    """Fetch a GVS PO token for the Android client using yt-dlp.
    Returns the token string or None on failure.
    """
    dummy_id = "dQw4w9WgXcQ"  # public video ID used only to get the token
    cmd = (
        f'yt-dlp --quiet --print "po_token" '
        f'--extractor-args "youtube:player_client=android" '
        f'"https://www.youtube.com/watch?v={dummy_id}"'
    )
    try:
        result = subprocess.run(shlex.split(cmd), capture_output=True, text=True, check=True)
        token = result.stdout.strip()
        return token if token else None
    except Exception as e:
        print(f"[!] Could not obtain PO token: {e}")
        return None

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

def download_youtube(url, media_type, options=None):
    """Download YouTube content.
    `options` may include {'quality': '1080p' or '720p'} to override format.
    """
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
        # Enable subtitle download for video
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'postprocessors': [
            {'key': 'FFmpegThumbnailsConvertor', 'format': 'jpg', 'when': 'before_dl'},
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata', 'add_metadata': True},
            {'key': 'FFmpegSubtitlesConvertor', 'format': 'srt'}
        ],
        'postprocessor_args': {
            'thumbnailsconvertor': ['-vf', blur_filter],
        },
    }

    # Determine format based on media_type and optional quality flag
    if media_type in ["1", "3"]:
        # Video download
        base_format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        if options and options.get('quality'):
            # Map explicit quality to format string
            qual = options['quality']
            if qual == '1080p':
                fmt = 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            elif qual == '720p':
                fmt = 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            else:
                fmt = qual  # Assume user provided a valid yt-dlp format string
        else:
            # Fallback logic: try 1080p then 720p via yt-dlp's format selection later
            fmt = 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best/bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        ydl_opts.update({
            'format': fmt,
            'outtmpl': os.path.join(path_video, '%(playlist_title)s/%(title)s.%(ext)s' if media_type == "3" else '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'noplaylist': media_type == "1",
        })
    elif media_type in ["2", "4"]:
        # Audio download
        base_audio = 'bestaudio/best'
        if options and options.get('quality'):
            # Quality flag for audio can be ignored or mapped; we keep default
            fmt = base_audio
        else:
            fmt = base_audio
        ydl_opts.update({
            'format': fmt,
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

def parse_args():
    parser = argparse.ArgumentParser(description="YouTube audio/video downloader with flag based CLI.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--audio', action='store_true', help='Download audio only')
    group.add_argument('-v', '--video', action='store_true', help='Download video only')
    parser.add_argument('-p', '--playlist', action='store_true', help='Treat URL as a playlist')
    parser.add_argument('-q', '--quality', choices=['1080p', '720p', 'best'], help='Preferred quality (default tries 1080p then 720p)')
    parser.add_argument('--po-token', help='PO Token for authentication/bypass')
    # Delete subflags
    parser.add_argument('-d', '--delete', action='store_true', help='Delete a previously downloaded entry')
    parser.add_argument('--id', dest='del_id', help='Video ID to delete')
    parser.add_argument('--url', dest='del_url', help='Video URL to delete')
    parser.add_argument('--path', dest='del_path', help='Exact file path to delete')
    parser.add_argument('url', nargs='?', help='YouTube video or playlist URL')
    args = parser.parse_args()
    return args

def delete_entry(args):
    # Resolve identifier to video ID and file path
    archive_json = os.path.join(expand_path('~/Documents/Personal/Yt-Music/'), 'download_history.json')
    archive_txt = os.path.join(expand_path('~/Documents/Personal/Yt-Music/'), 'archive.txt')
    history = load_archive(archive_json)
    video_id = None
    file_path = None
    if args.del_id:
        video_id = args.del_id
    elif args.del_url:
        try:
            info = yt_dlp.YoutubeDL().extract_info(args.del_url, download=False)
            video_id = info.get('id')
        except Exception:
            print('Failed to extract video ID from URL.')
            return
    elif args.del_path:
        # Find entry matching the path
        for vid, entry in history.items():
            if entry.get('file') == args.del_path:
                video_id = vid
                file_path = args.del_path
                break
    if not video_id:
        print('No matching video ID found for deletion.')
        return
    # Determine file path from history if not already known
    if not file_path:
        entry = history.get(video_id)
        if entry:
            file_path = entry.get('file')
    # Delete the file(s)
    if file_path and os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f'Deleted file: {file_path}')
        except Exception as e:
            print(f'Error deleting file: {e}')
    # Remove from JSON archive
    if video_id in history:
        del history[video_id]
        save_archive(archive_json, history)
        print(f'Removed entry {video_id} from download_history.json')
    # Update archive.txt
    if os.path.exists(archive_txt):
        try:
            with open(archive_txt, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            with open(archive_txt, 'w', encoding='utf-8') as f:
                for line in lines:
                    if line.strip() != video_id:
                        f.write(line)
            print('Updated archive.txt')
        except Exception as e:
            print(f'Error updating archive.txt: {e}')

def main():
    args = parse_args()
    # Fetch PO token once per session (if we are going to download)
    po_token = None
    if not args.delete:
        po_token = fetch_android_po_token()
        if po_token:
            print("[*] PO token obtained for Android client.")
    if args.delete:
        delete_entry(args)
        return
    # Determine media_type code based on flags
    if args.audio and not args.playlist:
        media_type = "2"
    elif args.audio and args.playlist:
        media_type = "4"
    elif args.video and not args.playlist:
        media_type = "1"
    elif args.video and args.playlist:
        media_type = "3"
    else:
        # Fallback to interactive mode if no flags provided
        url = args.url or input("Enter URL:\n>> ").strip()
        media_type = input("\n1: Video | 2: Audio | 3: Playlist Video | 4: Playlist Audio\n>> ").strip()
        options = {}
        if args.quality:
            options["quality"] = args.quality
        if po_token:
            options["po_token"] = po_token
        download_youtube(url, media_type, options if options else None)
        return
    # URL must be supplied either as positional arg or prompted
    url = args.url or input("Enter URL:\n>> ").strip()
    options = {}
    if args.quality:
        options["quality"] = args.quality
    if po_token:
        options["po_token"] = po_token
    download_youtube(url, media_type, options if options else None)

if __name__ == "__main__":
    main()
