from convert_video_to_audio import convert_video_to_audio_ffmpeg, current_directory
import os

translate = False
dest_language = ""


# API_KEY = input("insert assemblyai Api key. You can get it on")
video_file = input("Input full path of video file.\n> ")
video_name = video_file.split('/')[-1].split(".")[0]


translate_subs = input("Translate subtitles? [y/N].\n> ")

if translate_subs.lower() == "yes" or translate_subs.lower() == "y":

    translate = True
    dest_language = input("Input language of subtitles.\n(Skip to use default [english])> ")

    if dest_language == "":
        dest_language = "en"

elif translate_subs.lower() != "no" and translate_subs.lower() != "n" and translate_subs != "":
    print("No such option. Try again.")
    exit()


orig_language = input("Input language of video.\n(Skip for autodetect)> ")

if orig_language == "":
    orig_language = "autodetect"
print("Processing...\n")

convert_video_to_audio_ffmpeg(video_file)

os.system(f'{current_directory}/venv-aai/bin/python {current_directory}/assemblyai_gen.py'
          f' {video_name} {orig_language} {translate} {dest_language}')


print("Done!\n")











