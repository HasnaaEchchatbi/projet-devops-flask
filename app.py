from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
 # Design minimaliste et professionnel
    return """
    <div style="text-align:center; padding:50px; font-family:sans-serif; background-color:#f0f4f8; height:100vh;">
        <div style="background:white; display:inline-block; padding:30px; border-radius:15px; shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 5px solid #007bff;">
            <h1 style="color:#007bff;">🚀 Projet Master DevOps</h1>
            <p style="font-size:1.2em; color:#333;">Hello hello?! Mon infrastructure fonctionne sur <b>Kubernetes</b> !</p>
            <span style="color:green;">✔ CI/CD Jenkins validée</span>
        </div>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    
