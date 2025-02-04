from flask import Flask, redirect, url_for, send_from_directory
from receipts.routes import receipts_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import os


# create the application
app = Flask(__name__) 

def register_receipts():
  app.register_blueprint(receipts_blueprint, url_prefix="/receipts")

def config_swagger() -> str:
  SWAGGER_URL = '/swagger'
  API_URL = '/swagger.json'
  swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Receipt Processor"}
  )
  app.register_blueprint(swaggerui_blueprint, prefix=SWAGGER_URL)

# register blueprints
register_receipts()
config_swagger()

@app.route("/swagger.json")
def swagger_route():
   return send_from_directory(os.path.join(os.getcwd(), "receipts/config"), "swagger.json")

#redirect to swagger docs
@app.route("/")
def home():
    print(os.path.join(os.getcwd(), "receipts/config"))
    return redirect(url_for('swagger_ui.show'))

if __name__ == '__main__':
  app.run(host="0.0.0.0", port="4000", debug=True)