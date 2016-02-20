#!/usr/bin/python

import os
import sys
import time
import zmq
from twisted.internet import reactor
from txzmq import ZmqEndpoint, ZmqFactory, ZmqREQConnection, ZmqREPConnection, ZmqRequestTimeoutError

"""
rep 实例可以多个，有复杂均衡的效果
"""

zf = ZmqFactory()
e = ZmqEndpoint('connect', "ipc:///tmp/txzmq-test-req")

sock = ZmqREPConnection(zf, e)

def doPrint(messageId, message):
	print "Replying to %s, %r" % (messageId, message)
	sock.reply(messageId, "%s %r " % (messageId, message))

sock.gotMessage = doPrint
reactor.run()