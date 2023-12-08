import PySimpleGUI as sg
from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("mpg123 output.mp3") #macos
    #os.system("start output.mp3") for windows

sg.theme('DarkBlue')

layout = [
    [sg.Text('écrivez votre texte:')],
    [sg.Multiline('', size=(60, 10), key='input_text')],
    [sg.Button('lire'), sg.Button('enregistrer le texte'), sg.Button('Exit')]
]

window = sg.Window('sauvegarde de texte et TTS', layout)

while True:
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break
    elif event == 'lire':
        text_to_speech(values['input_text'])
    elif event == 'enregistrer le texte':
        with open('output.txt', 'w') as f:
            f.write(values['input_text'])
        sg.popup('Text enregistré')

window.close()
