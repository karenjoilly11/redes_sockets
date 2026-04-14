""""
UDPServer.py
Este é um exemplo de um servidor UDP simples que recebe mensagens de clientes, 
converte as mensagens para maiúsculas e as envia de volta para os clientes.
Parte 2
Slide 9
Karen Joilly
"""
from socket import *

serverPort = 12000 # Numero da Porta do Servidor
serverSocket = socket(AF_INET, SOCK_DGRAM) # Cria um socket UDP
serverSocket.bind(('', serverPort)) # Associa o Socket a um endereço e porta

print('The server is ready to receive') # Informa que o servidor está pronto para receber mensagens

while True:
    message, clientAddress = serverSocket.recvfrom(2048) # Recebe a mensagem do cliente e o endereço do cliente
    modifiedMessage = message.decode().upper() # Converte a mensagem para maiúsculas
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) # Envia a mensagem modificada de volta para o cliente