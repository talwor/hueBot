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
    
    if pMessage == "who is bitch":
        n = random.randint(1,3)
        if n == 1:
            return "josh"
        
        if n == 2:
            return "kevin"
        
        if n == 3:
            return "taylor"
    
    if pMessage == "bitch":
        return "ur the bitch"
    
    if pMessage == "roll":
        return "69"
    
