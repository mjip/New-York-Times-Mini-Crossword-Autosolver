#!/usr/bin/python3

import os
import sys
import urllib.request
import zipfile

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

class CrosswordAI:
	def __init__(self):
		options = Options()
		options.headless = True
		self.driver = webdriver.Firefox(options=options)

		self.across_clues = {}
		self.across_letters = {}

		self.down_clues = {}
		self.down_letters = {}

	def start_game(self):
		self.driver.get('https://www.nytimes.com/crosswords/game/mini')
		elem = self.driver.find_element_by_tag_name('body')
		elem.send_keys(Keys.RETURN)

	def extract_clues(self):
		elem = self.driver.find_elements_by_class_name('ClueList-wrapper--3m-kd')
		for clue in elem:
			clue_parts = clue.text.split('\n')
			if clue_parts[0] == "ACROSS":
				for i in range(1, len(clue_parts), 2):
					self.across_clues[int(clue_parts[i])] = clue_parts[i+1]
			elif clue_parts[0] == "DOWN":
				for i in range(1, len(clue_parts), 2):
					self.down_clues[int(clue_parts[i])] = clue_parts[i+1]

	def end_game(self):
		self.driver.get_screenshot_as_file('ai-mini.png')
		print(self.across_clues)
		self.driver.close()
		print(self.down_clues)


if __name__ == '__main__' :
	'''
	I wanted it to replicate human playing of the game as closely as possible.
	The clues are viewable in the page source without starting the game, and the words
	could have been brute forced, but I choose instead to start the game timer before
	extracting clues and to look up the clues to find possible relevant words.
	'''
	ai = CrosswordAI()
	ai.start_game()

	''' 
	You can extract clues by pulling out the elements under the 'ClueList-wrapper--3m-kd' class name
	'''
	ai.extract_clues()

	'''
	Once we have the clues, you can cycle through the clues by hitting tab (typing out the guess is optional)
	'''
	ai.
	ai.end_game()

