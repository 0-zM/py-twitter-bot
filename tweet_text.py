"""Construct messages to be sent as tweet text"""

# Allows using time related functions
from datetime import datetime
# convert times according to time zones
from pytz import timezone

import random

def reply(tweet):
    """Return text to be used as a reply"""
    message = tweet['text']
    user = tweet['user']['screen_name']
    if "hi" in message.lower():
        berlin_time = datetime.now(timezone('Europe/Berlin'))
        date = berlin_time.strftime("It is %H:%M:%S on a %A.")
        return "Hi @" + user + "! " + date
    return None

def idle_text():
    """Return text that is tweeted when not replying"""
	
    # Construct the text we want to tweet out (280 chars max)
    berlin_time = datetime.now(timezone('Europe/Berlin'))
    formatted_time = berlin_time.strftime("%H:%M:%S")
    random.seed(formatted_time)
    
    blobfisch = []
    for i in range(16):
        blobfisch.append(random.choice(("1", "!")))
    	
    text = "I have a meeting with my " + random.choice((
		"doctor", 
		"hairdresser", 
		"manager", 
		"dentist",
		"friends",
		"brother",
		"sister",
		"grandparents",
		"teacher",
		"classmate",
		)) + " at " + formatted_time + ". WIR SIND BLOBFISCH" + "".join(blobfisch)
    return text
