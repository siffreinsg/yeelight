import socket
import struct

MCAST_GRP = '239.255.255.250'
MCAST_PORT = 1982
SRC_PORT = 5159  # my random port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.bind(('', SRC_PORT))
sock.sendto("M-SEARCH * HTTP/1.1\r\n\
HOST: 239.255.255.250:1982\r\n\
MAN: \"ssdp:discover\"\r\n\
ST: wifi_bulb\r\n".encode(), (MCAST_GRP, MCAST_PORT))

# close this multicast socket
sock.close()

# and open a new receive socket on the same port
sock_recv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock_recv.bind(('', SRC_PORT))

while True:
    print(sock_recv.recv(10240).decode())
