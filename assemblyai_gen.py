from convert_video_to_audio import current_directory

import assemblyai as aai
import sys
import os


aai.settings.api_key = "da50dd26ff3047b2bebe31b382ec28a5"

subtitle_directory = current_directory + '/subtitles'

if not os.path.exists(subtitle_directory):
    os.makedirs(subtitle_directory)

def generate_sub(video_name, orig_language, translate, dest_language):


    audio_file = current_directory + "/audio/" + video_name + ".wav"
    if orig_language == "autodetect":
        print("Autodetecting...")
        config = aai.TranscriptionConfig(language_detection=True)
    else:
        config = aai.TranscriptionConfig(language_code=f"{orig_language}")

    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(audio_file)
    subtitles = transcript.export_subtitles_srt()

    subtitle_file = f"{subtitle_directory}/{video_name}.srt"
    f = open(f"{subtitle_file}", 'a')
    f.write(subtitles)
    f.close()


    if translate:
        print("Translating...")
        if dest_language == "":
            dest_language = "en"

        os.system(f'{current_directory}/venv/bin/python {current_directory}/translater_googletrans.py '
                  f'{subtitle_file} {dest_language}')




generate_sub(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
