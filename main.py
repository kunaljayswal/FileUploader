# * Import Python Module
from flask import Flask

# * Import User Defined Functions
from app.routes.fileCRUD import file_module
from utils.dbManager import db_manager

# * Initialize Flask API
app = Flask(__name__)

# * Initialize Base Flask API
@app.route("/")
def hello_world():
    return "Hello, User!"

app.register_blueprint(file_module, url_prefix="/files")

# * Run API Server
if __name__ == "__main__":
    # run_server()
    app.run(debug=True, port=8080)
    
