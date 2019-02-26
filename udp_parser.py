import socket
from _socket import SOL_SOCKET, SO_BROADCAST
import time
import array

#[jthorn] I know it's bad to do this, but I am doing it anyways
import sys
reload(sys)
sys.setdefaultencoding('ISO-8859-1')

'''
[jthorn]: parses binary arrays received over udp broadcasts and converts to hex string
'''

UDP_IP = "127.255.255.255"
UDP_PORT = 54321
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.bind((UDP_IP, UDP_PORT))
while True:
     data, addr = sock.recvfrom(1024)
     decoded = array.array('b', data).tostring().decode('ISO-8859-1').strip()
     print "received message:", decoded.encode('hex')