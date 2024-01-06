import os
import requests
def get_proxies():
    os.system("cls")
    global pprr
    global working_proxies
    working_proxies = []
    rsp = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all') # proxyscrape link to fetch proxies from
    with open("proxies.txt","wb") as fp:
     fp.write(rsp.content) # Write proxies
     print("Success getting proxy list!")
     file = "proxies.txt"
     pprr = open(file).readlines()
    print("Proxies Counts %d" % len(pprr)) # count how many proxies it got

with open('proxies.txt') as f:
    proxies = f.readlines() # read the proxies in lines

if __name__ == "__main__":
 get_proxies()