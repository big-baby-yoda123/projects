import webbrowser
import random
import datetime
import os
import audio

name = "Vladimir"

def doAction(respone):
    if respone == '*rickroll*':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
        return 'Have fun!'
    elif respone == "*starwars*":
        webbrowser.open('https://fmovies.to/search?keyword=star+wars&vrf=fQRB7QbizOJy8adcz6lgk')
        return 'Enjoy'
    elif respone == "*born*":
        date1 = datetime.date(2022, 4, 17)
        date2 = datetime.date.today()
        ans = "I was born in 17.04.2022 so I'm " + str((date2 - date1).days) + " days old"
        return ans
    elif respone == "*russianMode*":
        webbrowser.open('https://www.youtube.com/watch?v=GK2GUxOnjDQ&ab_channel=SebastianGiangregorio')
        return ""
    elif respone == "*openPlex*":
        webbrowser.open('http://127.0.0.1:32400/web/index.html#!/')
        return "Enjoy"
    elif respone == "*openNetflix*":
        webbrowser.open('https://www.netflix.com/browse')
        return "Enjoy"

def changeName(respone):
    name1 = ""
    if respone == "*changeName*":
        audio.speak("whats my new name")
        name1 = audio.get_audio()
        if audio.get_audio() == "yes":
            name = name1
    return name