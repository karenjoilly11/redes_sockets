## 📋 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de **Redes de Computadores** e implementa comunicação cliente-servidor utilizando sockets **UDP** e **TCP** em Python.

## 👩‍💻 Autora

<div align="center">

| 👤 Nome | 🖼️ Foto | :octocat: GitHub | 💼 LinkedIn | 📤 Gmail |
|:---:|:---:|:---:|:---:|:---:|
| **Karen Joilly** | <img src="./assets/fotokaren.jpg" width="80px" style="border-radius: 50%;"> | <a href="https://github.com/vcaraujo"><img src="https://joaopauloaramuni.github.io/image/github6.png" width="40px"></a> | <a href="https://www.linkedin.com/in/karen-joilly-araujo-gregorio-de-almeida/"><img src="https://joaopauloaramuni.github.io/image/linkedin2.png" width="40px"></a> | <a href="mailto:karenjoilly@gmail.com"><img src="https://joaopauloaramuni.github.io/image/gmail3.png" width="40px"></a> |

</div>

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
