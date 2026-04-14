"""
TCPClient.py
Cliente TCP simples que conecta ao servidor e envia uma frase
Parte 3
Slide 14
Karen Joilly
"""
from socket import *

serverName = '127.0.0.1'  # Endereco do servidor
serverPort = 12000  # Porta do servidor

clientSocket = socket(AF_INET, SOCK_STREAM)  # Cria socket TCP
clientSocket.connect((serverName, serverPort))  # Conecta ao servidor

sentence = input('Input lowercase sentence: ')  # Le a frase do usuario
clientSocket.send(sentence.encode())  # Envia a frase

modifiedSentence = clientSocket.recv(1024)  # Recebe resposta
print('From Server:', modifiedSentence.decode())  # Imprime resposta

clientSocket.close()  # Fecha o socket