from models import db
from app import app

# Create tables
db.drop_all()
db.create_all()