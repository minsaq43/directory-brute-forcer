import requests

url = input("Enter the url of the website you test? ")
wordlist = open("wordlist.txt").read().splitlines()

for word in wordlist:
    x = requests.get("https://"+url+"/"+word ,timeout=5)
    if x.status_code == 200:
     print(f"Found: {url}/{word} - Status: {x.status_code}")
print(len(wordlist))
