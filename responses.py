import random

def handle_response(message) -> str:
    pMessage = message.lower()
    
    if pMessage == ":hue:":
        return ":hue:"
    
    if pMessage == "hi":
        return "hello"
    
    if pMessage == "<:hue:945524033338900560>": #guilds of ravenwind specific emoji
        return "<:hue:945524033338900560>"
    
    if pMessage == "roll d20":
        return str(random.randint(1,20)) 
    
    if pMessage == "bruh":
        pass