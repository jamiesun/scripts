#!/usr/bin/env python
#coding:utf-8
from __future__ import unicode_literals
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import binascii
import hashlib
import base64
import random
import os
import time

class AESCipher:
	
	def __init__(self,key=None):
		if key:self.setup(key)

	def setup(self, key): 
		self.bs = 32
		self.ori_key = key
		self.key = hashlib.sha256(key.encode()).digest()

	def encrypt(self, raw):
		raw = raw.encode('utf-8')
		raw = self._pad(raw)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(self.key, AES.MODE_CBC, iv)
		return base64.b64encode(iv + cipher.encrypt(raw))

	def decrypt(self, enc):
		enc = base64.b64decode(enc)
		iv = enc[:AES.block_size]
		cipher = AES.new(self.key, AES.MODE_CBC, iv)
		return self._unpad(cipher.decrypt(enc[AES.block_size:]))

	def _pad(self, s):
		return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

	def _unpad(self,s):
		return s[:-ord(s[len(s)-1:])]




if __name__ == '__main__':
	
	aes = AESCipher("123456")
	print aes.encrypt("123")
	print aes.encrypt("好")
	print aes.decrypt("mDamye3CB4KgKOICOZ/K4y3UIGCcnRHQrRbxybEdF4CzKR0c/S108SSBg3D11yfO")





