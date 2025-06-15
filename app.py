from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'message': 'AI Video Editor API is running'})

# Add this to make sure it runs properly
if __name__ == '__main__':
    app.run()
