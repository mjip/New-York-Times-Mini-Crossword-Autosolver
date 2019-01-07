#!/usr/bin/python3

import os
import sys
import urllib.request
import zipfile

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class CrosswordAI:
	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1024x1400")

		if not os.path.isfile('chromedriver'):
			zipresp = urllib.request.urlopen('https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip')
			with open('chromedriver_linux64.zip', 'wb') as tempzip:
				tempzip.write(zipresp.read())

			with zipfile.ZipFile('chromedriver_linux64.zip') as zip_ref:
				zip_ref.extractall()
		os.chmod('chromedriver', 0o755)
	
		chrome_driver = os.path.join(os.getcwd(), 'chromedriver')

		self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
		self.across_clues = {}
		self.down_clues = {}

	def start_game(self):
		self.driver.get('https://www.nytimes.com/crosswords/game/mini')
		elem = self.driver.find_element_by_tag_name('body')
		elem.send_keys(Keys.RETURN)

	def extract_clues(self):
		elem = self.driver.find_elements_by_class_name('ClueList-wrapper--3m-kd')
		for clue in elem:
			#self.clues.append(clue.text.split('\n'))
			clue_parts = clue.text.split('\n')
			if clue_parts[0] == "ACROSS":
				for i in range(1, len(clue_parts), 2):
					self.across_clues[int(clue_parts[i])] = clue_parts[i+1]
			elif clue_parts[0] == "DOWN":
				for i in range(1, len(clue_parts), 2):
					self.down_clues[int(clue_parts[i])] = clue_parts[i+1]
		
			print(self.across_clues)
			print(self.down_clues)


	def end_game(self):
		self.driver.get_screenshot_as_file('ai-mini.png')
		self.driver.close()


if __name__ == '__main__' :
	'''
	I wanted it to replicate human playing of the game as closely as possible.
	The clues are viewable in the page source without starting the game, and the words
	could have been brute forced, but I choose instead to start the game timer before
	extracting clues and to look up the clues to find possible relevant words.
	'''
	ai = CrosswordAI()
	ai.start_game()
	ai.extract_clues()
	ai.end_game()

