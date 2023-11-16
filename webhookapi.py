from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print('Webhook alındı:', data)
    return jsonify({'message': 'Webhook başarıyla alındı'})

if __name__ == '__main__':
    app.run(port=3000)
