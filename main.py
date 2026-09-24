import os
import subprocess
from pathlib import Path

def generate_silver_man_video():
    output_filename = "final_video.mp4"
    print("-> Silver Man වීඩියෝව FFmpeg මඟින් සකස් කරමින් පවතී...")
    
    # ටවුන් එක ළඟ රිදී මිනිසා (Silver Man) තේමාවට අදාළව ටෙක්ස්ට් එකක් සහිතව වීඩියෝව සකස් කිරීම
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=1280x720:d=5",
        "-vf", "drawtext=text='Silver Man in Town':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
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
    generate_silver_man_video()
