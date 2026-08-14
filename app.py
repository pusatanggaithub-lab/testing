from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. TAMBAHKAN ROUTE INI (Untuk menampilkan halaman utama HTML)
@app.route('/')
def home():
    return render_template('index.html')

# 2. ROUTE CHATBOT (Untuk memproses pesan)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pesan_user = data.get('message', '') if data else ''
    
    if not pesan_user:
        return jsonify({"status": "error", "reply": "Pesan tidak boleh kosong!"}), 400
        
    # Logika sederhana respons bot
    pesan_lower = pesan_user.lower()
    if "halo" in pesan_lower or "hi" in pesan_lower:
        balasan = "Halo! Ada yang bisa saya bantu hari ini?"
    elif "harga" in pesan_lower:
        balasan = "Untuk informasi harga, silakan hubungi tim kami."
    else:
        balasan = f"🤖 [Bot AI]: Saya menerima pesanmu: '{pesan_user}'"

    return jsonify({"status": "success", "reply": balasan})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
