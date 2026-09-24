import os
import subprocess
from pathlib import Path

def generate_silver_man_video():
    output_filename = "final_video.mp4"
    print("-> වැඩි දියුණු කළ Silver Man වීඩියෝව සකස් කරමින් පවතී...")
    
    # ඩියුරේෂන් එක තත්පර 15 දක්වා වැඩි කර, HD කොලිටියෙන් සහ Silver Man කතාවට ගැළපෙන ටෙක්ස්ට් එකක් සහිතව සකස් කිරීම
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", "color=c=black:s=1280x720:r=30:d=15",
        "-vf", "drawtext=text='Silver Man Amazes People in Town':fontcolor=silver:fontsize=44:x=(w-text_w)/2:y=(h-text_h)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_filename
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("FFmpeg Output:", result.stdout)
    print("FFmpeg Error:", result.stderr)
    
    if os.path.exists(output_filename):
        print(f"-> සාර්ථකයි! අලුත් ෆයිල් සයිස් එක: {os.path.getsize(output_filename)} bytes")
    else:
        print("-> දෝෂයකි: වීඩියෝව සෑදී නැත!")

if __name__ == "__main__":
    generate_silver_man_video()
