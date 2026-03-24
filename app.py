from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():

    # On définit le contenu HTML et le CSS directement ici
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Demo DevOps K8s</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f6;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                text-align: center;
                border-top: 8px solid #007bff;
                max-width: 500px;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
            }
            p {
                color: #666;
                font-size: 1.2rem;
                line-height: 1.5;
            }
            .badge {
                display: inline-block;
                background-color: #28a745;
                color: white;
                padding: 8px 20px;
                border-radius: 50px;
                font-weight: bold;
                margin-top: 20px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 DevOps Project</h1>
            <p>Hello hello?! Mon infrastructure DevOps fonctionne sur <strong>Kubernetes</strong> !</p>
            <div class="badge">● Pipeline Jenkins : Success</div>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


    
