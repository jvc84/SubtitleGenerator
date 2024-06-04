import subprocess
import os
from pathlib import Path


# Variables
current_directory = str(Path(__file__).parent.resolve())

audio_directory = current_directory + "/audio"

if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)

# Functions
def convert_video_to_audio_ffmpeg(video_file, output_ext="wav"):
    filename, ext = os.path.splitext(video_file)
    filename = filename.split("/")[-1]

    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{audio_directory}/{filename}.{output_ext}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)






