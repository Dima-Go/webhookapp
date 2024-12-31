from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
   print(f"Received webhook data", flush=True)  
   return 'Webhook received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)