print('\033[31m' + r'''
 _______   _______    ______   __    __  __      __       
/       \ /       \  /      \ /  |  /  |/  \    /  |      
$$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |$$  \  /$$/       
$$ |__$$ |$$ |__$$ |$$ |  $$ |$$  \/$$/  $$  \/$$/        
$$    $$/ $$    $$< $$ |  $$ | $$  $$<    $$  $$/         
$$$$$$$/  $$$$$$$  |$$ |  $$ |  $$$$  \    $$$$/          
$$ |      $$ |  $$ |$$ \__$$ | $$ /$$  |    $$ |          
$$ |      $$ |  $$ |$$    $$/ $$ |  $$ |    $$ |          
$$/       $$/   $$/  $$$$$$/  $$/   $$/     $$/           
                                                          
                                                          
                                                          
 __        ______   ______   __    __  ________  _______  
/  |      /      | /      \ /  |  /  |/        |/       \ 
$$ |      $$$$$$/ /$$$$$$  |$$ | /$$/ $$$$$$$$/ $$$$$$$  |
$$ |        $$ |  $$ |  $$/ $$ |/$$/  $$ |__    $$ |__$$ | 
$$ |        $$ |  $$ |      $$  $$<   $$    |   $$    $$<  
$$ |        $$ |  $$ |   __ $$$$$  \  $$$$$/    $$$$$$$  | 
$$ |_____  _$$ |_ $$ \__/  |$$ |$$  \ $$ |_____ $$ |  $$ | 
$$       |/ $$   |$$    $$/ $$ | $$  |$$       |$$ |  $$ | 
$$$$$$$$/ $$$$$$/  $$$$$$/  $$/   $$/ $$$$$$$$/ $$/   $$/  
                                                          
                                                          
                                                          
''' + '\033[0m')
print("Welcome to Proxlicker!")
import asyncio
import aiohttp
import re
from termcolor import colored

async def get_proxies(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            proxies = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+", text)
            return proxies

async def main():
    urls = [
        "https://www.socks-proxy.net/",
        "https://www.us-proxy.org/",
        "https://free-proxy-list.net/uk-proxy.html",
        "https://www.sslproxies.org/",
        "https://www.proxy-list.download/SOCKS4/",
        "https://www.proxy-list.download/SOCKS4",
        "https://www.proxy-list.download/SOCKS4?api",
        "https://www.proxy-list.download/SOCKS4/proxylist.txt",
        "https://www.proxy-list.download/SOCKS4/proxylist.xml",
        "https://www.proxy-list.download/SOCKS4/proxylist.json"
    ]

    with open("results.txt", "w") as file:
        for i, url in enumerate(urls, 1):
            try:
                proxies = await get_proxies(url)
                for proxy in proxies:
                    file.write(proxy + "\n")
            except:
                print(colored(f"[ERROR] Could not get proxies from {url}", "red"))
            else:
                print(colored(f"[INFO] Proxies scraped from {url}", "green"))
            print(colored(f"[INFO] Progress: {i}/{len(urls)}", "yellow"))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
