#!/usr/bin/python
#
# ./king_resolver.py
# Data de criação: 25/11/2021
# Autor: Reinaldo Garcia
# Versão: 1.0
# Descrição: Script em Python para resolução de nomes

import socket,sys

if len(sys.argv) != 2:
    print("Modo de uso: python king_resolver.py site.com")
else:
    host = sys.argv[1]
    print("== King Resolver ==")
    print("== Domínio = Endereço IP ==\n")
    print(host,"--->",socket.gethostbyname(host))
