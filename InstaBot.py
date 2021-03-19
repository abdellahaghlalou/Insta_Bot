import instaloader
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random
 
# Login Credentials
username = input('Enter your Username ')
password = input('Enter your Password ')
url = 'https://instagram.com/'

def getfollowees(username,password):
	bot = instaloader.Instaloader()
	profile = instaloader.Profile.from_username(bot.context, username)
	bot.login(user=username,passwd=password)
	followees = [follower.username for follower in profile.get_followees()]
	return followees
def path():
	global chrome
	 
	# starts a new chrome session 
	chrome = webdriver.Chrome() # Add path if required

def url_name(url): 
  chrome.get(url)
   
  # adjust sleep if you want
  time.sleep(4)

def login(username, your_password):
	log_but = chrome.find_element_by_class_name("L3NKy") 
	time.sleep(2)
	log_but.click()
	time.sleep(4)
	 
	# finds the username box 
	usern = chrome.find_element_by_name("username")
	 
	# sends the entered username 
	usern.send_keys(username)
 
	# finds the password box 
	passw = chrome.find_element_by_name("password")
 
	# sends the entered password 
	passw.send_keys(your_password)
	 
	# press enter after sending password
	passw.send_keys(Keys.RETURN) 
	time.sleep(5.5)
	 
	# Finding Not Now button
	notk = chrome.find_element_by_class_name("yWX7d")  
	notk.click()
	time.sleep(3)

def send_message():
   
	# Find message button
	
	message = chrome.find_element_by_class_name("vBF20 _1OSdk")
	
	message = chrome.find_element_by_class_name('_862NM ')

	message.click()
	time.sleep(2)
	chrome.find_element_by_class_name('HoLwm ').click()
	time.sleep(1)
	l = ["https://gaingame.me/PS5/","heeeey we gift you a playtation 5 simulation ,enjoooy","there is a gaveway coming sooon"]
	for elt in l:
		mbox = chrome.find_element_by_tag_name('textarea')
		mbox.send_keys(elt)
		mbox.send_keys(Keys.RETURN)
		time.sleep(1.2)
		

path()
time.sleep(1)
followers=followers=['sn3perxpl','chensa_m_07','qt.jxey','fcdaniele99731','yt_duoz','gope.solis','midy_si','xorp.co','mr._prince7','xking25_boiyt','elfeo.sfwebo','simranramgrahia123','kunfessonyt','panxhofn_','fortnite_sweat_07','anthonypowell900','so.wavvvvy_keyashia','bryce___1k','swxtchrr_','dplayz246','suarexalejandro','getready112233','dubz.clannn','pa.olo5680','7v.jaxon','phenomenaaaaaaa']
for elt in followers:
	url_name(url+elt)
	login(username, password)
	send_message()


