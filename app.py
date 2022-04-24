from distutils.command.clean import clean
from struct import pack
import tkinter as tk
import aiMind
import audio
import keyboard

def main1():
    def sendToAi():
        voice_input = ''
        while not keyboard.is_pressed('s'):
            voice_input = audio.get_audio()
            if "Vladimir" in voice_input:
                answer = aiMind.talk(voice_input)
                text.insert(tk.INSERT, answer)
                text.insert(tk.INSERT, "\n")
                audio.speak(answer)
                input.delete(0, tk.END)
    root = tk.Tk()
    canvas = tk.Canvas(root, height=400, width=400, bg = "#263D42")
    canvas.pack()
    farme = tk.Frame(root, bg="white")
    farme.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    input = tk.Entry(farme, bg="#DDDDDD")
    input.pack(side=tk.LEFT)
    askAi = tk.Button(root, text="ask AI", padx=10, pady=10, fg="white", bg="#263D42", command=sendToAi)
    text = tk.Text(farme)
    text.insert(tk.INSERT, "Vladimir: \n")
    text.pack(side=tk.RIGHT)
    askAi.pack()
    root.mainloop()
    
    
