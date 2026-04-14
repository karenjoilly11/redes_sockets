""""
TCPConcurrentServer.py
Servidor TCP concorrente que aceita multiplos clientes usando threads
Parte 5
Slide 23
Karen Joilly
"""

import socket
import _thread

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 50000  # Porta do servidor

def conectado(con, cliente):
    """Funcao executada por cada thread para atender um cliente"""
    print('\nCliente conectado:', cliente)
    while True:
        msg = con.recv(1024)  # Recebe mensagem
        if not msg:  # Se nao houver mensagem, cliente desconectou
            break
        print('\nCliente...: ', cliente)
        print('Mensagem..: ', msg.decode())
        con.send(msg.upper())  # Envia resposta em maiusculas
    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()

# Cria o socket principal
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)  # Associa o socket a porta
tcp.listen(5)  # Escuta por ate 5 conexoes pendentes
print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)

# Loop principal do servidor
while True:
    con, cliente = tcp.accept()  # Aceita nova conexao
    print('\nNova thread iniciada para essa conexao')
    _thread.start_new_thread(conectado, (con, cliente))  # Cria thread