# instaVirtualStagging

**A simple Python script to create before-and-after comparison videos for virtual staging.**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Project Overview

`instaVirtualStagging` is a Python project that generates short comparison videos showcasing "before" and "after" images, ideal for virtual staging in real estate or similar applications.  It uses the `moviepy` library to create a video with two images side-by-side, overlaid with "Before" and "After" text, and accompanied by an audio track.  The script is designed to be easy to use, requiring minimal configuration.

## Table of Contents

* [Project Overview](#project-overview)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Project Architecture](#project-architecture)
* [Contributing](#contributing)
* [License](#license)


## Prerequisites

* Python 3.11 or higher
* `moviepy>=2.2.1`
* `pillow>=11.3.0`
* An audio file (MP3 recommended)
* Two images ("before" and "after") to be compared.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/harshkasat/instaVirtualStagging.git
   cd instaVirtualStagging
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare your assets:** Place your "before" image (`before.png`), "after" image (`after.png`), and audio file (`Apt.mp3`) in the `assets/` and `assets/songs/` directories respectively.  Ensure the images are appropriately sized.  The script currently assumes a portrait (vertical) orientation.

2. **Run the script:**
   ```bash
   python main.py
   ```

This will generate a video named `before_after_split.mp4` in the same directory.


## Project Architecture

The project consists of two main Python files:

* **`main.py`:** This file serves as the entry point for the application. It calls the `collage.py` script to create the video.

* **`collage.py`:** This file contains the core logic for creating the video collage using the `moviepy` library.  It loads images, adds text overlays, combines them into a composite video, adds audio, and exports the final video file.

Here's a snippet from `collage.py` showing the core video creation process:

```python
# Load and resize images
before_clip = ImageClip(before_img, duration=duration).resized(width=video_width)
after_clip = ImageClip(after_img, duration=duration).resized(width=video_width)

# ... (other image and text manipulation) ...

# Create the combined video
final_video = CompositeVideoClip(
    [before_positioned, after_positioned, before_text_positioned, after_text_positioned],
    size=(video_width, video_height),
)

# Add audio (with error handling)
# ...

# Export video
final_video.write_videofile("before_after_split.mp4", fps=24, codec="libx264", audio_codec="aac")
```

## Contributing

Contributions are welcome! Please open an issue to discuss proposed changes before submitting a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
