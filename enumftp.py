# Data: 02/05/2022
# Autor: Reinaldo Garcia
# Versão: 1.0
# Descrição: Script para conectar com o usuário anonymous no FTP 

import socket
import sys

if len(sys.argv) != 2:
    print("Modo de uso: python enumftp.py site.com")
else:
    print("Conectando com o Servidor FTP\n")
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((sys.argv[1], 21))

    # Capturar o banner
    banner = tcp.recv(1024)
    print(banner)

    # Envio do Usuario
    print("Enviado o usuario\n")
    mensagem = (b"USER anonymous\r\n")
    tcp.send(mensagem)
    user = tcp.recv(1024)
    print(user)

    # Envio da Senha
    print("Enviando a senha\n")
    tcp.send(b"PASS anonymous\r\n")
    password = tcp.recv(1024)
    print(password)

    # Executar HELP
    print("Executando o comando HELP\n")
    tcp.send(b"HELP \r\n")
    cmd = tcp.recv(2048)
    print(cmd)
