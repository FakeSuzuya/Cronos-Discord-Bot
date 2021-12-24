import os, sys, time, json


 
def get_emoji():
    with open("./utils/emoji.json",'r') as emoji:
        r = json.load(emoji)
    return r

def get_config():
    with open("config.json",'r') as config:
        z = json.load(config)
    return z

def get_prefix():
    with open("config.json",'r') as config:
        z = json.load(config)  
    return z["prefix"]

def clear():
    os.system("cls")
    
def close():
    time.sleep(5)
    sys.exit()
    
