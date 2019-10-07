"""
bus.py
Demonstrate a dictionary.
"""

import sys
import os
import tempfile
import playsound
import gtts   #Google Text-To-Speech

bus = {
    "wheels": "round and round",
    "wipers": "swish, swish, swish",
    "horn": "beep,beep,beep",
    "doors": "open and shut",
    "driver": "move on back",
    "babies": "move on back",
    "mommies": "shush, shush, shush",
    "muggers": "bang, bang, bang"
}

song = ""
song3 = " All through the town"
for things in bus:
    song1 = " The " + things + " on the bus go " + bus[things]
    song2 = " " + bus[things] + "," + bus[things]
    song = song + song1 + song2 + song3
    
try:
    textToSpeech = gtts.gTTS(text = song, lang = lang, slow = True)
except BaseException as error:
    print(error, file = sys.stderr)
    sys.exit(1)

# Save the audio in a temporary file with a name.
temporaryFile = tempfile.NamedTemporaryFile()
textToSpeech.save(temporaryFile.name)

# Play and erase the temporary file.
try:
    playsound.playsound(temporaryFile.name, True)   #Requires a filename or URL.
except OSError as error:
    print(error, file = sys.stderr)
    sys.exit(1)
finally:
    temporaryFile.close()   #Erases the temporary file.

sys.exit(0)
