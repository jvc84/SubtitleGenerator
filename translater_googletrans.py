import sys

from convert_video_to_audio import current_directory
from googletrans import Translator
import subprocess

tr = Translator()


def translate_subtitles(subtitle_file, dest_language):
    file_name = subtitle_file.split("/")[-1].split(".")[0]
    new_file = f"{current_directory}/files/subtitles/{file_name}_{dest_language}.srt"

    subprocess.call([f"touch {new_file}"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT, shell=True)

    nf = open(new_file, "w")
    f = open(str(subtitle_file), "r+")

    for x in f:

        if "-->" in x:
            nf.write(x[:-1])
            nf.write("\n")

        elif x == "\n":
            nf.write("\n")

        else:
            try:
                data = tr.translate(x, dest_language)
                nf.write(data.text)
                nf.write("\n")

            except ValueError:
                for i in range(1000):
                    try:
                        data = tr.translate(x, dest_language)
                        nf.write(data.text)
                        nf.write("\n")
                        break

                    except:
                        continue
    f.close()
    nf.close()


translate_subtitles(sys.argv[1], sys.argv[2])
