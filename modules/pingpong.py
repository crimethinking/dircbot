# ping-pong module for dircbot
# function takes a socket, channel and lower/uppercase Boolean as arguments
def pingpong(socket, channel, case):
    if case == False:
        socket.send(b"PRIVMSG " + channel + b" :pong\r\n")
    else:
        socket.send(b"PRIVMSG " + channel + b" :PONG\r\n")