import os
import subprocess
from pathlib import Path

def generate_video():
    output_filename = "final_video.mp4"
    print("-> FFmpeg මඟින් සැබෑ වීඩියෝව සකස් කරමින් පවතී...")
    
    # FFmpeg හරහා පර්ෆෙක්ට් MP4 වීඩියෝවක් රෙන්ඩර් කිරීම
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "testsrc=size=1280x720:rate=30",
        "-t", "5",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_filename
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("FFmpeg Output:", result.stdout)
    print("FFmpeg Error:", result.stderr)
    
    if os.path.exists(output_filename):
        print(f"-> සාර්ථකයි! ෆයිල් සයිස් එක: {os.path.getsize(output_filename)} bytes")
    else:
        print("-> දෝෂයකි: වීඩියෝව සෑදී නැත!")

if __name__ == "__main__":
    generate_video()
