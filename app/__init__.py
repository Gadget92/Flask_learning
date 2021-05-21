from flask import Flask

app = Flask(__name__)

# Fix cycle error
from app import routes
