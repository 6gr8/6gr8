import requests
import colorama
from colorama import Fore
import json
from time import sleep
from colorama import Fore, Back, Style
import sys,time
colorama.init(autoreset=True)
print(Fore.RED+f"""
                ▓██▓░▓▒                 
               ▓▓  ▒▒▒██▓░              
            ░▓█░      ░  █              
          ░█▓▒           ▒█             
          ▓▓              ▒█▒           
           █                ▒██░        
          █▓                 █▓         
          █▒                ▒█▒         
        ░▓█                ▒█           
      ▒█▓▓                 █▒            
   ▒█▓▒                     ██           {Fore.WHITE}
 ▓▓▓                        ▒█▒          [ My Instagram - @6gr8 ]
 █▒                          ▒█▓         [ My Telegram - RRRBG ]
  █                            ▒█▓▒      [ My Channel - DENS0R ]
  ██░                            ▒▓█          # Mr DeNsor :)
   ▓▓▓▓▓▓░                         ▒█   
        ▒▓█▓░                       █   
           ▓▓█▓                    ▒█▒  
              ▒██░                  ░█  
                ▒██░                 ▓▓ 
                  ▒██▒           ▓█▓▓▓█▓
                    ░██▒        ▒█      
                       ▒▓▒▒▒▒░░▒▓ 

""")
print(Fore.RED+"[?] This Tool For Info Your Account [ login ]")
usernamenew = input('[+] Enter username : ')
passwordnew = input('[+] Enter password : ')
urlloginnew = "https://i.instagram.com/api/v1/web/accounts/login/ajax/"
headrsnew = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '272',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
        'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '790551e77c76',
        'x-requested-with': 'XMLHttpRequest'}
datanew = {
        "username": usernamenew,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{passwordnew}",
        "queryParams": "{}",
        "optIntoOneTap": "false"}
req = requests.post(urlloginnew, headers=headrsnew, data=datanew)
if ("userId") in req.text:
     print(Fore.LIGHTMAGENTA_EX + 'Done Login ')
     cocke = req.cookies
     cocke2 = cocke.get_dict()
     cookie = f"sessionid={cocke2['sessionid']};"
elif ("two_factor") in req.text:
    print('two_factor')
    input("")
    exit(0)
elif ("checkpoint_url") in req.text:
    print('Account Secure')
    input("")
    exit(0)
else:
    print(Fore.LIGHTRED_EX +'The username or password is wrong')
    input("")
    exit(0)


headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/download/request/?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
get_email = req.json()["email_hint"]
print(Fore.GREEN+"[!] The Email Is "+" : "+get_email)

headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/former_phones?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Nums Is "+" : "+req.text)

headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/former_usernames?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Usernames Is "+" : "+req.text)

headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/former_bio_texts?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Bio's Is "+" : "+req.text)




headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/accounts_you_hide_stories_from?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Acc's You Hide Is "+" : "+req.text)


headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/former_full_names?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Name's Is "+" : "+req.text)



headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/former_emails?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Emails Linked Is "+" : "+req.text)



headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/accounts_you_blocked?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Acc's Blocked Is "+" : "+req.text)



headrsch = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'viewport-width': '1600'
}
data = ''
urlchange = 'https://www.instagram.com/accounts/access_tool/search_history?__a=1'


req = requests.get(urlchange,data=data,headers=headrsch,cookies=cocke2)
print(Fore.GREEN+"[!] The Search Is "+" : "+req.text)
input("")