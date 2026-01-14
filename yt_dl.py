from pytube import YouTube
import os
import tkinter


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    # Calculate the progress in percentage
    progress = (bytes_downloaded / total_size) * 100
    print(f"Downloading... {progress:.2f}% done")

def on_complete(stream, file_handle):
    print("Download completed!")

while True:
    print("----------------------------------------------------------! Welcome on the PyTube Youtube Downloader !---------------------------------------------------------")
    print("-------------------------------------------! Make sure to have a stable internet connexion while using this tool !---------------------------------------------")
    print("Menu\n")
    print("1. Download a video with the sound")
    print("2. Download a video without the sound")
    print("3. Download just the song of a video")
    print("0. Exit")

    choice = int(input("Choose an option (0-3) : "))

    if choice == 0:
        break

    elif choice == 1:
        link = input("Input the link of the YouTube video: ")
        print("Quality of the video")
        print("1. UHD : 1080p")
        print("2. HD : 720p")
        print("0. Exit")

        choice1 = int(input("Choose an option (0-2) : "))

        if choice1 == 0:
            break

        elif choice1 == 1:
            def downloadHighResVideo(url, output_folder="."):
                try:
                    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
                    video = yt.streams.get_highest_resolution()
                    print("Download of the video : {}".format(yt.title))
                    print("Size of the video : {} MB".format(round(video.filesize / (1024 * 1024), 2)))
                    download_path = os.path.join(output_folder, "{}.mp4".format(yt.title))
                    video.download(output_folder)
                    print("Download completed! The video has been saved to {}".format(download_path))
                except Exception as e:
                    print("An error occurred: {}".format(str(e)))

            output_folder = input("Enter the full path of the location where you want to save the video (press Enter to save it in the current folder) : ")
            downloadHighResVideo(link, output_folder)

        elif choice1 == 2:
            def downloadLowResVideo(url, output_folder=".", resolution="720p"):
                try:
                    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
                    video = yt.streams.filter(res=f"{resolution}").first()
                    print("Download of the video : {}".format(yt.title))
                    print("Size of the video : {} MB".format(round(video.filesize / (1024 * 1024), 2)))
                    download_path = os.path.join(output_folder, "{}.mp4".format(yt.title))
                    video.download(output_folder)
                    print("Download completed! The video has been saved to {}".format(download_path))
                except Exception as e:
                    print("An error occurred: {}".format(str(e)))

            output_folder = input("Enter the full path of the location where you want to save the video (press Enter to save it in the current folder) : ")
            downloadLowResVideo(link, output_folder, resolution="720p")

    elif choice == 2:
        link = input("Input the link of the YouTube video: ")
        print("Quality of the video\n")
        print("1. UHD : 1080p")
        print("2. HD : 720p")
        print("0. Exit")

        choice2 = int(input("Choose an option (0-2): "))

        if choice2 == 0:
            break

        elif choice2 == 1:
            def downloadHighResVideoWithoutAudio(url, output_folder="."):
                try:
                    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
                    video = yt.streams.filter(file_extension="mp4", only_video=True).first()
                    print("Download of the video without audio: {}".format(yt.title))
                    print("Size of the video: {} MB".format(round(video.filesize / (1024 * 1024), 2)))
                    download_path = os.path.join(output_folder, "{}_no_audio.mp4".format(yt.title))
                    video.download(output_folder)
                    print("Download completed! The video without audio has been saved to: {}".format(download_path))
                except Exception as e:
                    print("An error occurred: {}".format(str(e)))

            output_folder = input("Enter the full path of the location where you want to save the video (press Enter to save it in the current folder): ")
            downloadHighResVideoWithoutAudio(link, output_folder)

        elif choice2 == 2:
            def downloadLowResVideoWithoutAudio(url, output_folder=".", resolution="720p"):
                try:
                    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
                    video = yt.streams.filter(res=f"{resolution}", file_extension="mp4", only_video=True).first()
                    print("Download of the {} video without audio: {}".format(resolution, yt.title))
                    print("Size of the video: {} MB".format(round(video.filesize / (1024 * 1024), 2)))
                    download_path = os.path.join(output_folder, "{}_no_audio.mp4".format(yt.title))
                    video.download(output_folder)
                    print("Download completed! The video without audio has been saved to: {}".format(download_path))
                except Exception as e:
                    print("An error occurred: {}".format(str(e)))

            output_folder = input("Enter the full path of the location where you want to save the video (press Enter to save it in the current folder): ")
            downloadLowResVideoWithoutAudio(link, output_folder, resolution="720p")

    elif choice == 3 :
        link = input("Input the link of the YouTube video: ")
        print('Download mp3 file of a video')
        print("0. Exit")

        choice3 = int(input("If you want to quit, press 0"))

        if choice3 == 0 :
            break
        else :
            def downloadAudioOnly(url, output_folder="."):
                try:
                    yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=on_complete)
                    audio_stream = yt.streams.filter(file_extension="mp3", only_audio=True).first()
                    print("Download of the audio only: {}".format(yt.title))
                    print("Size of the audio: {} MB".format(round(audio_stream.filesize / (1024 * 1024), 2)))
                    download_path = os.path.join(output_folder, "{}_audio_only.mp4".format(yt.title))
                    audio_stream.download(output_folder)
                    print("Download completed! The audio has been saved to: {}".format(download_path))
                except Exception as e:
                    print("An error occurred: {}".format(str(e)))

            output_folder = input("Enter the full path of the location where you want to save the audio (press Enter to save it in the current folder): ")
            downloadAudioOnly(link, output_folder)
