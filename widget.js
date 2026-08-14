(function () {
  // 1. Buat & Sisipkan Style CSS Kotak Chat Secara Otomatis
  const style = document.createElement('style');
  style.innerHTML = `
    .custom-chat-button {
      position: fixed; bottom: 20px; right: 20px;
      background: #007bff; color: white; border: none;
      border-radius: 50%; width: 60px; height: 60px;
      font-size: 24px; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.2);
      z-index: 9999;
    }
    .custom-chat-box {
      display: none; position: fixed; bottom: 90px; right: 20px;
      width: 320px; height: 420px; background: white;
      border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);
      flex-direction: column; overflow: hidden; z-index: 9999; font-family: sans-serif;
    }
    .chat-header { background: #007bff; color: white; padding: 15px; font-weight: bold; text-align: center; }
    .chat-logs { flex: 1; padding: 10px; overflow-y: auto; background: #f9f9f9; }
    .msg { margin-bottom: 8px; font-size: 14px; padding: 8px 12px; border-radius: 6px; max-width: 80%; }
    .msg.user { background: #007bff; color: white; margin-left: auto; text-align: right; }
    .msg.bot { background: #e9e9e9; color: #333; margin-right: auto; text-align: left; }
    .chat-input { display: flex; padding: 10px; border-top: 1px solid #ddd; background: white; }
    .chat-input input { flex: 1; padding: 8px; border: 1px solid #ccc; border-radius: 4px; outline: none; }
    .chat-input button { margin-left: 5px; padding: 8px 12px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
  `;
  document.head.appendChild(style);

  // 2. Buat Elemen HTML Widget
  const chatButton = document.createElement('button');
  chatButton.className = 'custom-chat-button';
  chatButton.innerHTML = '💬';

  const chatBox = document.createElement('div');
  chatBox.className = 'custom-chat-box';
  chatBox.innerHTML = `
    <div class="chat-header">Asisten Bot AI</div>
    <div class="chat-logs" id="widgetChatLogs">
      <div class="msg bot">Halo! Ada yang bisa saya bantu?</div>
    </div>
    <div class="chat-input">
      <input type="text" id="widgetUserInput" placeholder="Ketik pesan...">
      <button id="widgetSendBtn">Kirim</button>
    </div>
  `;

  document.body.appendChild(chatButton);
  document.body.appendChild(chatBox);

  // Toggle Buka/Tutup Chat
  chatButton.onclick = () => {
    chatBox.style.display = chatBox.style.display === 'flex' ? 'none' : 'flex';
  };

  // 3. Logika Kirim Pesan ke Backend Vercel
  const BASE_URL = 'https://testing-theta-gold.vercel.app'; // URL Vercel kamu

  async function sendMessage() {
    const input = document.getElementById('widgetUserInput');
    const logs = document.getElementById('widgetChatLogs');
    const msg = input.value.trim();
    if (!msg) return;

    logs.innerHTML += `<div class="msg user">${msg}</div>`;
    input.value = '';
    logs.scrollTop = logs.scrollHeight;

    try {
      const res = await fetch(`${BASE_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
      });
      const data = await res.json();
      logs.innerHTML += `<div class="msg bot">${data.reply}</div>`;
      logs.scrollTop = logs.scrollHeight;
    } catch (e) {
      logs.innerHTML += `<div class="msg bot" style="color:red;">Gagal terhubung.</div>`;
    }
  }

  document.getElementById('widgetSendBtn').onclick = sendMessage;
  document.getElementById('widgetUserInput').onkeydown = (e) => {
    if (e.key === 'Enter') sendMessage();
  };
})();
