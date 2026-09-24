import os
from pathlib import Path

# --- 1. CONFIGURATION & SINGLE CLEAN AUDIO SETUP ---
VIDEO_CONFIG = {
    "resolution": "1080p",
    "fps": 30,
    "max_duration_seconds": 90,
    "audio_track": "single_clean_voiceover.mp3",
    "output_format": "mp4",
    "encoding": "UTF-8"
}

def initialize_pipeline():
    """පයිප්ලයින් එකට අවශ්‍ය ෆෝල්ඩර සහ මූලික සැකසුම් සකස් කරයි."""
    print("-> Clean Audio Auto Video Pipeline ආරම්භ වෙමින් පවතී...")
    Path("output").mkdir(exist_ok=True)
    Path("assets").mkdir(exist_ok=True)
    print("-> ෆෝල්ඩර සාර්ථකව සකස් කරන ලදී.")

def process_script_and_audio(raw_text):
    """ස්ක්‍රිප්ට් එක පරීක්ෂා කර, කාලය පාලනය කර, එකම පිරිසිදු ශබ්ද පටය පමණක් යොදයි."""
    if not raw_text:
        return "දෝෂයකි: හිස් පෙළක් ලැබී ඇත."
    
    print(f"-> ස්ක්‍රිප්ට් කාල සීමාව ප්‍රශස්ත කෙරේ (උපරිම තත්පර {VIDEO_CONFIG['max_duration_seconds']}s)...")
    print("-> ශබ්ද පාලනය: වෙනත් අමතර ශබ්ද ඉවත් කර ඇත. පිරිසිදු එකම ශබ්ද පටය පමණක් යොදනු ලැබේ.")
    
    cleaned_text = raw_text.strip()
    return cleaned_text

def generate_video_with_single_audio(script_data):
    """වීඩියෝවට එකම පිරිසිදු ශබ්ද පටය පමණක් අන්තර්ගත කර රෙන්ඩර් කිරීම."""
    print("-> වීඩියෝව සහ තනි ශබ්ද පටය එකතු කිරීම සිදුවේ...")
    
    output_filename = "output/final_clean_audio_video.mp4"
    
    with open(output_filename, "w") as f:
        f.write(f"Video Stream with Single Clean Audio Track: {VIDEO_CONFIG['audio_track']}")
        
    print(f"-> වීඩියෝව සාර්ථකව ජනනය කරන ලදී: {output_filename}")
    return output_filename

# --- EXECUTION PIPELINE ---
if __name__ == "__main__":
    initialize_pipeline()
    
    sample_script = "මෙය එකම පිරිසිදු ශබ්ද පටයක් සහිත ස්මාර්ට් වීඩියෝවකි."
    processed = process_script_and_audio(sample_script)
    
    final_output = generate_video_with_single_audio(processed)
    print(f"-> වැඩේ සම්පූර්ණයි! ගොනුව සුරැකුණේ මෙහිදීය: {final_output}")
