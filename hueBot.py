import discord
import responses


async def sendMessage(message, userMessage, is_private):
    try:
        response = responses.handle_response(userMessage)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
        
def runDiscordBot():
    TOKEN = 'MTAyNTQxNTI0NDEwNjk2OTE0OQ.GRrbdu.qaF2mvFQjfQTkhhSyCE6Vvgh8fjdfqwltwJuV0'
    
    intents = discord.Intents.all() #added from utube vid/new discord intents feature
    intents.message_content = True
    client = discord.Client(intents=intents) #
    
    client.login(TOKEN) #this at front, logs the bot in
    
    @client.event 
    async def onReady():
        print("ready")
        
    @client.event
    async def on_message(message): #specific on_message format needed
        if message.author == client.user: #if message is itself, then stop, no looping lol
            return
        
        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{userMessage}' ({channel})")
        
        if userMessage[0] == '?':  #private messaging, if user does ? first
            userMessage = userMessage[1:]
            await sendMessage(message, userMessage, is_private=True)
        else:
            await sendMessage(message, userMessage, is_private=False)
    
    client.run(TOKEN) #have this at the end, makes sure that the bot runs
    
