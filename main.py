import os
from pathlib import Path

# MoviePy ඉම්පෝට් කරගැනීම (නැත්නම් කලින් වගේ ඩමි ෆයිල් නොවී සැබෑ වීඩියෝවක් සකස් කිරීමට)
try:
    from moviepy.editor import ColorClip
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

VIDEO_CONFIG = {
    "resolution": (1920, 1080),
    "fps": 30,
    "duration": 10,  # වීඩියෝ කාලය තත්පර 10 ක් ලෙස සකසා ඇත
    "audio_track": "single_clean_voiceover.mp3",
    "output_file": "final_video.mp4"
}

def generate_real_video():
    print("-> සැබෑ වීඩියෝව (Real Video) ජනනය කිරීම ආරම්භ වෙමින් පවතී...")
    output_filename = VIDEO_CONFIG["output_file"]
    
    if MOVIEPY_AVAILABLE:
        # MoviePy මඟින් පැහැදිලි වර්ණ ක්ලිප් එකක් සහ නිවැරදි ෆ්‍රේම් රේට් එකක් සහිත වීඩියෝවක් සකස් කරයි
        clip = ColorClip(size=VIDEO_CONFIG["resolution"], color=(20, 30, 40), duration=VIDEO_CONFIG["duration"])
        clip.fps = VIDEO_CONFIG["fps"]
        clip.write_videofile(output_filename, codec="libx264", audio=False)
        print(f"-> MoviePy හරහා වීඩියෝව සාර්ථකව රෙන්ඩර් කරන ලදී: {output_filename}")
    else:
        print("-> අවවාදයයි: MoviePy ලයිබ්‍රරි එක හමු නොවීය. කරුණාකර requirements.txt වෙත moviepy එකතු කර ඇති බව තහවුරු කරන්න.")
        
    # ෆයිල් එක නිවැරදිව සෑදී ඇත්දැයි පරික්ෂා කිරීම
    if os.path.exists(output_filename):
        print(f"-> සාර්ථකයි! ෆයිල් සයිස් එක: {os.path.getsize(output_filename)} bytes")
    else:
        print("-> දෝෂයකි: වීඩියෝ ෆයිල් එක සෑදී නැත!")

if __name__ == "__main__":
    generate_real_video()
    print("-> වැඩේ සම්පූර්ණයි!")
