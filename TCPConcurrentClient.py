"""
TCPConcurrentClient.py
Cliente TCP para testar o servidor concorrente
Parte 6
Slide 26
Karen Joilly
"""
import socket

HOST = '127.0.0.1'  # Endereco do servidor
PORT = 50000  # Porta do servidor

# Cria e conecta o socket
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)

print('\nDigite suas mensagens')
print('Para sair use Control + X\n')

mensagem = input()
while mensagem != '\x18':  # \x18 eh o caractere Control+X
    tcp.send(mensagem.encode())  # Envia mensagem
    resposta = tcp.recv(1024)  # Recebe resposta
    print('Resposta do servidor:', resposta.decode())
    mensagem = input()

tcp.close()  # Fecha socket