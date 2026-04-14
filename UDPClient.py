"""
UDPClient.py
Este é um exemplo de um cliente UDP simples que envia uma mensagem para o servidor, recebe a mensagem modificada do servidor e a imprime na tela.
Parte 1
Slide 8
Karen Joilly
"""
from socket import *

serverName = '127.0.0.1' # Endereço IP do Servidor (localhost)
serverPort = 12000 # Numero da Porta do Servidor

clientSocket = socket(AF_INET, SOCK_DGRAM) # Cria um socket UDP

sentence = input('Input lowercase sentence: ') # Solicita ao usuário para digitar uma frase em minúsculas
clientSocket.sendto(sentence.encode(), (serverName, serverPort)) # Envia a frase para o servidor

modifiedSentence, serverAddress = clientSocket.recvfrom(2048) # Recebe a frase modificada do servidor
print('From Server:', modifiedSentence.decode()) # Imprime a frase modificada recebida do servidor

clientSocket.close() # Fecha o socket do cliente