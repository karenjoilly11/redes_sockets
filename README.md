📋 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de **Redes de Computadores** e implementa comunicação cliente-servidor utilizando sockets **UDP** e **TCP** em Python.

## 📁 Estrutura do Projeto
Codigo/redes_sockets/
├── UDPClient.py # Cliente UDP
├── UDPServer.py # Servidor UDP
├── TCPClient.py # Cliente TCP simples
├── TCPServer.py # Servidor TCP simples
├── TCPConcurrentClient.py # Cliente TCP concorrente
└── TCPConcurrentServer.py # Servidor TCP concorrente (multithread)

text

## 🔧 Requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária (apenas socket, que já vem com Python)

## 🚀 Como Executar

### 1. Protocolo UDP (não orientado à conexão)

**Terminal 1 - Servidor:**
```bash
cd Codigo/redes_sockets
python3 UDPServer.py

**Terminal 2 - Cliente:**
```bash
cd Codigo/redes_sockets
python3 UDPClient.py

## 🔧 Requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária (apenas socket, que já vem com Python)

## 🚀 Como Executar

### 1. Protocolo UDP

**Terminal 1 - Servidor:**
```bash
cd Codigo/redes_sockets
python3 UDPServer.py
Terminal 2 - Cliente:

bash
cd Codigo/redes_sockets
python3 UDPClient.py
2. Protocolo TCP Simples
Terminal 1 - Servidor:

bash
cd Codigo/redes_sockets
python3 TCPServer.py
Terminal 2 - Cliente:

bash
cd Codigo/redes_sockets
python3 TCPClient.py
3. Servidor TCP Concorrente
Terminal 1 - Servidor:

bash
cd Codigo/redes_sockets
python3 TCPConcurrentServer.py
Terminal 2 - Cliente 1:

bash
cd Codigo/redes_sockets
python3 TCPConcurrentClient.py
Terminal 3 - Cliente 2:

bash
cd Codigo/redes_sockets
python3 TCPConcurrentClient.py
