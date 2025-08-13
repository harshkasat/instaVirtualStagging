from moviepy import (
    ImageClip,
    concatenate_videoclips,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
)

# Paths
before_img = "assets/before.png"
after_img = "assets/after.png"
audio_file = "assets/songs/Apt.mp3"

# Video settings
duration = 1  # Total duration for the combined video
video_width = 1080
video_height = 1920  # Portrait/vertical format

# Load and resize images to fit half the screen height
before_clip = ImageClip(before_img, duration=duration).resized(width=video_width)
after_clip = ImageClip(after_img, duration=duration).resized(width=video_width)

# Calculate half height for each section
half_height = video_height // 2

# Resize clips to half height while maintaining aspect ratio
before_clip = before_clip.resized(height=half_height)
after_clip = after_clip.resized(height=half_height)

# Create text overlays
before_text = TextClip(text="Before", font_size=80, color="white", duration=duration, size=(None, None), margin=(20, 20), font="assets/didot/Didot Bold.otf")

after_text = TextClip(text="After", font_size=80, color="white", duration=duration, size=(None, None), margin=(20, 20), font="assets/didot/Didot Bold.otf")

# Position before section at top
before_positioned = before_clip.with_position(("center", 0))
before_text_positioned = before_text.with_position((50, half_height - 170))

# Position after section at bottom
after_positioned = after_clip.with_position(("center", half_height))
after_text_positioned = after_text.with_position((50, video_height - 170))

# Create the combined video with both sections visible simultaneously
final_video = CompositeVideoClip(
    [
        before_positioned,
        after_positioned,
        before_text_positioned,
        after_text_positioned,
    ],
    size=(video_width, video_height),
)

# Add audio
try:
    audio = AudioFileClip(audio_file)
    # Adjust audio duration to match video
    if audio.duration > duration:
        audio = audio.subclipped(0, duration)
    elif audio.duration < duration:
        # Loop audio if it's shorter than video
        loops_needed = int(duration / audio.duration) + 1
        audio_clips = [audio] * loops_needed
        audio = concatenate_videoclips(audio_clips)
        audio = audio.subclipped(0, duration)

    final_video = final_video.with_audio(audio)
except Exception as e:
    print(f"Audio error: {e}. Continuing without audio...")

# Export video
print("Exporting video...")
final_video.write_videofile(
    "before_after_split.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac" if "audio" in locals() and audio else None,
)

print("Video created successfully!")

# Clean up
final_video.close()
if "audio" in locals():
    audio.close()
