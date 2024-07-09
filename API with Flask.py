from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.json
    user_input = data.get('input')
    # Process the input as needed
    response = {'message': f'Received input: {user_input}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
