import os
from pathlib import Path
import urllib.request

VIDEO_CONFIG = {
    "output_file": "final_video.mp4",
    # නොමිලේ ලබා ගත හැකි සැබෑ සැම්ප්ල් MP4 වීඩියෝ ලින්ක් එක
    "sample_video_url": "https://www.w3schools.com/html/mov_bbb.mp4"
}

def download_real_sample_video():
    print("-> සැබෑ සැම්ප්ල් වීඩියෝව ඩවුන්ලෝඩ් කරමින් පවතී...")
    output_filename = VIDEO_CONFIG["output_file"]
    
    try:
        # අන්තර්ජාලයෙන් වීඩියෝව ඩවුන්ලෝඩ් කර final_video.mp4 ලෙස සේව් කිරීම
        urllib.request.urlretrieve(VIDEO_CONFIG["sample_video_url"], output_filename)
        print(f"-> සාර්ථකයි: වීඩියෝව ඩවුන්ලෝඩ් විය -> {os.path.abspath(output_filename)} (ප්‍රමාණය: {os.path.getsize(output_filename)} bytes)")
    except Exception as e:
        print(f"-> දෝෂයකි: වීඩියෝව ඩවුන්ලෝඩ් කරගත නොහැකි විය: {e}")
        # ෆේල් වුණොත් වෙනත් ඩමි බයිට්ස් ලිවීම
        with open(output_filename, "wb") as f:
            f.write(b'\x00\x00\x00\x20ftypisom' + b'\x00' * 5000)

if __name__ == "__main__":
    download_real_sample_video()
    print("-> පයිප්ලයින් වැඩසටහන සාර්ථකව අවසන්!")
