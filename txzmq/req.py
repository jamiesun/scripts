#!/usr/bin/python

import os
import sys
import time
import zmq
from twisted.internet import reactor
from txzmq import ZmqEndpoint, ZmqFactory, ZmqREQConnection, ZmqREPConnection, ZmqRequestTimeoutError

def on_resp(resp):
	print resp

zf = ZmqFactory()
e = ZmqEndpoint('bind', "ipc:///tmp/txzmq-test-req")

sender = ZmqREQConnection(zf, e)

def send():
	print 'send data'
	try:
		sender.sendMsg(str(int(time.time())), timeout=0.95).addCallback(on_resp)
	except:
		pass
	reactor.callLater(1, send)
	

reactor.callWhenRunning(reactor.callLater, 1, send)
reactor.run()