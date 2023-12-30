# PyTube YouTube Downloader

## Description
This is a simple command-line YouTube downloader script using PyTube library. It provides options to download videos with or without audio and to download only the audio of a video. Users can choose the quality/resolution of the video to download.

## Requirements
- Python 3.x
- PyTube library (install it using `pip install pytube`)

## How to Use
1. Run the script using `python yt_dl.py`.
2. Choose an option from the menu:
    - **Download a video with the sound**
    - **Download a video without the sound**
    - **Download just the song of a video**
    - **Exit**
   
### Download a video with sound
- Enter the YouTube video link.
- Choose the quality of the video (UHD or HD).
- Specify the output folder to save the video.

### Download a video without sound
- Enter the YouTube video link.
- Choose the quality of the video (UHD or HD).
- Specify the output folder to save the video without audio.

### Download just the song of a video
- Enter the YouTube video link.
- Specify the output folder to save the audio-only file.

## Progress Monitoring
The script provides progress updates during the download process, displaying the percentage completion.

## Callbacks
Two callback functions are defined:
- `on_progress`: Displays download progress in percentage.
- `on_complete`: Notifies when the download is completed.

## Examples
- Download a video with sound in UHD resolution:
  ```python
  Choose an option (1-3) : 1
  Input the link of the YouTube video: [YouTube Video Link]
  Choose an option (0-2) : 1
  Enter the full path of the location where you want to save the video: [Output Folder]
