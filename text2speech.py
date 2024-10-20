#read me 
"""

"""



# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os
import sys

# The text that you want to convert to audio
input_name = sys.argv[1] + '.txt'
mytext =  open(input_name, "r")

# Language in which you want to convert
language = 'es'
tld = 'com'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext.read(), lang=language, tld=tld, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
myobj.save(f"{input_name}.mp3")

# Playing the converted file
os.system(f"start {input_name}.mp3")