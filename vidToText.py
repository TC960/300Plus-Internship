import speech_recognition as sr
import ffmpeg

def extractAudio(video_path, audio_path):
    stream = ffmpeg.input(video_path)
    stream = ffmpeg.output(stream, audio_path,
             acodec = "pcm_s16le", ac = 1, ar = "16000")
    ffmpeg.run(stream)


def extractText(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Speech Recognition could not understand audio"
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service"


extractAudio("sampleVid.mp4","OutputAudio.wav")

text = extractText("OutputAudio.wav")
with open("data.txt","w") as file:
    file.write(text)
    