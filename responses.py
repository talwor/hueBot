import random
import re

def handle_response(message) -> str:
    pMessage = message.lower()
    if pMessage == "<:hue:945524033338900560>": #guilds of ravenwind specific emoji
        return "<:hue:945524033338900560>"
    
    if pMessage == "roll d20":
        return str(random.randint(1,20)) 
    
    if pMessage == "who is bitch":
        listName = ["josh", "kevin", "taylor","leelee", "sam", "sam lmao"]
        n = random.randint(1,len(listName))
        return listName[n-1]
    
    if pMessage == "bitch":
        return "ur the bitch"
    
    if pMessage == "sex":
        return "i know what sex is but i wont tell you"
    
    if pMessage =="help":
        return "nah <:hue:945524033338900560>"
    
    if pMessage == "bruh":
        return ":moyai:"
    
    if pMessage.split()[0] == "annoy":
        return f"nerd {pMessage.split()[1]}"
    
    if "HAH" in message:
        return "shut up"
    
    if "idk" in message:
        return "stupid bitch"

    if pMessage.split()[0] == "roll": #dice roller
        dieList = re.split("[\s|\+]",pMessage)
        
        dieNumber = int(dieList[1].replace("d", ""))
        
        dieNumber = random.randint(0,dieNumber)
        string = "roll: " + str(dieNumber)
        
        if len(dieList) == 3:
            finalNumber = dieNumber + int(dieList[2])
        else:
            finalNumber = dieNumber
        
        string2 = "total: " + str(finalNumber)
        return string + " " + string2
    
    if pMessage.split()[0] == "size":
        number = random.randint(0,10)
        string = number*"="
        if len(pMessage.split()) > 1:
            user = pMessage.split()[1]
            return f"{user}'s size: 8"+string+"D"
        else:
            return "ur size: 8"+string+"D"
        
    if pMessage.split()[0] == "8ball":
        ballList = ["yeah lmao <:hue:945524033338900560>", "bruhaps :moyai:", "yeah nah yeah nah"
                    "nah", "fuck off", "u suk", "probably"]
        n = random.randint(0,len(ballList))
        return ballList[n-1]