#!/usr/share/python
#
# ./consulta_whois.py
# Data de criação: 22/12/2021
# Autor: Reinaldo Garcia
# Versão: 1.0
# Descrição: Script em python que realiza consulta whois

import socket,sys

ALVO = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.iana.org",43))
s.send(ALVO+"\r\n")
resposta = s.recv(1024).split()
responsavel = resposta[19]
s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((responsavel, 43))
s1.send(ALVO+"\r\n")
resposta = s1.recv(1024)
print(resposta)
