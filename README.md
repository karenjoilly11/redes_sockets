## 📋 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de **Redes de Computadores** e implementa comunicação cliente-servidor utilizando sockets **UDP** e **TCP** em Python.

## 👩‍💻 Autora

- **Karen Joilly**
- GitHub: karenjoilly11

## 📁 Estrutura do Projeto
```
Codigo/redes_sockets/
|
├── UDPClient.py
├── UDPServer.py
├── TCPClient.py
├── TCPServer.py
├── TCPConcurrentClient.py
└── TCPConcurrentServer.py
```



## 🔧 Requisitos

- Python 3.x
- Nenhuma biblioteca externa necessária

## 🚀 Como Executar

### 1. Protocolo UDP

**Terminal 1 - Servidor:**
cd Codigo/redes_sockets
python3 UDPServer.py

text

**Terminal 2 - Cliente:**
cd Codigo/redes_sockets
python3 UDPClient.py

text

### 2. Protocolo TCP Simples

**Terminal 1 - Servidor:**
cd Codigo/redes_sockets
python3 TCPServer.py

text

**Terminal 2 - Cliente:**
cd Codigo/redes_sockets
python3 TCPClient.py

text

### 3. Servidor TCP Concorrente

**Terminal 1 - Servidor:**
cd Codigo/redes_sockets
python3 TCPConcurrentServer.py

text

**Terminal 2 - Cliente 1:**
cd Codigo/redes_sockets
python3 TCPConcurrentClient.py

text

**Terminal 3 - Cliente 2:**
cd Codigo/redes_sockets
python3 TCPConcurrentClient.py

text

## 📊 Diferenças UDP vs TCP

| Característica | UDP | TCP |
|----------------|-----|-----|
| Conexão | Sem conexão | Orientado à conexão |
| Confiabilidade | Não confiável | Confiável |
| Velocidade | Mais rápido | Mais lento |

## 🔗 Repositório

https://github.com/karenjoilly11/redes_sockets

## ✅ Status

- [x] UDP implementado
- [x] TCP simples implementado
- [x] TCP concorrente implementado

---

*Última atualização: Abril de 2026*
