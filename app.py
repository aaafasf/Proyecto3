from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi App Flask</title>
        <style>
            body { 
                font-family: sans-serif; 
                background-color: #f0f2f5;
                display: flex; 
                justify-content: center;
                align-items: center; 
                height: 100vh; 
                margin: 0; 
            }
            .card { 
                background: white; 
                padding: 2rem; 
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                text-align: center; 
            }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>CRISTIAN STEVEN CALLE CUZCO</h1>
            <p>Ejecutándose con Flask y probado con Pytest. Versión 3.0.0</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
