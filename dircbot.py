#!/usr/bin/env python3.4

# dircbot 0.1 - a Python IRC bot
# by Duy Nguyen

# import system modules
import random
import socket
import sys
import time
import threading

# import my own modules in modules/ subfolder
import modules.quote as quote
import modules.misc as misc
import modules.pingpong as pingpong

# configuration
# all string configuration must be set with a "b" prefix (typecasting variables
# as bytes in order for Python to communicate with server through sockets)

# bot's nickname
nickname = b"dircbot"

# server, port and socket buffer size
#
# irc server address and port
# 6667 is the default insecure irc port of all popular irc servers
server = b"irc.freenode.net"
port = 6667

# buffer size
# from Python socket documentation: "the value of bufsize should be a 
# relatively small power of 2, for example, 4096"
# so you can leave buffer_size as it is
buffer_size = 4096

# channel to join
channel = b"##py_irc_test4235"

# random quoting configuration
# quote database
filename = "quote.txt"
# minimum and maximum interval between sending each quote (in seconds)
min_interval = 20
max_interval = 40

# debug mode
debug = True

# seed the rng with the system's current time for random quoting later on
random.seed()

# create an internet socket and connect to the IRC server
irc = socket.socket()
irc.connect((server, port))

def main():
    # authorize with server
    # send bot's nickname
    irc.send(b"NICK " + nickname + b"\r\n")    
    # send bot's identification using the USER command
    # RFC 2812 compliant
    irc.send(b"USER dirc 0 * :dircbot\r\n")
    # join the predefined channel
    irc.send(b"JOIN " + channel + b"\r\n")

    print("dircbot 0.1 running. Press Ctrl+C to stop.")

    # loop for as long as the connection is alive
    while True:
        # initialize a buffer for socket data stream
        buffer_data = irc.recv(buffer_size)
        if debug == True:    # print buffer data if debug mode is on
            print(buffer_data)
        else:
            pass
        
        # rudimentary chat parsing, should be reworked sometime in the future 
        # as this has a lot of drawbacks
        # keep-alive ping, greeting and about commands
        # respond to server's PING command to keep connection alive
        if buffer_data.find(b"PING") != -1:
            misc.ping(irc, buffer_data)
        # when an user joins the channel, the buffer stream will receive
        # a JOIN command. if a JOIN is found, send out a greeting
        if buffer_data.find(b"JOIN") != -1:
            misc.greet(irc, channel)
        # when users type !about into chat, reply with version information
        if buffer_data.find(b":!about\r\n") != -1:
            misc.about(irc, channel)

        # ping-pong feature
        # if users send a "ping" message, reply with "pong"
        # there is distinction between lower and uppercase "ping"
        if buffer_data.find(b":ping\r\n") != -1:
            pingpong.pingpong(irc, channel, False)
        elif buffer_data.find(b":PING\r\n") != -1:
            pingpong.pingpong(irc, channel, True)

def quoting(socket, channel, filename):
    while True:
        interval = random.randint(min_interval, max_interval)
        time.sleep(interval)
        quote.quote(socket, channel, filename)

# showtime
def run():
    try:
        # 2 threads running concurrently to prevent I/O or 
        # timer blocking misc functions
        # main thread that parses IRC stream for chat commands
        threading.Thread(target=main).start()
        # another thread runs concurrently to provide quotations
        threading.Thread(target=quoting, args=(irc, channel, filename)).start()
    # handling SIGINT or EOF gracefully
    # quit the channel, close socket and exit the program
    except KeyboardInterrupt or EOFError:
        misc.quit(irc, channel)
        irc.close()
        print("Bot terminated.")
        sys.exit()

run()
