"""
TCPServer.py
Servidor TCP simples que aceita uma conexao, converte mensagem para maiusculas
Parte 4
Slide 15
Karen Joilly
"""
from socket import *

serverPort = 12000  # Porta do servidor
serverSocket = socket(AF_INET, SOCK_STREAM)  # Cria socket TCP
serverSocket.bind(('', serverPort))  # Associa a porta
serverSocket.listen(1)  # Escuta por conexoes

print('The server is ready to receive')  # Servidor pronto

while True:  # Loop infinito
    connectionSocket, addr = serverSocket.accept()  # Aceita conexao
    sentence = connectionSocket.recv(1024).decode()  # Recebe dados
    capitalizedSentence = sentence.upper()  # Converte para maiusculas
    connectionSocket.send(capitalizedSentence.encode())  # Envia resposta
    connectionSocket.close()  # Fecha conexao