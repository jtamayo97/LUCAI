# This is a WEAK virtual assistant called LUCAI
# This is to practice Python, APIs, & weak AI

import wolframalpha
client = wolframalpha.Client("WQPH5L-WLKTTL2J5K")

import PySimpleGUI as sg
import wikipedia

import pyttsx3
engine = pyttsx3.init()

sg.theme('DarkTeal')
layout = [  [sg.Text('What can I do for you?')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


# Create GUI
window = sg.Window('LUCAI', layout)



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.Popup("WolframAlpha: " + wolfram_res, "Wikipedia: " + wiki_res)
    except wikipedia.exceptions.DisambiguationError or wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

window.close()