import pyttsx3
from pydub import AudioSegment
from pydub.playback import play

class Voice():
    def __init__(self):
        pass

    def to_voice(self,text):
        engine = pyttsx3.init()
        engine.setProperty("rate",155)
        engine.setProperty("volume",1)

        # engine.save_to_file(text)
        engine.save_to_file(text,"output.mp3")
        engine.runAndWait()