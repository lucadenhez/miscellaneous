import requests, json

username = input("Username: ")
password = input("Password: ")
print("")

r = requests.post("https://luca-auth-api.herokuapp.com/auth", json = { "username" : username, "password" : password, "project" : "nuker" })

try:
    if r.status_code == 200:
        rjson = json.loads(r.text)
        nuker = requests.get(rjson["url"])
        open("nuker.png", "wb").write(nuker.content)
        print("Downloaded file. Check in this folder for a file named 'nuker.py'")
    elif r.status_code == 401:
        print("Invalid username or password.")
    elif r.status_code == 403:
        print("Error occured. Unable to download nuker.")
    else:
        print("Error occured. Unable to download nuker.")
except:
    print("Error occured. Unable to download nuker.")
