
import os
import threading
import requests
import ctypes
import random
import json
import time
import base64
import sys
import re
from prettytable import PrettyTable
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Function to print the colored title with gradient colors
def print_colored_title():
    print(Fore.YELLOW + "           .-/+osssso+/-`")
    print(Fore.GREEN + "                   `/sdNMMMMMMMMMMMMMMNds/`")
    print(Fore.GREEN + "                .odMMMMMMMMMMMMMMMMMMMMMMMMdo.")
    print(Fore.YELLOW + "              :hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh:")
    print(Fore.RED + "            -dMMMNmMMMMMMMNNNNNNNNNNMMMMMMMmNMMMd-")
    print(Fore.RED + "          `sMNNs-oMMMMNNNNNNNNNNNNNNNNNNMMMMo-sNNMs")
    print(Fore.RED + "         `dM+s-:sMMMNNNNNNNNNNNNNNNNNNNNNNMMMs-:s+Md`")
    print(Fore.RED + "        `mho.h/:dMNNMMMNMMNmNoso-dmNMMNMMMNNMd:/d`ohm`")
    print(Fore.RED + "        hs//::oMMNMMMMNMMMMNMmmo+NNMMMMNMMMMNMNo:-+:yh")
    print(Fore.YELLOW + "       /M--y+:hMNNNNNNNMMMNNMMmmMMNMMMMNNNNNNNMh:oy.:M:")
    print(Fore.YELLOW + "       dd+./.hMNMMMMMNMMMNNNNNooNNNNNMMMNMMMMMNMy./.odh")
    print(Fore.GREEN + "      `M-m-/yyMNMMMMMNMMMMNMNdssdNMNMMMMNMMMMMNMyy/-m-N")
    print(Fore.GREEN + "      `M:-ho`NMNNNNNNNNNmho-sN:/Ms-shmNNNNNNNNNMm`sh-/M`")
    print(Fore.GREEN + "      `Mh`+ sdMNMMMMMh`     NMosMN     `dMMMMMNMdo`/`hN")
    print(Fore.YELLOW + "       d/h/.m.MNMMMMM+      yM--My      oMMMMMNM.m`/h/h")
    print(Fore.YELLOW + "       /d`/ss mNNNNNN-      `d.-h`      -NNNNNNd ss/`d:")
    print(Fore.RED + "        hm/`+ d:mNMMN                    NMMNd:h`+`/mh")
    print(Fore.RED + "        `doss/++.mNNh                    hNNm`o//ssod`")
    print(Fore.RED + "         `ds.:+y-:sso                    osy:-y+--sd`")
    print(Fore.RED + "           sMy+/:./+                      +/.:/+yMs")
    print(Fore.RED + "            -dyo/////.```            ```./////ohh-")
    print(Fore.YELLOW + "              :hMhoosss/`            `/sssoohMh:")
    print(Fore.YELLOW + "                .ohysoos.            .soosyh+`")
    print(Fore.YELLOW + "                   `/sdN`            `Nds/`")

    print(Fore.GREEN + "╔════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.GREEN + "║" + Fore.RED + "    ...::::[ " + Fore.YELLOW + "Tool by Tricker - TIENPHAT🇻🇳" + Fore.RED + " ]::::..." + Fore.GREEN + "                                          ║")
    print(Fore.GREEN + "╠════════════════════════════════════════════════════════════════════════════════════════════════╣")
    print(Fore.GREEN + "║" + Fore.YELLOW + "    => TOOL Buff View Tiktok Zefoy" + Fore.GREEN + "                                                                                     ║")
    print(Fore.GREEN + "║" + Fore.YELLOW + "    => Author: Tricker TIENPHAT🇻🇳" + Fore.GREEN + "                                                                                    ║")
    print(Fore.GREEN + "║" + Fore.YELLOW + "    => Telegram Group : https://t.me/+rUfJ7XrlHFM1YzY1" + Fore.GREEN + "                                                                 ║")
    print(Fore.GREEN + "╚════════════════════════════════════════════════════════════════════════════════════════════════╝")

# Function to run the tool with a counter
def run_tool():
    global run_counter
    run_counter += 1
    os.system("cls" if os.name == "nt" else "clear")

    # Print the colored title with gradient effect
    print_colored_title()
    print(f"{Fore.YELLOW}Tool has been run {run_counter} times.")

# Initialize run counter
run_counter = 0

# Example of running the tool
run_tool()
class Zefoy:
    def __init__(self):
        self.base_url = 'https://zefoy.com/'
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.captcha_1 = None
        self.captcha_ = {}
        self.service = 'Views'
        self.video_key = None
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = 'None'
        self.text = 'Tool Zefoy'
        import time
import requests
from colorama import Fore

class Zefoy:
    def __init__(self):
        self.base_url = 'https://zefoy.com/'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        self.session = requests.Session()
        self.captcha_1 = None
        self.captcha_ = {}
        self.video_key = None
        self.services = {}
        self.services_ids = {}
        self.services_status = {}
        self.url = 'None'
        self.text = 'Tool Zefoy'

        url1=input("Enter video link: ")
        self.url=url1
        
        # Khởi tạo khóa
        self.key = None
        self.key_expiry = None
        self.ask_for_key()

    def ask_for_key(self):
        valid_keys = {
            "key_abcfree2904toollphat": 24 * 60 * 60,  # 24 hours in seconds
            "key_30daysphattoool": 30 * 24 * 60 * 60  # 30 days in seconds
        }

        def is_key_valid(key):
            return key in valid_keys

        def get_key_expiry(key):
            return time.time() + valid_keys.get(key, 0)

        while True:
            key = input("Enter your key: ").strip()
            if is_key_valid(key):
                self.key = key
                self.key_expiry = get_key_expiry(key)
                print(f"{Fore.GREEN}Key accepted.")
                break
            else:
                print(f"{Fore.RED}Invalid key. Please try again.")

    def is_key_active(self):
        if self.key is None:
            return False
        return time.time() < self.key_expiry
        
    def get_captcha(self):
        if os.path.exists('session'): self.session.cookies.set("PHPSESSID", open('session',encoding='utf-8').read(), domain='zefoy.com')
        request = self.session.get(self.base_url, headers=self.headers)
        if 'Enter Video URL' in request.text: self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]; return True

        try:
            for x in re.findall(r'<input type="hidden" name="(.*)" value="(.*)">', request.text): self.captcha_[x[0]] = x[1]

            self.captcha_1 = request.text.split('type="text" name="')[1].split('" oninput="this.value=this.value.toLowerCase()"')[0]
            captcha_url = request.text.split('<img src="')[1].split('" onerror="imgOnError()" class="')[0]
            request = self.session.get(f"{self.base_url}{captcha_url}",headers=self.headers)
            open('captcha.png', 'wb').write(request.content)
            print('🧠Solving captcha..')
            return False
        except Exception as e:
            print(f"❌Unable to solve captcha: {e}")
            time.sleep(2)
            self.get_captcha()

    def send_captcha(self, new_session = False):
        if new_session: self.session = requests.Session(); os.remove('session'); time.sleep(2)
        if self.get_captcha(): print('🌐Connecting to session');return (True, 'The session already exists')
        captcha_solve = self.solve_captcha('captcha.png')[1]
        self.captcha_[self.captcha_1] = captcha_solve
        request = self.session.post(self.base_url, headers=self.headers, data=self.captcha_)

        if 'Enter Video URL' in request.text: 
            print('🌐Session has been created')
            open('session','w',encoding='utf-8').write(self.session.cookies.get('PHPSESSID'))
            print(f"✅Captcha solved successfully: {captcha_solve}")
            self.video_key = request.text.split('" placeholder="Enter Video URL"')[0].split('name="')[-1]
            return (True,captcha_solve)
        else: return (False,captcha_solve)

    def solve_captcha(self, path_to_file = None, b64 = None, delete_tag = ['\n','\r']):
        if path_to_file: task = path_to_file
        else: open('temp.png','wb').write(base64.b64decode(b64)); task = 'temp.png'
        request = self.session.post('https://api.ocr.space/parse/image?K87899142388957', headers={'apikey':'K87899142388957'}, files={'task':open(task,'rb')}).json()
        solved_text = request['ParsedResults'][0]['ParsedText']
        for x in delete_tag: solved_text = solved_text.replace(x,'')
        return (True, solved_text)

    def get_status_services(self):
        request = self.session.get(self.base_url, headers=self.headers).text
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+\n.+', request): self.services[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = x.split('d-sm-inline-block">')[1].split('</small>')[0].strip()
        for x in re.findall(r'<h5 class="card-title mb-3">.+</h5>\n<form action=".+">', request): self.services_ids[x.split('title mb-3">')[1].split('<')[0].strip()] = x.split('<form action="')[1].split('">')[0].strip()
        for x in re.findall(r'<h5 class="card-title">.+</h5>\n.+<button .+', request): self.services_status[x.split('<h5 class="card-title">')[1].split('<')[0].strip()] = False if 'disabled class' in x else True
        return (self.services, self.services_status)

    def get_table(self, i = 1):
        table = PrettyTable(field_names=["ID", "SERVICE", "Status"], title="Status Services", header_style="upper",border=True)
        while True:
            if len(self.get_status_services()[0])>1:break
            else:print('Cant get services, retrying...');self.send_captcha();time.sleep(2)
        for service in self.services:
            table.add_row([f"{Fore.CYAN}{i}{Fore.RESET}", service, f"{Fore.GREEN if 'ago updated' in self.services[service] else Fore.RED}{self.services[service]}{Fore.RESET}"])
            i += 1
        table.title = f"{Fore.YELLOW}Number of Active Services: {len([x for x in self.services_status if self.services_status[x]])}{Fore.RESET}"
        print(table)

    def find_video(self):
        if self.service is None: return (False, "You didn't choose the service")
        while True:
            if self.service not in self.services_ids: self.get_status_services(); time.sleep(1)
            request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':'multipart/form-data; boundary=----WebKitFormBoundary0nU8PjANC8BhQgjZ', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary0nU8PjANC8BhQgjZ\r\nContent-Disposition: form-data; name="{self.video_key}"\r\n\r\n{self.url}\r\n------WebKitFormBoundary0nU8PjANC8BhQgjZ--\r\n')
            try: self.video_info = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
            except: time.sleep(3); continue
            if 'Session expired. Please re-login' in self.video_info:
                print('⌛Session expired. Logging in again...')
                self.send_captcha()
                return
            elif 'service is currently not working' in self.video_info:
                return (True, '📡Service is currently unavailable, please try again later.')
            elif """onsubmit="showHideElements""" in self.video_info:
                self.video_info = [self.video_info.split('" name="')[1].split('"')[0],self.video_info.split('value="')[1].split('"')[0]]
                return (True, request.text)
            elif 'Checking Timer...' in self.video_info:
                try: 
                    t=int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                    zefoy = int(re.findall(r'ltm=(\d*);', self.video_info)[0])
                except: 
                    return (False,)
                if zefoy==0:self.find_video()
                elif zefoy >= 1000:
                    print('\033[31m🚨IP BLOCKED')
                _=time.time()
                while time.time()-2<_+zefoy:
                    t-=1
                    print('\033[31m</>🚀Please wait\033[1;32m{0}\033[31m '.format(t)+'giây\033[1;32m',end='\r')
                    time.sleep(1)
                continue
            elif 'Too many requests. Please slow' in self.video_info:
                time.sleep(3)
            else:
                print(self.video_info)

    def use_service(self):
        if self.find_video()[0] is False:
            return False
        self.token = "".join(random.choices(ascii_letters+digits, k=16))
        request = self.session.post(f'{self.base_url}{self.services_ids[self.service]}', headers={'content-type':f'multipart/form-data; boundary=----WebKitFormBoundary{self.token}', 'user-agent':self.headers['user-agent'], 'origin':'https://zefoy.com'}, data=f'------WebKitFormBoundary{self.token}\r\nContent-Disposition: form-data; name="{self.video_info[0]}"\r\n\r\n{self.video_info[1]}\r\n------WebKitFormBoundary{self.token}--\r\n')
        try:
            res = base64.b64decode(unquote(request.text.encode()[::-1])).decode()
        except:
            time.sleep(3)
            return ""
        if 'Session expired. Please re-login' in res:
            print('\033[31m⌛Session expired. Logging back in.')
            self.send_captcha()
            return ""
        elif 'Too many requests. Please slow' in res:
            time.sleep(3)
        elif 'service is currently not working' in res:
            return ('\033[31m🚨Service is currently unavailable, please try again later')
        else:
            print(res.split("sans-serif;text-align:center;color:green;'>")[1].split("</")[0])

    def get_video_info(self):
        request = self.session.get(f'https://tiktok.livecounts.io/video/stats/{urlparse(self.url).path.rpartition("/")[2]}',headers={'authority':'tiktok.livecounts.io','origin':'https://livecounts.io','user-agent':self.headers['user-agent']}).json()
        if 'viewCount' in request:
            return request
        else:
            return {'viewCount':0, 'likeCount':0,'commentCount':0,'shareCount':0,'favoritesCount':0,'followersCount':0}

    def get_video_id(self, url_ = None, set_url=True):
        if url_ is None:
            url_ = self.url
        if url_[-1] == '/':
            url_ = url_[:-1]
        url = urlparse(url_).path.rpartition('/')[2]
        if url.isdigit():
            self.url = url_
            return url_
        request = requests.get(f'https://api.tokcount.com/?type=videoID&username=https://vm.tiktok.com/{url}',headers={'origin': 'https://tokcount.com','authority': 'api.tokcount.com','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'})
        if request.text == '':
            print('\033[31m🚨Invalid video link')
            return False
        else:
            json_ = request.json()
        if 'author' not in json_:
            print(f'\033[31m{self.url} | ❌Invalid video link')
            return False
        if set_url:
            self.url = f'https://www.tiktok.com/@{json_["author"]}/video/{json_["id"]}'
            print(f'Formated video url --> {self.url}')
        return request.text

    def check_config(self):
        while True:
            try: 
                last_url = self.url
                if last_url != self.url:
                    self.get_video_id()
            except Exception as e:
                print(e)
            time.sleep(4)

    def update_name(self):
        while True:
            try:
                ctypes.windll.kernel32.SetConsoleTitleA(self.text.encode())
                video_info = self.get_video_info()
                self.text = f"Views: {video_info['viewCount']} | Hearts: {video_info['likeCount']} | Comment: {video_info['commentCount']} | Favorites: {video_info['favoritesCount']} | Followers: {video_info['followersCount']}"
            except:
                pass
            time.sleep(5)

    def select_service(self):
        while True:
            trang = "\033[1;37m"
            xanh_la = "\033[1;32m"
            xanh_duong = "\033[1;34m"
            do = "\033[1;31m"
            vang = "\033[1;33m"
            tim = "\033[1;35m"
            self.get_table()
            print(f"{xanh_la}Enter number\033[1;37m:", end=' ')
            service_id = input()
            if service_id.isdigit():
                service_id = int(service_id)
                if service_id in range(1, len(self.services) + 1):
                    services_list = list(self.services.keys())
                    self.service = services_list[service_id - 1]
                    break
                else:
                    print(f"{do}👀Reading and Entering Numbers Is Also Wrong.")
            else:
                print(f"{do}👀Reading and Entering Numbers Is Also Wrong.")

    def run(self):
        self.select_service()
        while True:
            trang = "\033[1;37m"
            xanh_la = "\033[1;32m"
            xanh_duong = "\033[1;34m"
            do = "\033[1;31m"
            vang = "\033[1;33m"
            tim = "\033[1;35m"
            try:
                if 'Service is currently not working, try again later' in str(self.use_service()):
                    print(f'{do}[\033[1;33mService is currently unavailable, please try again later.')
                    time.sleep(5)
            except Exception as e:
                print(f'\033[1;31m🚨UNEXPECTED ERROR | TRY AGAIN LATER | {e}')
                time.sleep(10)
	
if __name__ == "__main__":

    Z = Zefoy()
    threading.Thread(target=Z.check_config).start()
    threading.Thread(target=Z.update_name).start()
    Z.send_captcha()
    Z.run()
