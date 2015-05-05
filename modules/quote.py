# random quoting module for dircbot
# function takes a socket and channel as arguments

import os
import random

def quote(socket, channel, filename):
    try:
        # resolve path for quote database
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, filename))

        # open the quote database in utf-8 encoding
        quote_file = open(filepath, "r", encoding="utf-8")
        
        # read the quotes into an array
        quote_list = quote_file.readlines()

        # seed the rng with the system's current time
        random.seed()

        # return a random quote from the array as utf-8 encoded bytes
        # move on if any exception occurs
        try:
            quotation = bytes(random.choice(quote_list), "utf-8")
        except UnicodeEncodeError:
            pass

        # send the quote
        socket.send(b"PRIVMSG " + channel + b" :" + quotation + b"\r\n")
    # move on if any exception occurs
    except:
        pass
