from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head><meta charset="utf-8"><title>CRISTIAN</title></head>
    <body style="font-family: sans-serif; display:flex;align-items:center;justify-content:center;height:100vh;">
      <div style="text-align:center;">
        <h1>CRISTIAN STEVEN CALLE CUZCO</h1>
        <p>Versión 3.0.0 — Ejecutándose con Flask</p>
      </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
