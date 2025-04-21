import requests

# Obfuscated username using hex
u = ''.join(chr(x) for x in [0x6a, 0x6f, 0x6b, 0x65, 0x72])  # 'joker'

# Obfuscated password using ROT13-style shift
p = ''.join(
    chr(((ord(c) - 97 + 13) % 26) + 97) if c.islower() else c
    for c in 'qbaaxlqvrf'  # original string that becomes 'donkeydies'
)

# Direct GitHub raw file path (publicly accessible or private if creds work)
url = 'https://raw.githubusercontent.com/joker/dark-repo/main.py'

# Send request with basic auth
resp = requests.get(url, auth=(u, p))

if resp.status_code == 200:
    with open("downloaded.py", "wb") as f:
        f.write(resp.content)
    print("File downloaded as downloaded.py")
else:
    print(f"Failed: {resp.status_code} - {resp.text}")
