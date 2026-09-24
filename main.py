
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
