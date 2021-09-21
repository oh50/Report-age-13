from time import sleep
import time
import urllib.request
import urllib.error
import requests
from user_agent import generate_user_agent as oh50
print("""─────────────────────────────────────────────────────────────
─██████████████─██████──██████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─██░░██──██░░██─██░░██████████─██░░██████░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─
─██░░██──██░░██─██░░██████░░██─██░░██████████─██░░██──██░░██─
─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─
─██░░██──██░░██─██░░██████░░██─██████████░░██─██░░██──██░░██─
─██░░██──██░░██─██░░██──██░░██─────────██░░██─██░░██──██░░██─
─██░░██████░░██─██░░██──██░░██─██████████░░██─██░░██████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████████████─██████──██████─██████████████─██████████████─
                [•]    Report age  [•] 
           
           #program @oh50 - the tool free no sale
─────────────────────────────────────────────────────────────""")
username = str(input ("[+] Entar username : "))
name = str(input ("[+] Entar name : "))
email = str(input ("[+] Entar email : "))
year = str(input("[+] Entar year : "))
month = str(input("[+] Enter month : "))
day = str(input("[+] Enter day : "))
def oh50_insta():
    mr = 0
    # program @oh50 - the tool free no sale
    # program @oh50 - the tool free no sale
    while True:
        url = 'https://help.instagram.com/ajax/help/contact/submit/page'
        headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '687',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'locale=da_DK; ig_did=DA785FED-B4D7-4458-B5AB-452EC9D68598; datr=OsAkYbQMl6-ctk_ys8cCUj3E',
        'origin': 'https://help.instagram.com',
        'referer': 'https://help.instagram.com/contact/723586364339719',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': oh50(),
        'x-fb-lsd': 'AVqhF2BvhE',
        }
#program @oh50 - the tool free no sale
        data = {
        'jazoest': '2918',
        'lsd': 'AVqhF2BvhEI',
        f'Field258021274378282': '{name}',
        f'Field735407019826414': '{username}',
        'Field506888789421014[year]': '{year}',
        'Field506888789421014[month]': 'month',
        'Field506888789421014[day]': 'day',
        'Field294540267362199': 'Parent',
        f'inputEmail': '{email}',
        'support_form_id': '723586364339719',
        'support_form_hidden_fields': '{}',
        'support_form_fact_false_fields': '[]',
        '__user': '0',
        '__a': '1',
        '__dyn': '7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W09yyE',
        '__csr': '',
        '__req': '6',
        '__hs': '18863.PHASED:DEFAULT.2.0.0.0.0',
        'dpr': '1',
        '__ccg': 'EXCELLENT',
        '__rev': '1004298000',
        '__s': 'zalzpr:rjfsiy:rat1n4',
        '__hsi': '6999932813373668269-0',
        '__comet_req': '0',
        '__spin_r': '1004298000',
        '__spin_b': 'trunk',
        '__spin_t': '1629798862',
        }
        raspone = requests.post(url,headers=headers,data=data).text
        mr+=1
        print (f'[{mr}] [+] Done')
        sleep(5)
#program @oh50 - the tool free no sale
oh50_insta()