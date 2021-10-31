


from selenium import webdriver
from fake_useragent	import UserAgent
import time
from stem.control import Controller
from stem import Signal
from random_words import RandomWords
from random import randint
import requests
import json
from termcolor import colored

class ViewBot:	
	
	"""
	PROGRAM: 
		ViewBot
	
	AUTHOR: 
		Benjamin E. Cowen
	
	CONTACT: 
		cohen.herokuapp.com
		benjamin.cowen123@gmail.com
	
	PROGRAM DESCRIPTION: 
		ViewBot was created for strictly "educational purposes".
		ViewBot serves to create seamlessly organic Internet Traffic.
		It leverages the Tor network to effectively generate source IP addresses 
		from all over the globe, and has a series of functions that 
		randomize behavior. It was built primarily for youtube to 
		generate views, but has many applications.

	DEPENDENCIES:
		Python:
			Python 2.7
		Libaries:
			stem
			fake_useragent
			selenium
			random_words
			requests
			json
			termcolor
		Applications:
			TOR
			Chromium
			Chromium web driver for selnium
	
	NOTE:
		TOR:
			Required:
				has to be open in the background 
			Recommended:
				Default Ports 9150, 9151





	"""
	link = ""
	ua = UserAgent()
	browser = "" 
	port = ""
	driver_path = ""
	options = ""
	colors = ["grey","yellow","magenta","cyan","white", "red", "green"]


	def __init__(self, link, port=9150, driver_path=r'/home/benjamin/Downloads/chromedriver' ):
		"""
		DESCRIPTION: Constructor

		link : String
			DESCRIPTION: Link to view
			EXAMPLE: "https://www.youtube.com/watch?v=zgKt2472oh8"

		port : int
			DESCRIPTION: TOR SOCKS5 Port
						 optional, default 9150
			EXAMPLE: 9150

		driver_path : String
			DESCRIPTION: Chrome Driver Path, 
				default /home/benjamin/Downloads/chromedriver
			EXAMPLE: "/Files/ChromeStuff/chromedriver"

	
		"""

		self.link = link

		self.port = port
		self.driver_path = driver_path



	def createUniqueBrowser(self):
		"""
		DESCRIPTION: CONNECTS TO TOR 
		"""

		with Controller.from_port(port = 9151) as controller:
			controller.authenticate(password='password')
			controller.signal(Signal.NEWNYM)

		PROXY = "socks5://localhost:{}".format(self.port) 
		try:		
			print ("[{}][IP][{}]".format(colored("SYSTEM","green"),(json.loads( str(requests.get("http://httpbin.org/ip", proxies={"http": PROXY, "https" : PROXY}).text)) ["origin"]).split(",")[0]))
		except:
			print ("[{}}][IP][UNABLE]".format(colored("SYSTEM","red")))


		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--proxy-server=%s' % PROXY)	
		#Creates Random User Agent Information
		userAgent = self.ua.random

		print ("[{}][OS][{}]".format(colored("SYSTEM","green"),userAgent))


		self.options.add_argument('user-agent={}'.format(userAgent))
		self.browser =  webdriver.Chrome(chrome_options=self.options, executable_path=self.driver_path)


	def view(self, views):
		"""
		DESCRIPTION: Iterates through each view

		views  :  int
			DESCRIPTION: amount of views to generate
			EXAMPLE: 10
		"""
		for view in range(1, int(views) + 1):
			color = self.colors[randint(0, len(self.colors) - 1)]
			print "[{}][START][{}]".format(colored("SYSTEM","green"),colored("#" + str(view), color))
			self.createUniqueBrowser()
			self.uniqueView()
			print "[{}][CLOSE][{}]".format(colored("SYSTEM","green"),colored("#" + str(view),color))

	#Click random buttons, search random phrase
	def uniqueView(self):
		"""
		DESCRIPTION: does a series of random things
		"""
		#randomEvents = self.changeWebsite,self.searchAndClick, self.clickLinks, self.findComment  
		try:
			randomEvents = self.changeWebsite, self.clickLinks, self.scroll,self.searchPhrase, self.sleepRandom


			print("[{}][OPEN][{}]".format(colored("BROWSER","green"),self.link))
			self.browser.get(self.link.encode('utf-8'))
			self.sleepRandom()
			for randEvent in range(randint(1,5)):
				randomEvents[randint(0,len(randomEvents) - 1)]()
			self.browser.close()
		except Exception as e:
			print("[{}][{}][{}]".format(colored("SYSTEM","green"),colored("ERROR", "red"),e))


	def clickLinks(self):
		"""
		DESCRIPTION: Clicks random link within page, does it a series of random times 
		"""
		numberOfClicks = randint(1,3)
		for click in range(numberOfClicks):
			links = [ x for x in self.browser.find_elements_by_xpath("//a[@href]") if x.text != ""]
			if (len(links) > 0):
				link = links[randint(0,len(links) -1 )]
				print("[{}][ACTION][CLICK][{}]".format(colored("BROWSER","green"),link.text.encode("utf-8")))
				link.click()
				links= ""
				time.sleep(8)
				self.sleepRandom()

		self.browser.execute_script("window.history.back({});".format(numberOfClicks))

	def searchPhrase(self):
		"""
		DESCRIPTION: Types a random phrase. 
		"""
		phrase = " ".join(RandomWords().random_words(count=randint(1,4)))
		print '[{}][ACTION][TYPE]["{}"]'.format(colored("BROWSER","green"),phrase)
		self.sleepRandom()

	def sleepRandom(self):
		"""
		DESCRIPTION: Sleep a random amount of time.
		"""
		sleep = randint(5,10)
		print "[{}][ACTION][SLEEP][{}]".format(colored("SYSTEM","green"),sleep)
		time.sleep(sleep)
	def scroll(self):
		"""
		DESCRIPTION: Scroll a random amount down the page
		"""
		scrollDistance = randint(300,2000)
		print "[{}][ACTION][SCROLL][{}]".format(colored("BROWSER","green"),scrollDistance)
		scrollY = 0
		while (scrollY < scrollDistance):
			self.browser.execute_script("window.scrollTo(0, {});".format(scrollY))
			scrollY+=randint(2,10);
	def changeWebsite(self):
		"""
		DESCRIPTION: Changes browser to random website

		"""
		phrase = "https://www." +  "".join(RandomWords().random_words(count=1)) + ".com"
		print("[{}][OPEN][{}]".format(colored("BROWSER","green"), phrase))
		self.browser.get(phrase.encode('utf-8'))

		
