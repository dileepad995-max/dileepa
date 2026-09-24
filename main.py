import os
import requests
from google import genai
from gtts import gTTS
from moviepy.editor import VideoFileClip, AudioFileClip

def generate_script():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    prompt = (
        "Write a 40-second viral TikTok script about a street living silver statue "
        "who suddenly moves and shocks tourists. Hook the viewer in the first 3 seconds. "
        "Keep it engaging, emotional, and high-retention."
    )
    
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt,
    )
    return response.text.strip()

def download_pexels_video():
    api_key = os.environ.get("PEXELS_API_KEY")
    headers = {"Authorization": api_key}
    url = "https://api.pexels.com/videos/search?query=living+statue&per_page=1"
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if "videos" in data and len(data["videos"]) > 0:
        video_files = data["videos"][0]["video_files"]
        # Select an HD or suitable video link
        video_url = video_files[0]["link"]
        
        print("Downloading video from Pexels...")
        video_data = requests.get(video_url).content
        video_path = "temp_video.mp4"
        with open(video_path, "wb") as f:
            f.write(video_data)
        return video_path
    else:
        raise Exception("No videos found on Pexels for the given query.")

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

    # Trim video to match audio length if video is longer, or loop if needed
    if video_clip.duration > audio_clip.duration:
        video_clip = video_clip.subclip(0, audio_clip.duration)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
    print("Final video generated successfully as final_video.mp4!")

if __name__ == "__main__":
    main()
