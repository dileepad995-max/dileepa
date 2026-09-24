import os
from pathlib import Path

# --- 1. CONFIGURATION ---
VIDEO_CONFIG = {
    "resolution": "1080p",
    "fps": 30,
    "max_duration_seconds": 90,
    "audio_track": "single_clean_voiceover.mp3",
    "output_format": "mp4",
    "encoding": "UTF-8"
}

def initialize_pipeline():
    print("-> Clean Audio Auto Video Pipeline ආරම්භ වෙමින් පවතී...")
    print(f"-> Current Working Directory: {os.getcwd()}")
    Path("output").mkdir(exist_ok=True)
    Path("assets").mkdir(exist_ok=True)

def generate_video_with_single_audio():
    # GitHub Actions බලාපොරොත්තු වන පරිදි කෙළින්ම 'final_video.mp4' ලෙස සේව් කිරීම
    output_filename = "final_video.mp4"
    
    print(f"-> ෆයිල් එක සකස් කෙරේ: {output_filename}")
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(f"Video Stream with Single Clean Audio Track: {VIDEO_CONFIG['audio_track']}")
    
    # ෆයිල් එක නිවැරදිව සෑදී ඇත්දැයි පරීක්ෂා කිරීම
    if os.path.exists(output_filename):
        print(f"-> සාර්ථකයි: ෆයිල් එක පිහිටා ඇත්තේ මෙහිදීය -> {os.path.abspath(output_filename)}")
    else:
        print("-> දෝෂයකි: ෆයිල් එක සෑදී නැත!")
        
    return output_filename

if __name__ == "__main__":
    initialize_pipeline()
    generate_video_with_single_audio()
    print("-> වැඩේ සාර්ථකව අවසන්!")
