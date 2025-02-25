import requests
from bs4 import BeautifulSoup
from voice import Voice
from lines import Line
from movie import Movie
from upload_video import Upload_Youtue
import random

voc = Voice()
li = Line()
mov = Movie()
up = Upload_Youtue()

global text

class youtue():
    def __init__(self):
        pass
        

    def scrap(self):
        page = requests.get("https://www.biblestudytools.com/bible-verse-of-the-day/")
        soup = BeautifulSoup(page.text,"html.parser")

        verse = soup.find_all("h2",attrs={"class":"mb-5 text-lg md:text-2xl font-bold flex-grow"})
        chap = soup.find_all("a",attrs={"class":"text-blue-600 font-bold text-2xl"})
        read = soup.find_all("div",attrs={"class":"leading-8 rounded my-1"})
        gos = []

        # for verses in verse:
        #     gos.append(verses.text.strip("\n "))
        #     print(gos)
        # for chapt in chap:
        #     gos.append(chapt.text.strip("\n "))
        #     print(gos)
        # for reading in read:
        #     gos.append(reading.text.strip("\n "))
        # print(gos[0:3])
        for verses,chapt,reading in zip(verse,chap,read):
            text = verses.text+","+chapt.text+","+reading.text
            text = " ".join(text.split())
            # print(text)
        Day = verses.text.strip(" \n")
        bible = chapt.text.strip(" \n")
        gospel =f"Todays Word of God {bible} \n #Bible #Gospel #Jesus #Christanity"
        li.cut_lines(text)
        print(text)
        voc.to_voice(text)

        input = ["src/input.mp4","src/input2.mp4","src/input3.mp4"]
        input_choice = random.choice(input)
        print(input_choice)

        mov.to_video(input_choice,text,"output.mp3")
        up.authenticate_youtube(Day,gospel)

        # print(verse[0].strip(" \n "))
        




yt = youtue()
yt.scrap()

