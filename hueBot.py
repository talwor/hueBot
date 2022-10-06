import discord
import responses
import os
import assets
     
def runDiscordBot():
    TOKEN = 'MTAyNTQxNTI0NDEwNjk2OTE0OQ.GEOGan.y6jXdd8oWKAj9TxvxZvwihsK_1MgFwNRjGXH9w' #ask me for token if u want 
    
    intents = discord.Intents.all() #added from utube vid/new discord intents feature
    intents.message_content = True
    client = discord.Client(intents=intents) #
    
    client.login(TOKEN) #this at front, logs the bot in
    
    
    @client.event 
    async def on_ready():
        #status
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='farts'))
        
        
    @client.event
    async def on_message(message): #specific on_message format needed
        if message.author == client.user: #if message is itself, then stop, no looping lol
            return
        
        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{userMessage}' ({channel})")
        
        '''
        the following if statements are for multimedia
        '''
        
        if ("<:hue:945524033338900560>" in userMessage) or ("<:jU570fSTMucYUKyohxNC1g:946211396901818439>" in userMessage):
            await message.add_reaction("<:hue:945524033338900560>")
        
        if "sad" in userMessage:
            await message.channel.send(file=discord.File('assets/imageGif/moyai.png'))
        
        if userMessage == "anger":
            await message.channel.send(file=discord.File('assets/imageGif/wojak.gif'))
            
        if userMessage == "NOOO":
            await message.channel.send(file=discord.File('assets/imageGif/agonyman.gif'))
        
        if userMessage == "hue":
            await message.channel.send("did you mean", file=discord.File('assets/imageGif/haha.png'))
        
        '''
        else see if responses can do anything
        '''
        response = responses.handle_response(userMessage)
        await message.channel.send(response) 
        

    client.run(TOKEN) #have this at the end, makes sure that the bot runs
    
