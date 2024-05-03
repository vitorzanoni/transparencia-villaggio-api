import logging

from flask import Flask
from flask.logging import default_handler
from flask_cors import CORS
from waitress import serve

from controller import boleto_controller

app = Flask("transparencia-villaggio-api")
CORS(app, origins=["https://localhost:4200"])
app.register_blueprint(boleto_controller.bp, url_prefix="/boleto")
log = logging.getLogger()
log.addHandler(default_handler)
log = app.logger
log.setLevel(10)
port = 5000
version = "1.0.0"


@app.route("/health", methods=["GET"])
def health():
    return {"status": "UP"}, 200


if __name__ == "__main__":
    log.info("%d | Transparencia Villaggio Api v%s", port, version)
    serve(app=app, host="0.0.0.0", port=port)
