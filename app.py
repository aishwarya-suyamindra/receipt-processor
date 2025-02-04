from flask import Flask
from receipts.routes import receipts_blueprint

def create_app():
  app = Flask(__name__)
  app.register_blueprint(receipts_blueprint, url_prefix="/receipts")
  return app

if __name__ == '__main__':
  app = create_app()
  app.run(host="0.0.0.0", port="4000", debug=True)