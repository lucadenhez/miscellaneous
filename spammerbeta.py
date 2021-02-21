import os, sys, subprocess, requests

def getTokens():
    tokens = []
    f = open(f"{os.getcwd()}\\usertokens.txt", 'r')
    lines = f.read().splitlines()
    for line in lines:
        tokens.append(line)
    return tokens

def createFiles(message, tokens, victimID, amount):
    for i in range(len(tokens)):
        torep = f'''import discord
client = discord.Client()
@client.event
async def on_ready():
    victim = await client.fetch_user({victimID})
    for i in range({str(amount)}):
        await victim.send("{message}")
        print("[+] Account {str(i)} sent message.")
client.run("{tokens[i]}", bot=False)'''
        f = open(f"{os.getcwd()}\\spammer{str(i)}.py", 'w')
        f.write(torep)
        f.close()

def start(tokens, inviteCode):
    for i in range(len(tokens)):
        r = requests.post(f"https://discordapp.com/api/v8/invites/{inviteCode}?inputValue=SERVER_JOIN_STR&with_counts=true", headers={"authorization":tokens[i]})
        p = subprocess.Popen([sys.executable, f"{os.getcwd()}\\spammer{str(i)}.py"])

tokens = getTokens()
createFiles("abcd", tokens, 123456789, 100) # Message, Token list, Victim's ID, Amount for each account
print("")
start(tokens, "qX7CY9y") # Server invite link ID. In order to DM, there has to be a mutual server
