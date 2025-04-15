from flask import Flask
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/healthz')
def health():
    # Will return 500 after 10 seconds (Failure)
    if time.time() - start_time < 10:
        return "OK", 200
    else:
        return "ERROR", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

