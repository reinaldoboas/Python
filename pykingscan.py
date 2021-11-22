#!/usr/bin/python
#
# ./pykingscan.py
# Criação: 22/11/21
# Autor: Reinaldo Garcia
# Versão: 1.0
# Descrição: Script que realiza port scannning escrito em Python

import socket,sys

if len(sys.argv) != 2:
        print("Modo de uso: python ./pykingscan.py 192.168.0.1")
else:
        for porta in range(1,65535):
                meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if meusocket.connect_ex((sys.argv[1],porta)) == 0:
                        print("Porta",porta,"[ABERTA]")
                        meusocket.close()
