import requests


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

r = requests.get(url, auth=("huge", "file"))

print(r.cookies["info"])
