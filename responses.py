import random
import re

def handle_response(message) -> str:
    message = message.lower()
    if "<:hue:945524033338900560>" in message or message == "<:jU570fSTMucYUKyohxNC1g:946211396901818439>" : #guilds of ravenwind specific emoji
        return "<:hue:945524033338900560>"
    
    if message == "roll d20":
        return str(random.randint(1,20)) 
    
    if message == "who is bitch":
        listName = ["josh", "kevin", "taylor","leelee", "sam", "sam lmao", "laklan"]
        n = random.randint(1,len(listName))
        return listName[n-1]
    
    if message == "bitch":
        return "ur the bitch"
    
    if message == "sex":
        return "i know what sex is but i wont tell you"
    
    if (message =="<:hue:945524033338900560> help") or message == "hueHelp":
        return "nah <:hue:945524033338900560>"
    
    if message == "bruh":
        return ":moyai:"
    
    if message.split()[0] == "annoy":
        return f"nerd {message.split()[1]}"
    
    if "idk" in message:
        return "stupid bitch"
    
    if "bruh" in message:
        return "moyai"

    if message.split()[0] == "roll": #dice roller
        dieList = re.split("[\s|\+]",message)
        
        dieNumber = int(dieList[1].replace("d", ""))
        
        dieNumber = random.randint(0,dieNumber)
        string = "roll: " + str(dieNumber)
        
        if len(dieList) == 3:
            finalNumber = dieNumber + int(dieList[2])
        else:
            finalNumber = dieNumber
        
        string2 = "total: " + str(finalNumber)
        return string + " " + string2
    
    if message.split()[0] == "size":
        number = random.randint(0,10)
        string = number*"="
        if len(message.split()) > 1:
            user = message.split()[1]
            return f"{user}'s size: 8"+string+"D"
        else:
            return "ur size: 8"+string+"D"
        
    if message.split()[0] == "8ball":
        ballList = ["yeah lmao <:hue:945524033338900560>", "bruhaps :moyai:", 
                    "probably", "nah", "ur lame"]
        n = random.randint(0,len(ballList))
        return ballList[n-1]
    
    if message == "among us":
        return "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ ⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ ⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ ⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ ⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ ⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ ⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ ⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀ ⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ ⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
    
    if message == "aha":
        return ":eyes:....nah nevermind.... <:eyes2:935047776293752872>...unless?"
    
    if message == "<a:battle:1026408741433770045>": #guilds of ravenwind specific groove
        return "<a:groove:1026408727236051006>"
    
    if message == "<a:groove:1026408727236051006>":
        return "<a:battle:1026408741433770045>"