# misc module for dircbot
# all functions take a socket and a data stream as arguments

# keep-alive ping
# respond to server's PING command to keep connection alive
def ping(socket, stream):
    socket.send(b"PONG " + stream.split()[1] + b"\r\n")

# about
# reply with bot's version information
def about(socket, channel):
    socket.send(b"PRIVMSG " + channel + b" :dircbot 0.1 by Duy Nguyen\r\n")

# greet
# when an user joins the channel, send out a greeting
def greet(socket, channel):
    socket.send(b"PRIVMSG " + channel + b" :Welcome to " + channel + b" channel.\r\n")

# quit
# quit the channel
def quit(socket, channel):
    socket.send(b"QUIT\r\n")
