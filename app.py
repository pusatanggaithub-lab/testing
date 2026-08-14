from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Izinkan frontend mengakses backend ini

# Fungsi simulasi respons AI
def dapatkan_respon_ai(pesan_user):
    # Di sini kamu bisa panggil API OpenAI / Anthropic / LangChain
    pesan_lower = pesan_user.lower()
    if "halo" in pesan_lower:
        return "Halo! Ada yang bisa saya bantu hari ini?"
    elif "harga" in pesan_lower:
        return "Untuk info harga layanan, kamu bisa cek di menu Pricing."
    else:
        return f"🤖 [Bot AI]: Saya menerima pesanmu: '{pesan_user}'"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pesan_user = data.get('message', '')
    
    if not pesan_user:
        return jsonify({"status": "error", "reply": "Pesan tidak boleh kosong!"}), 400
        
    balasan_bot = dapatkan_respon_ai(pesan_user)
    return jsonify({"status": "success", "reply": balasan_bot})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
