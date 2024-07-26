from flask import Flask, request, jsonify
import certbot.main

app = Flask(__name__)

@app.route('/create_ssl', methods=['POST'])
def create_ssl():
    domain = request.json.get('domain')
    email = request.json.get('email')
    
    try:
        certbot.main.main([
            'certonly',
            '--non-interactive',
            '--agree-tos',
            '--email', email,
            '--standalone',
            '-d', domain
        ])
        return jsonify({'status': 'success', 'message': 'SSL certificate created successfully.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context=('server.crt', 'server.key'))