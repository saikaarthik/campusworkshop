"""Setup at app startup"""
from app import routes
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
    host="dpg-chi7udt269vf5qbbp63g-a.singapore-postgres.render.com",
    database="todo_prgn",
    user="todo_prgn_user",
    password="8ZE6fe2FBiJnnVwHzQz8c8Gj2MiBr7RX")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
