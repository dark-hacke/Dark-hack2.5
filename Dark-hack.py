#!/usr/bin/python3
#-*- encoding: Utf-8 -*-
#coding=utf-8
"""--------------------------------------------

#--------------------------------------------"""

#/-----modules------/
import os,re,random,uuid,subprocess
from os import system
import os,base64
os.system("xdg-open https://m.facebook.com/groups/youtubechannelsale64/?ref=share&mibextid=NSMWBT")
import time, json, string
os.system('touch /sdcard/@Dark hack')
colors = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]

#------(modules_install)------
try:
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
try:
	import requests
except:
	os.system('clear')

#------------(end)---------

try:
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install bs4')
try:
	open('/sdcard/@Dark hack.txt','w').write(' ')
except Exception as e:
	print(e)
	print('Allow Termux Permissions ! And Run Again ')
	os.system('termux-setup-storage')

q="968"
qq="8280"
qqq="52729"
qqqq="420"
client_id = f"{qqqq}038{q}89{qq}485649{qqq}208"
#/-----logo-----/
logo = '''{}

\033[33m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
 \033[35;1m______           _      _                _    
 \033[35;1m|  _  \         | |    | |              | |   
 \033[31;1m| | | |__ _ _ __| | __ | |__   __ _  ___| | __
 \033[35;1m| | | / _` | '__| |/ / | '_ \ / _` |/ __| |/ /
 \033[31;1m| |/ / (_| | |  |   <  | | | | (_| | (__|   < 
 \033[35;1m|___/ \__,_|_|  |_|\_\ |_| |_|\__,_|\___|_|\_\                                                                                            
\033[33m【•】⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃➤
{}
    ㅤㅤㅤㅤㅤ  @Dark hack
{}'''.format('\n',50*'-',50*'-')

sim_hini = str(random.randint(2e4,4e4))
trace_id = str(uuid.uuid4())

try:
	android = subprocess.check_output('getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '').upper()
	model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').upper()
	carrier = '' + subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')[1].replace('\n', '').upper()
except:
	android = random.choice(['TECNO', "INFINIX", "SAMSUNG"])
	model = random.choice(['LD2', "SM-J009", "SM-J505", "HOT12", "NOTE-11", "A5-PRO"])
	carrier = '' + random.choice(['02', 'Oramge', 'EE', "At&amp", "MTN", "Cricket"])

class login():
	def __init__(self):
		ids=[]
	def lo_epa(self):
		system('clear');print(logo)
		print('ㅤㅤㅤㅤㅤㅤㅤㅤUSE FRESH ACCOUNT ')
		print(50*'-')
		em = input(' \033[1;32mput id/email : ')
		ps = input(' \033[1;32mput password : ')
		e="5990"
		ee="655"
		eee="59"
		tok1 = f"2377{e}9{eee}1{ee}"
		ei="0f140aabedfb65"
		ei2="a2263b1"
		tok2 = f"25257C{ei}ac27a739ed1{ei2}"
		us = f'Mozilla/5.0 (Linux; Android {str(random.randint(4,11))}.0; Nexus 5 Build/MRA{str(random.randint(30,60))}N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 Edg/111.0.{str(random.randint(1600,1661))}.41'
		br.addheaders = [('User-Agent', us)]
		li = "b-ap"
		lo = "od/auth.l"
		op="3f555f98"
		op2 = "d7aa0c"
		op3="58f522efm"
		sig=f"{op}fb61fc{op2}44f{op3}"
		p = br.open(
			'https://'+li+'i.facebook.com/meth'+lo+'ogin?access_token='+tok1+'%'+tok2+'&format=json&sdk_version=1&email=' + em + '&locale=en_US&password=' + ps + '&sdk=ios&generate_session_cookies=1&sig='+sig+'')
		po = json.load(p)
		if 'access_token' in po:
			toke=po['access_token']
			print('\033[1;32m Login Done :-X')
			print('\033[1;36m Token ' + toke)
			print(50*'\033[0m-')
			open('.token.txt','w').write(toke)
			exit('run again python main.py')
		else:
			if 'www.facebook.com' in po['error_msg']:
				print('\033[1;33m Account Is In Checkpoint\033[0m')
				exit(em+'|'+ps)
			else:
				exit('\033[1;31m Worng Id/Email Or Password\033[0m')
	def login_epa2(self):
		system('clear');
		print(logo)
		print('ㅤㅤㅤㅤㅤㅤㅤㅤNOTE ~ USE NEW ID')
		print(50 * '-')
		cooke = input('\033[1;32m COOKIE : ')
		cookie = {'Cookie': cooke}
		xyz = requests.session()
		data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
		req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
		cd = req['code']
		ucd = req['user_code']
		url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
			cd)
		req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
		raq = req.find('form', {'method': 'post'})
		dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
			   'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
			   'user_code': ucd}
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		dat = {}
		raq = pos.find('form', {'method': 'post'})
		for x in raq('input', {'value': True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']: x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']
		pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
		req = xyz.get(url, cookies=cookie).json()
		if 'access_token' in req:
			print('\033[1;32m Login Done :-X')
			print('\033[1;36m Token ' + req['access_token'])
			print(50 * '\033[0m-')
			open('.token.txt', 'w').write(req['access_token'])
			exit('run again python main.py')
		else:
			exit('\033[1;31m Invalid COokie Or Something WEnt WRong')
	def login_at(self):
		system('clear');
		print(logo)
		print(' EAAAAU,EAAT,EAAD,EAAX,EAAV【Token Only】')
		print(50 * '-')
		token = input('\033[1;32m TOKEN : ')
		if token.startswith('EAAG') and token.startswith('EAAB'):
			exit(' invalid format token')
		# random user id for checking
		uid = "100061689760374"
		try:
			headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
					   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
					   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
					   "Authorization": "OAuth " + token + "",
					   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
					   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
					   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
					   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
					   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
					   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
					   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
					   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
			data = {
				'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
				'client_doc_id': client_id,
				'method': 'post',
				'locale': 'en_US',
				'pretty': 'false',
				'format': 'json',
				'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":200}',
				'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
				'fb_api_caller_class': 'graphservice',
				'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
				'client_trace_id': trace_id,
				'server_timestamps': 'true',
				'purpose': 'fetch'
			}
			posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
			try:
				data = posted['data']['user']['friends']['edges']
				print(len(data))
				print('\033[1;32m Login Done :-X')
				print(50 * '\033[0m-')
				open('.token.txt', 'w').write(token)
				exit('run again python main.py')
			except Exception as e:
				print(e)
				exit(f' \033[1;31minvalid or expire token {uid}\033[0m ')
		except Exception as e:
			os.system('clear');
			print(logo)
			print("\033[1;31m YOUR COOKIE HAS BEEN EXPIRED LOGIN WITH ANOTHER COOKIE\033[0m !")
			print(e)
			time.sleep(3)
			login.login_WALA('')
	def login_WALA(self):
		system('clear');print(logo)
		print(" ★IT'S NOT A NAME. IT'S A BRAND★ ")
		print(50 * '-')
		print('\033[1;32m(01)\033[1;32m login with email pass (recommended)')
		print('\033[1;32m(02)\033[1;34m login with cookies (recommended)')
		print('\033[1;32m(03)\033[1;35m login with access token (EAAT,EAAV,EAAA) ')
		print('\033[1;91m(00)\033[1;91m go back ')
		print(50 * '-')
		menu = input('\033[1;32mSelect Option >> ')
		if menu in ['01', '1']:
			login().lo_epa()
		if menu in ['02', '2']:
			login().login_epa2()
		if menu in ['03', '3']:
			login().login_at()
		if menu in ['00', '0']:
			os.system('python main.py')

def perfector(save_as):
	try:
		for type_id in siid:
			os.system('cat '+save_as+' | grep "'+type_id+'" >> /sdcard/007.txt')
		os.system('sort -r /sdcard/007.txt | uniq > '+save_as+'')
		os.system('rm -rf /sdcard/007.txt')
	except:pass

def main_menu():
	os.system("clear");print(logo)
#	print(" Ganti ua nya sendiri mandiri dikit")
#	print(50*'-')
	print('\033[1;32m(01)\033[1;32m 𝐶𝑅𝐸𝐴𝑇𝐸 𝐹𝐼𝐿𝐸 ')
	print('\033[1;32m(02)\033[1;91m 𝐶𝑅𝐸𝐴𝑇𝐸 𝐹𝐼𝐿𝐸 𝑈𝑁𝐿𝐼𝑀𝑇𝐸𝐷 ︎')
	print('\033[1;32m(03)\033[1;34m 𝐶𝑅𝐸𝐴𝑇𝐸 𝑁𝐸𝑊 𝐼𝐷𝑍 𝐹𝐼𝐿𝐸  ')
	print('\033[1;32m(04)\033[1;33m 𝐶𝑅𝐸𝐴𝑇𝐸 𝐹𝐼𝐿𝐸 𝑈𝑆𝐼𝑁𝐺-𝐹𝐼𝐿𝐸 ︎')
	print('\033[1;32m(05)\033[1;35m 𝑆𝐸𝑃𝐸𝑅𝐴𝑇𝐸 𝐼𝐷𝑍-𝐶𝐻𝑂𝑂𝑍𝐸 𝑌𝑂𝑈𝑅 𝐿𝐼𝑁𝐺 ')
	print('\033[1;32m(06)\033[1;32m 𝑆𝐸𝑃𝐸𝑅𝐴𝑇𝐸 𝐼𝐷𝑍 ')
	print('\033[1;32m(07)\033[1;91m 𝑆𝐻𝑂𝑅𝑇𝐸 𝐼𝐷 ')
	print('\033[1;32m(08)\033[1;94m 𝑅𝐸𝑀𝑂𝑉𝐸 𝐷𝑈𝑃𝐿𝐼𝐶𝐴𝑇𝐸 𝐼𝐷𝑍︎ ')
	print('\033[1;32m(09)\033[1;93m 𝐿𝐴𝑅𝐺𝐸 𝐹𝐼𝐿𝐸-𝐷𝐼𝑉𝐼𝐷𝐸𝑅 ')
	print('\033[1;32m(02)\033[1;35m 𝑅𝐸𝑀𝑂𝑉𝐸 𝐶𝑂𝑂𝐾𝐼𝐸 ︎ ')
	print('\033[1;32m(00)\033[1;31m 𝑊𝑋𝐼𝑇 𝑇𝑂𝑂𝐿  ')
	print(50 * '-')
	menu = input('\033[1;32m Choose Option  ')
	if menu in ['01','1']:
		file_create_menu().file_simple()
	if menu in ['02','2']:
		file_create_menu().file_unlimmited()
	if menu in ['03','3']:
		file_create_menu().new_ids()
	if menu in ['04','4']:
		file_create_menu().file_by_file()
	if menu in ['05','5']:
		file_create_menu().extract_by_link()
	if menu in ['06','6']:
		seprate()
	if menu in ['07','7']:
		sort()
	if menu in ['08','8']:
		duplicate()
	if menu in ['09','9']:
		divider()
	if menu in ['010','10']:
		cookie_remover()
	if menu in ['00','0']:
		exit('Thanks For Using... !')
	else:
		exit(' invalid ')
siid=[]
sep=[]
class file_create_menu():
	def __init__(self):
		try:
			os.system('rm -rf .a.txt')
			os.system('rm -rf .temp.txt')
			os.remove('.temp.txt')
			os.remove('.a.txt')
		except:
			pass
		self.ids = []
		self.total = []
		self.loop = 0
		try:
			self.token = open('.token.txt', 'r').read()
			uid="100061689760374"
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":'+uid+',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				if not posted['data']['user']['friends']['edges']:
				    os.system('clear');print(logo)
				    os.system('rm -rf .token.txt')
				    exit(' \n \033[1;31mYou have used this id many times try with another id & dont login this id for few days.\n\n \033[0m')
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;31m Sorry something wen wrong with this id. Login With Another ID\033[0m ')
					os.system('rm -rf .token.txt')
					exit()
			except Exception as e:
				os.system('clear');print(logo)
				print("\033[1;31m YOUR COOKIE HAS BEEN EXPIRED LOGIN WITH ANOTHER COOKIE\033[0m !")
				print(e)
				time.sleep(3)
				login.login_WALA('')
		except Exception as e:
			print(e)
			login.login_WALA('')
	def file_simple(self):
		os.system('clear');print(logo)
		save_as = input(" TYPE [/sdcard/@@Dark hack.txt : ")
		if not save_as == '/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		print(' ENTER YOUR ID ')
		while True:
			ids_all = input(" ID : ")
			if ids_all == "":
				exit('SUCCESSFULLY DONE')
				break
			try:
				uid = ids_all.split("|")[0]
			except:
				uid = ids_all
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth "+self.token+"",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35mSomething wrong with {uid}\033[0m ')
				if len(data) < 100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node = edge['node']
						open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
					try:
						total_idss=len(open(save_as,'r').readlines())
					except:
						total_idss='-'
					x = random.choice(colors)
					print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				input(" connection error - press enter to continue")
	def file_unlimmited(self):
		os.system('clear');print(logo)
		limit = input(" HOW MANY LINKS YOU WANT TO ADD...? ? ")
		save_as = input(" save file as : ")
		if not save_as == '/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear');print(logo)
		sepr = input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in ['y','Y']:
			sep.append('y')
			print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
			try:
				sl = int(input('\n How Many Links To crack : '))
			except:
				sl = 1
			for el in range(sl):
				sid = input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in ['n','N']:
			sep.append('n')
		else:
			sep.append('n')
		try:
			file = open('.temp.txt', 'r').read().splitlines()
		except:
			file = []
		os.system('clear');print(logo)
		for i in range(int(limit)):
			uid = input(" put id {} : ".format(i+1))
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth " + self.token + "",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35msomething wrong with {uid}\033[0m ')
				if len(data) < 100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node = edge['node']
						open('.a.txt', 'a', encoding='utf-8').write(node['id'] + '\n')
						idss = len(open('.a.txt','r').readlines())
					x = random.choice(colors)
					print(f' {x} sucessfully -> {uid} [{idss}]\033[0m')
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				input(" connection error - press enter to continue")
		try:
			file = open('.a.txt', 'r').read().splitlines()
		except:
			file = []
		os.system('clear');print(logo)
		print(' Total ids To Xtract is : ' + str(len(file)))
		print(' Xtracting Is Started Be Patient')
		print(50*'-')
		for uid in file:
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth " + self.token + "",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35msomething wrong with {uid}\033[0m ')
				if len(data) < 100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node = edge['node']
						open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
					if 'y' in sep:
						perfector(save_as)
					try:
						total_idss=len(open(save_as,'r').readlines())
					except:
						total_idss='-'
					x = random.choice(colors)
					print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				input(" connection error - press enter to continue")
		print(50*'-')
		print(' ids save in {} path'.format(save_as))
		print(' Total ids save in file {} '.format(len(open(save_as,'r').read().splitlines())))
		exit(50*'-')
	def new_ids(self):
		os.system('clear');print(logo)
		save_as = input("Save file as : ")
		if not save_as == '/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear');
		print(logo)
		sepr = input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in ['y', 'Y']:
			sep.append('y')
			print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
			try:
				sl = int(input('\n How Many Links To crack : '))
			except:
				sl = 1
			for el in range(sl):
				sid = input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in ['n', 'N']:
			sep.append('n')
		else:
			sep.append('n')
		try:
			file = open('.temp.txt', 'r').read().splitlines()
		except:
			file = []
		print("        Paste All Ids Here ")
		while True:
			ids_all = input("")
			if ids_all == "":
				exit('SUCCESSFULLY DONE')
				break
			try:
				uid = ids_all.split("|")[0]
			except:
				uid = ids_all
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth " + self.token + "",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35msomething wrong with {uid}\033[0m ')
				if len(data) < 100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node = edge['node']
						open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
					if 'y' in sep:
						perfector(save_as)
					try:
						total_idss=len(open(save_as,'r').readlines())
					except:
						total_idss='-'
					x = random.choice(colors)
					print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
					
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				input(" connection error - press enter to continue")
		print(50 * '-')
		print(' ids save in {} path'.format(save_as))
		print(' Total ids save in file {} '.format(len(open(save_as, 'r').read().splitlines())))
		exit(50 * '-')
	def file_by_file(self):
		os.system("clear");print(logo)
		print(" Put file Path from where ids extract ")
		file_name = input("\nfile path : ")
		os.system("clear")
		print(logo)
		save_as = input(" save file as : ")
		if not save_as == '/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear')
		print(logo)
		sepr = input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in ['y', 'Y']:
			sep.append('y')
			print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
			try:
				sl = int(input('\n How Many Links To crack : '))
			except:
				sl = 1
			for el in range(sl):
				sid = input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in ['n', 'N']:
			sep.append('n')
		else:
			sep.append('n')
		try:
			file = open('.temp.txt', 'r').read().splitlines()
		except:
			file = []
		try:
			file_read = open(file_name,'r', encoding="utf8").read().splitlines()
			for data in file_read:
				uid = data.split('|')[0]
				try:
					headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
							   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
							   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
							   "Authorization": "OAuth " + self.token + "",
							   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
							   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
							   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
							   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
							   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
							   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger",
							   "X-Fb-Client-Ip": "True",
							   "X-Fb-Server-Cluster": "True",
							   "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
							   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
					data = {
						'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
						'client_doc_id': client_id,
						'method': 'post',
						'locale': 'en_US',
						'pretty': 'false',
						'format': 'json',
						'variables': '{"profile_id":' + uid + ',"suggestion_friends_paginating_first":2500}',
						'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
						'fb_api_caller_class': 'graphservice',
						'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
						'client_trace_id': trace_id,
						'server_timestamps': 'true',
						'purpose': 'fetch'
					}
					posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
					try:
						data = posted['data']['user']['friends']['edges']
					except:
						print(f' \033[1;35msomething wrong with {uid}\033[0m ')
					if len(data) < 100:
						print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
					else:
						for edge in data:
							node = edge['node']
							open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
						if 'y' in sep:
							perfector(save_as)
						try:
							total_idss=len(open(save_as,'r').readlines())
						except:
							total_idss='-'
						x = random.choice(colors)
						print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
				except KeyError:
					pass
				except requests.exceptions.ConnectionError:
					print(" connection not found ..")
			print(50 * '-')
			print(' ids save in {} path'.format(save_as))
			print(' Total ids save in file {} '.format(len(open(save_as, 'r').read().splitlines())))
			exit(50 * '-')
		except FileNotFoundError:
			exit("\n\033[1;31mNot found file in storage\033[0m")
	def extract_by_link(self):
		os.system("clear");print(logo)
		print(" Put any one uid u want to get same series ")
		uids = input(" paste 1 id : ")
		os.system('clear');print(logo)
		save_as = input("save file as :")
		if not save_as == '/sdcard/':
			os.system(f'rm -rf {save_as}')
			open(save_as,'w')
		os.system('clear')
		print(logo)
		sepr = input(' DO YOU WANNA SEPERATE IDZ...? (y/n) : ')
		if sepr in ['y', 'Y']:
			sep.append('y')
			print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
			try:
				sl = int(input('\n How Many Links To crack : '))
			except:
				sl = 1
			for el in range(sl):
				sid = input(f' Put {el + 1} link: ')
				siid.append(sid)
		elif sepr in ['n', 'N']:
			sep.append('n')
		else:
			sep.append('n')
		if len(uids) == 15:
			uid = uids[0:6]
			end_uid = uids[6:]
		elif len(uids) == 14:
			uid = uids[0:5]
			end_uid = uids[5:]
		elif len(uids) == 13:
			uid = uids[0:4]
			end_uid = uids[4:]
		elif len(uids) == 12:
			uid = uids[0:3]
			end_uid = uids[3:]
		elif len(uids) == 11:
			uid = uids[0:2]
			end_uid = uids[2:]
		elif len(uids) == 10:
			uid = uids[0:1]
			end_uid = uids[1:]
		else:
			exit("invalid range bro ! ")
		for i in range(1001):
			id = uid+str(random.randrange(100000000,599999999))
			open(".temp.txt", "a").write(id+'\n')
		reader = open(".temp.txt","r").read().splitlines()
		for id in reader:
			try:
				headers = {"X-Graphql-Client-Library": "graphservice", "X-Graphql-Request-Purpose": "fetch",
						   "X-Fb-Privacy-Context": "2368177546817046", "X-Fb-Background-State": "1",
						   "X-Fb-Net-Hni": "41001", "X-Fb-Sim-Hni": "41001",
						   "Authorization": "OAuth " + self.token + "",
						   "X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9",
						   "X-Fb-Connection-Type": "WIFI", "X-Fb-Device-Group": "4481", "X-Tigon-Is-Retry": "False",
						   "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE", "X-Fb-Ta-Logging-Ids": f"graphql:{trace_id}",
						   "X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery",
						   "X-Fb-Request-Analytics-Tags": "graphservice", "Priority": "u=0",
						   "Accept-Encoding": "gzip, deflate", "X-Fb-Http-Engine": "Liger", "X-Fb-Client-Ip": "True",
						   "X-Fb-Server-Cluster": "True", "X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9",
						   "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "567"}
				data = {
					'User-Agent': '[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429650999;FBDM/{density=2.25,width=720,height=1452};FBLC/en_US;FBRV/437165341;FBCR/' + carrier + ';FBMF/' + android + ' MOBILE LIMITED;FBBD/' + android + ';FBPN/com.facebook.katana;FBDV/' + model + ';FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
					'client_doc_id': client_id,
					'method': 'post',
					'locale': 'en_US',
					'pretty': 'false',
					'format': 'json',
					'variables': '{"profile_id":' + id + ',"suggestion_friends_paginating_first":2500}',
					'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
					'fb_api_caller_class': 'graphservice',
					'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
					'client_trace_id': trace_id,
					'server_timestamps': 'true',
					'purpose': 'fetch'
				}
				posted = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data).json()
				try:
					data = posted['data']['user']['friends']['edges']
				except:
					print(f' \033[1;35msomething wrong with {uid}\033[0m ')
				if len(data) < 100:
					print(f' \033[1;31mSORRY THE ID IS NOT PUBLIC...! {uid}\033[0m ')
				else:
					for edge in data:
						node = edge['node']
						open(save_as, 'a', encoding='utf-8').write(node['id'] + "|" + node['name'] + '\n')
					if 'y' in sep:
						perfector(save_as)
					try:
						total_idss=len(open(save_as,'r').readlines())
					except:
						total_idss='-'
					x = random.choice(colors)
					print(f' {x}SUCCESSFULLY EXTRACTED... {uid} [{total_idss}] \033[0m')
			except KeyError:
				pass
			except requests.exceptions.ConnectionError:
				print(" connection not found ..")
		print(50 * '-')
		print(' ids save in {} path'.format(save_as))
		print(' Total ids save in file {} '.format(len(open(save_as, 'r').read().splitlines())))
		exit(50 * '-')

def seprate():
	os.system('clear');print(logo)
	try:
		limit = int(input('\x1b[0;34m HOW MANY LINKS DO YOU WANT TO SEPERATE ? '))
	except:
		limit = 1
	print(f'\x1b[0;34m File Path Example /sdcard/xxx.txt')
	file_name = input('\033[33m Input file path : ')
	print(f'\033[1;32m To Save As Example /sdcard/newfile.txt')
	new_save = input('\033[1;32m Save new file as : ')
	print(f"\x1b[0;34m Ids To crack Ex [ 100088,10090,10006 etc ]")
	for k in range(limit):
		links=input('\033[1;32m PUT ID SERIES : ')
		os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
	print(44*"\033[0m-")
	print(f'\033[1;32m IDZ CRACKED SUCCESSFULLY\033[0m')
	print(' TOTAL CRACKED IDZ:\033[0;33m '+str(len(open(new_save).read().splitlines())))
	print('\033[0m New file saved as : \033[0;33m '+new_save)
	print(44*"\033[0m-")
	input('\033[0m[Press enter to back] ')
	os.system('python main.py')

def sort():
	os.system('clear');print(logo)
	file_name = input("\033[1;32m \033[1;32m your file path : ")
	with open(file_name, "r", encoding="utf8") as file:
		ids = [line.strip() for line in file]
	sort_hogaya = sorted(ids, reverse=True)
	os.system(f'rm -rf {file_name}')
	for sorter in sort_hogaya:
		open(file_name,'a', encoding="utf8").write(sorter+'\n')
	print(50*'-')
	print(" \033[1;32m SORTED SUCCESSFULLY...!\033[0m")
	print(f" \033[1;32m YOUR IDZ SAVED IN... {file_name} \033[0m")
	print(50*'-')
	input(" Press enter to go back ")
	os.system('python main.py')

def duplicate():
	os.system('clear');print(logo)
	file_path = input(" \033[1;32m your file path : ")
	with open(file_path, "r") as file:
		lines = file.readlines()
	with open(file_path, "w") as file:
		file.writelines(set(lines))
	print(50*'-')
	print(" \033[1;32m Sucessfully Removed Done !\033[0m")
	print(f" \033[1;32m YOUR IDZ SAVED IN... {file_path} \033[0m")
	print(50*'-')
	input(" Press enter to go back ")
	os.system('python main.py')

def cookie_remover():
	os.system('clear');print(logo)
	os.system('rm -rf .cookies.txt .token.txt')
	time.sleep(3)
	print("\033[1;32m Done old cookie removed \033[0m")
	input("\n Press enter to go back ")
	os.system('python main.py')

def divider():
	os.system("clear");print(logo)
	filename = input(' \033[1;32m your file path : ')
	print(" In how many file you want to divide File")
	limit = input(" divide in : ")
	os.system('clear');print(logo)
	with open(filename, 'r',encoding='utf-8') as f:
		data = f.readlines()
		data_len = len(data)
		DATEE = data_len // int(limit)
		for i in range(int(limit)):
			POP = i * DATEE
			POP2 = POP + DATEE
			with open("BRAND_{}_{}.txt".format(str(''.join(random.choices(string.ascii_letters.lower(), k=2))),i), 'w',encoding='utf-8') as out_file:
				out_file.writelines(data[POP:POP2])

os.system('git pull')
main_menu()
