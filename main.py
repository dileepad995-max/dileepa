import os
import time
import requests
from google import genai
from google.genai.errors import ServerError
from gtts import gTTS
from moviepy import VideoFileClip, AudioFileClip

def generate_script():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    prompt = (
        "Write a 40-second viral TikTok script about a street living silver statue "
        "who suddenly moves and shocks tourists. Hook the viewer in the first 3 seconds. "
        "Keep it engaging, emotional, and high-retention."
    )
    
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
            )
            return response.text.strip()
        except ServerError as e:
            if "503" in str(e) and attempt < 2:
                print(f"Server busy (503), retrying in {(attempt + 1) * 5} seconds...")
                time.sleep((attempt + 1) * 5)
            else:
                raise e

def download_pexels_video():
    api_key = os.environ.get("PEXELS_API_KEY")
    headers = {"Authorization": api_key} if api_key else {}
    
    queries = ["living statue", "street performer", "silver statue", "statue", "performance"]
    
    for query in queries:
        try:
            url = f"https://api.pexels.com/videos/search?query={query.replace(' ', '+')}&per_page=1"
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "videos" in data and len(data["videos"]) > 0:
                    video_files = data["videos"][0]["video_files"]
                    if len(video_files) > 0:
                        video_url = video_files[0]["link"]
                        print(f"Downloading video from Pexels using query: '{query}'...")
                        video_data = requests.get(video_url, timeout=15).content
                        video_path = "temp_video.mp4"
                        with open(video_path, "wb") as f:
                            f.write(video_data)
                        return video_path
        except Exception as e:
            print(f"Query '{query}' failed: {e}")
            continue
            
    print("Pexels API failed or returned no videos. Using fallback public sample video...")
    try:
        fallback_url = "https://assets.mixkit.co/videos/preview/mixkit-hands-of-a-man-working-on-a-clay-sculpture-43098-large.mp4"
        video_data = requests.get(fallback_url, timeout=15).content
        video_path = "temp_video.mp4"
        with open(video_path, "wb") as f:
            f.write(video_data)
        return video_path
    except Exception as e:
        raise Exception(f"Failed to download fallback video: {e}")

def main():
    print("Generating viral script...")
    script_text = generate_script()
    print(f"Script generated successfully:\n{script_text}")

    print("Generating voiceover audio...")
    tts = gTTS(text=script_text, lang='en', tld='com')
    audio_path = "audio.mp3"
    tts.save(audio_path)
    print("Audio generated successfully.")

    print("Fetching video clip...")
    video_path = download_pexels_video()

    print("Combining video and audio into final_video.mp4...")
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    if video_clip.duration > audio_clip.duration:
        video_clip = video_clip.subclipped(0, audio_clip.duration)

    final_clip = video_clip.with_audio(audio_clip)
    output_filename = "final_video.mp4"
    final_clip.write_videofile(output_filename, fps=24, codec="libx264", audio_codec="aac")
    
    if os.path.exists(output_filename):
        print(f"Success! File exists at: {os.path.abspath(output_filename)}")
    else:
        raise Exception("Error: final_video.mp4 was not created successfully!")

if __name__ == "__main__":
    main()
