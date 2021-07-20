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

import re
import sys
import json
import requests
import urllib.request

class Request:
	"""
		This class is used to make all server requests
	"""
	# Progressbar
	@staticmethod
	def dlProgress(count, blockSize, totalSize):
		"""
		Progressbar for backup download
		"""
		percent = int(count*blockSize*100/totalSize)
		sys.stdout.write('\r[+] Downloading: ' + '%d%%' % percent)
		sys.stdout.flush()
	
	@staticmethod
	def urlretrieve(url, output):
		"""
		This method is used to download the backup file.
		"""
		try:
			request = urllib.request.urlretrieve(url, output, reporthook=Request.dlProgress)
			return request
		except urllib.error.HTTPError as e:
			return str(e)


	@staticmethod
	def authenticate(ip, username, password):
		"""
		This method authenticates the user.
			There are three error types which can occur:
				Connection timeout
				Connection error
				anything else
		"""
		print('\n[+] Requesting Cookie...')
		payload = {'action': 'login', 'username': username, 'password': password}
		try:
			r = requests.post(ip + '/telpho/login.php', payload, allow_redirects=False, timeout=5)
			cookie = dict(PHPSESSID=r.cookies['PHPSESSID'])
			return [r.text, cookie]
		except requests.Timeout:
			print('[x] Connection timed out')
			exit()
		except requests.ConnectionError:
			print('[x] Connection error\n | Please make sure you provided the right URL')
			exit()
		except requests.RequestException as e:
			print(str(e))

	@staticmethod
	def get_request(url, cookie=dict(PHPSESSID='None')):
		"""
		All GET requests are done in this method.
			There are three error types which can occur:
				Connection timeout
				Connection error
				anything else
		"""
		try:
			r = requests.get(url, cookies=cookie, timeout=5)
			return r.text
		except requests.Timeout as e:
			print('[x] Connection timed out')
			exit()
		except requests.ConnectionError:
			print('[x] Connection error')
			print(' | Server seems down.')
			exit()
		except requests.RequestException as e:
			print(str(e))


	@staticmethod
	def post_request(url, cookie, multipart_data):
		"""
		All POST requests are done in this method.
			There are three error types which can occur:
				Connection timeout
				Connection error
				anything else
		"""
		try:
			r = requests.post(url, cookies=cookie, data=multipart_data, headers={'Content-Type': multipart_data.content_type}, timeout=5)
			return r.text
		except requests.Timeout:
			print('[x] Connection timed out')
			exit()
		except requests.ConnectionError:
			print('[x] Connection error\n | Please make sure you provided the right URL')
			exit()
		except requests.RequestException as e:
			print(str(e))