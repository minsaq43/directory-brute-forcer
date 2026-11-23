import requests

url = input("Enter the url of the website you test? ")
wordlist = open("wordlist.txt").read().splitlines()
len(set(wordlist))
for word in wordlist:
    x = requests.get(url+"/"+word)
    print(f"Found: {url}/{word} - Status: {x.status_code}")
print(len(wordlist))