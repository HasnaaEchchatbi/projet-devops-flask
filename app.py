from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Il faut exactement 4 espaces (ou une tabulation) avant le "return"
    return "Hello hello?! Mon infrastructure DevOps fonctionne sur Kubernetes !"

if __name__ == '__main__':
    # Il faut exactement 4 espaces avant "app.run"
    app.run(host='0.0.0.0', port=5000)

