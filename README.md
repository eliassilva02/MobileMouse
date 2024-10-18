# 🚀 Projeto: MobileMouse

![Python](https://img.shields.io/badge/python-3.x-blue?logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

---

## 📖 Descrição do Projeto
O **MobileMouse** é um projeto que permite que um dispositivo móvel controle o cursor do mouse em um computador.

---

## 🛠 Tecnologias Utilizadas
- **Backend:** Python com WebSockets
- **Frontend:** HTML e JavaScript puro

---

## ✨ Funcionalidades
- **Controle de Mouse:** Movimentação do cursor do mouse no computador a partir de gestos de toque no celular.
- **Eventos de Clique:** Captura de toques no celular para simular cliques do mouse no computador.
- **Conexão em Tempo Real:** Comunicação bidirecional usando WebSockets, garantindo que os movimentos e cliques sejam refletidos imediatamente.

---

## 🏗 Estrutura do Projeto
### 🔌 Backend (Python)
- Configuração de um servidor WebSocket que escuta os eventos de entrada do celular.
- Processamento dos eventos de toque e clique, enviando as ações correspondentes ao sistema do computador.

### 🌐 Frontend (HTML/JavaScript)
- Interface simples em HTML para se conectar ao servidor WebSocket.
- Captura de eventos de toque e clique utilizando JavaScript, enviando os dados para o backend.

---

## ⚙️ Fluxo de Trabalho
1. O usuário abre a interface do MobileMouse em seu celular.
2. O celular se conecta ao servidor WebSocket em execução no computador.
3. O usuário interage com a interface do celular, e os eventos de toque e clique são capturados.
4. Os eventos são enviados via WebSocket para o backend Python, que processa as ações.
5. O cursor do mouse no computador é movido ou clicado de acordo com os eventos recebidos.

---

## 📋 Requisitos
- **Bibliotecas:** `websockets|py`, `asyncio|py`, `pyautogui|py`, `WebSockets|js`

---

## 🏁 Como Executar
1. Configure o servidor WebSocket em Python e inicie-o.
2. Inicie um servidor http na sua rede, dentro da pasta client, com o comando:
    ```powershell
    py -m http.server 8000
2. Acesse o html em um navegador no celular utilizando o IP da sua rede.
3. A partir do celular, interaja com a interface e veja o cursor do mouse do computador se mover conforme os comandos enviados.