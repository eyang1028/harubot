import random
import os

p = './pics/'

def getToken():
    return os.getenv('DISCORD_BOT_TOKEN')

def isImage(attachment):
    url = attachment.url;
    isPng = url[-len('png'):] == 'png'
    isJpg = url[-len('jpg'):] == 'jpg' 
    isGif = url[-len('gif'):] == 'gif'
    return isPng or isJpg or isGif

def numPics():
    pics = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
    return len(pics)

def getPic():
    return random.choice(os.listdir(p)) 

def getRandom():
    return random.random()
