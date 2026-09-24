import os
import subprocess
from pathlib import Path

VIDEO_CONFIG = {
    "output_file": "final_video.mp4"
}

def generate_real_ffmpeg_video():
    print("-> FFmpeg භාවිතයෙන් සැබෑ වීඩියෝවක් ජනනය කරමින් පවතී...")
    output_filename = VIDEO_CONFIG["output_file"]
    
    # FFmpeg හරහා තත්පර 5ක නිවැරදි playable MP4 වීඩියෝවක් සකස් කිරීම
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=1280x720:d=5",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_filename
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    
    if os.path.exists(output_filename):
        print(f"-> සාර්ථකයි: වීඩියෝව සෑදී ඇත -> {os.path.abspath(output_filename)} (ප්‍රමාණය: {os.path.getsize(output_filename)} bytes)")
    else:
        print("-> දෝෂයකි: වීඩියෝව සෑදී නැත!")

if __name__ == "__main__":
    generate_real_ffmpeg_video()
    print("-> වැඩේ සාර්ථකව අවසන්!")
