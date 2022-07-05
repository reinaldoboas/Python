#!/usr/bin/python
# 
# ./kinghash.py
# Data de criação: 29/06/2022
# Autor: Reinaldo Garcia
# Versão: 1.0
# Descrição: Script desenvolvido para descobrir senhas com salt por meio de wordlist

import sys,crypt,re

# Removendo espacos em branco
def remove(string):
    pattern = re.compile(r'\n+')
    return re.sub(pattern, '', string)

# Variaveis
wordlist = open("/usr/share/wordlists/rockyou.txt")
salt = str(input("Digite o Salt: "))
hash_completo = str(input("Digite o Hash: "))
hash_salt = crypt.crypt(remove(hash_completo),remove(salt))

print("\nIniciando o Brute Force:")
print("=-=" * 15)

# Repeticao lendo wordlist
for linha in wordlist:
    hash_linha = crypt.crypt(remove(linha),salt)

    # Procurando por senha
    if (str(hash_completo) == str(hash_linha)):
        print(f"\nSenha encontrada: {linha}")
        print("=-=" * 15)
