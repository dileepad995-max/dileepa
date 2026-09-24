import os
import requests
from google import genai
from gtts import gTTS

def generate_script():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    prompt = (
        "Write a 40-second viral TikTok script about a street living silver statue "
        "who suddenly moves and shocks tourists. Hook the viewer in the first 3 seconds. "
        "Keep it engaging, emotional, and high-retention."
    )
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
    )
    return response.text.strip()

def main():
    print("Generating viral script...")
    script_text = generate_script()
    print(f"Script generated successfully:\n{script_text}")

    print("Generating voiceover audio...")
    tts = gTTS(text=script_text, lang='en', tld='com')
    audio_path = "audio.mp3"
    tts.save(audio_path)
    print("Audio generated successfully.")

if __name__ == "__main__":
    main()
