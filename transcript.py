import pytube
import whisper
from os import remove
from os import path
from googletrans import Translator


youtubeUrl = input("Ingrese la url del video a transcribir de youtube ")
youtubeVideo = pytube.YouTube(youtubeUrl)

audio = youtubeVideo.streams.get_audio_only()

audio.download(filename="tmp.mp4")

model = whisper.load_model("large")

result = model.transcribe("tmp.mp4")

f = open("traduccion_original.txt", "w")
f.write(result["text"])
f.close()

if path.exists("/home/turko/codigo/codes/youtube_transcribe_video/tmp.mp4"):
    remove("/home/turko/codigo/codes/youtube_transcribe_video/tmp.mp4")

traducir_english_spanish = input("Desea traducir del ingles al castellano? y/n : ")
if traducir_english_spanish == "y":
    with open("/home/turko/codigo/codes/youtube_transcribe_video/traduccion_original.txt") as file:
        txt = file.read()
        traductor = Translator()

        file = traductor.translate(txt, dest="es", src="en").text
        f = open("traduccion_español.txt", "w")
        f.write(file)
        f.close()
  




