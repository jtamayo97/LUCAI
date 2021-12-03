# This is a WEAK virtual assistant called LUCAI
# This is to practice Python, APIs, & weak AI
# This program will take user input and retrieve responses from both 
# WolframAlpha and wikipedia
# 
# WolframAlpha will return the mathematical results
# Wikipedia will return the first 2 full sentences


# Importing wolfram API & Wikipedia API 
import wolframalpha
client = wolframalpha.Client("key-goes-here")

import PySimpleGUI as sg
import wikipedia

# Addind text to speech
# When clicking 'ok' system will read out the response
import pyttsx3
engine = pyttsx3.init()

# Setting up the GUI for user input
sg.theme('DarkTeal')
layout = [  [sg.Text('What can I do for you?')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create GUI
window = sg.Window('LUCAI', layout)


# Program will store user input as 'values'
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
        
    # Parses query('values') for a wolframalpha response then displays
    # Program will parse for a response from both APIs 
    # Ex: Input: 2+2 returns 4 from Wolfram and the first 2 full sentence listed in Wikipedia
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.Popup("WolframAlpha: " + wolfram_res, "Wikipedia: " + wiki_res)
        
    # Error handling if page is disambiguous or page does not exist
    except wikipedia.exceptions.DisambiguationError or wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
        
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
        
    # Summary of values parsed returning first 2 sentences
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

window.close()
