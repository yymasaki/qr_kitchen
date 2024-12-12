from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/img/<path:filename>')
def serve_pdf(filename):
    return send_from_directory('img', filename)

if __name__ == '__main__':
    app.run(debug=True, port=8000)