# whoopsie.py : 
# This file will 'accidentally' delete a specified file or directory after replacing the
# contents with a string of random bits of size equal to the original file's or files' content.
# Author : Jo
# License : Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

import re, sys, os, random
from argparse import ArgumentParser

prog = 'Whoopsie!'
version = 0.4
description = ''''Whoopsie' delete pontentially incriminating evidence
					-- just like the CIA!'''

whoops = re.compile(r'(?i)w+h+[o0]+p+s+[i!1]+[e3]s*')
nope = re.compile(r'(?i)(n+[o0]+(p+[e3]+ ?)?)+')
quit = re.compile(r'(?i)quit')

alphabet = list(map(chr, range(32, 127))) # ' ' to '~'
random.seed()

class Whoopsie(object):
	def __init__(self, target, k = 5, options = None):
		self.k = k
		self.options = options
		self.recursed = False

		if self.options['force']:
			self.__delete_silent(target = target)
		else:
			self.__delete_prompt(target = target)

	# Prompt user to confirm accidental intentions
	def __prompt(self, target):
		string = input('Whoopsie target file : {0}?\n[Whoopsie / Nope / Quit]\n'.format(target))

		if whoops.search(string):
			return True
		elif nope.search(string):
			return False
		elif quit.search(string):
			print('Quitting...')
			sys.exit(0)
		else:
			print('Input error: try again')
			return self.__prompt(target = target)

	# Accidentally delete with user prompt for every file and directory
	def __delete_prompt(self, target):
		# Prompt
		if self.__prompt(target): 	# Whoopsie
			# File
			if os.path.isfile(target):
				length = os.path.getsize(target)*4 # convert to word-size
				for i in range(1, self.k, 1):
					with open(target, 'w') as f:
						f.write(self.__unicode(length))

					if i % (k // 10) == 0:
						print('Whoopsie {0} of {1} overwritten'.format(i, k))

				os.remove(target)
				print('{0} whoopsied!'.format(target))

			# Directory
			elif os.path.isdir(target) and (self.options['recurse'] or not self.recursed):
				self.recursed = True
				for entry in os.scandir(target):
					self.__delete_prompt(entry.path)

				try:
					os.rmdir(target)
				except:
					print('Directory {0} not empty. No whoopsies.'.format(target))

			# Not found
			elif not os.path.isfile(target):
				raise FileNotFoundError('{0} not found'.format(target))

		else:	# Nope
			print('No whoopsies on {0}'.format(target))

	# Accidentally delete with no user prompting
	def __delete_silent(self, target):
		# File
		if os.path.isfile(target):
			length = os.path.getsize(target)*4 # convert to word-size
			for i in range(1, self.k, 1):
				with open(target, 'w') as f:
					f.write(self.__unicode(length))
			os.remove(target)

		# Directory
		elif os.path.isdir(target) and (self.options['recurse'] or not self.recursed):
			self.recursed = True
			for entry in os.scandir(target):
				self.__delete_silent(entry.path)

			try:
				os.rmdir(target)
			except:
				print('Directory {0} not empty. No whoopsies.'.format(target))

		# Not found
		elif not os.path.isfile(target):
			raise FileNotFoundError('{0} not found'.format(target))

	def __unicode(self, length):
		return ''.join(random.choice(alphabet) for i in range(length))

def main(target, k, options):
	whoops = Whoopsie(target = target, k = k, options = options)

if __name__ == '__main__':
	parser = ArgumentParser(prog=prog, description=description)

	# Optional Arguments
	parser.add_argument('--v', '--version', action='version', version='%(prog)s {0}'.format(version), help='show version info')
	parser.add_argument("-r", "--recurse", action="store_true", help="recursively delete all files and directories")
	parser.add_argument("-f", "--force", action="store_true", help="force delete -- hide all prompts")

	# Required Arguments
	parser.add_argument('loc', metavar='Location', type=str, action='store', help='Location of file or directory of files to be Whoopsied')
	parser.add_argument('k', metavar='K', type=int, default=5, action='store', help='Integer number of passes of random overwrites (default: 5)')

	# Parse Args
	args = parser.parse_args()
	options = vars(args)

	loc = options['loc']
	k = options['k']

	if k <= 0:
		raise ValueError('k should be a positive non-zero integer')

	del options['loc']
	del options['k']

	main(target = loc, k = k, options = options)
