import json
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Fungsi untuk membaca file faq.json
def muat_data_faq():
    path_faq = os.path.join(os.path.dirname(__file__), 'faq.json')
    if os.path.exists(path_faq):
        with open(path_faq, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

# Fungsi pencari jawaban berdasarkan kata kunci di JSON
def cari_jawaban_faq(pesan_user):
    data_faq = muat_data_faq()
    pesan_lower = pesan_user.lower()
    
    # Cek setiap item FAQ
    for item in data_faq:
        for keyword in item['keywords']:
            # Jika kata kunci ada dalam pesan pengguna
            if keyword in pesan_lower:
                return item['jawaban']
                
    # Jawaban default jika tidak ada kata kunci yang cocok
    return "Maaf, saya belum memahami pertanyaanmu. Coba tanyakan hal lain seperti 'jam buka', 'harga paket', atau 'kontak admin'."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pesan_user = data.get('message', '') if data else ''
    
    if not pesan_user.strip():
        return jsonify({"status": "error", "reply": "Pesan tidak boleh kosong!"}), 400
        
    # Cari jawaban dari file faq.json
    balasan = cari_jawaban_faq(pesan_user)

    return jsonify({"status": "success", "reply": balasan})

if __name__ == '__main__':
    app.run(port=5000, debug=True)


from flask import Flask, render_template, request, jsonify, send_from_directory
import os

# (Kode app.py kamu yang lainnya tetap sama...)

# Tambahkan route ini di app.py:
@app.route('/widget.js')
def serve_widget():
    return send_from_directory(os.path.dirname(__file__), 'widget.js')
