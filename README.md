# Directory Brute Forcer - Mini Gobuster

A simple Python Directory Brute Forcer I built to understand how Gobuster works behind the scenes.

## What does it do?

- Takes a website URL from the user
- Takes a wordlist of common directory names
- Tries each word: website + / + word
- Shows which directories EXIST

## How to use it?

1. Make sure you have requests installed:
   pip install requests

2. Run the file:
   python Directory_Brute_Forcer.py

3. Enter website when it asks:
   Example: https://example.com

4. It will print:
   Found: https://example.com/admin - Status: 200
   Found: https://example.com/login - Status: 200

## What is a status code?

- 200 = Page EXISTS - Found!
- 403 = Page EXISTS but Forbidden - Also interesting!
- 301 / 302 = Page Redirects - Also interesting!
- 404 = Page DOES NOT EXIST - Ignore, move on

My tool only prints 200 / 403 / 301 pages, so you don't get 1000 lines of 404 errors.

## What did I learn?

- How HTTP requests work
- What `requests.get()` and `.status_code` do
- Why 200 vs 404 matters in pentesting
- How to use a wordlist file: `open().read().splitlines()`
- How Gobuster finds hidden admin panels, backup files, and config files

## Files in this repo

- `Directory_Brute_Forcer.py` - Main tool
- `wordlist.txt` - List of common directory names (1800+ words)

## Disclaimer

For learning and authorized testing only. Only test websites you own or have permission to test, like TryHackMe labs or Bug Bounty programs.

