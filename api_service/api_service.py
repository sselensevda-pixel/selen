 from flask import Flask, request, jsonify 
from flask_cors import CORS 
import psycopg2, os 
app = Flask(__name__) 
CORS(app) 
DATABASE_URL = os.getenv( 
"DATABASE_URL", 
"postgresql://selen_user:bdtwMiVlpDP6OGQVVkvp5LSrNjJ8nJGE@dpg-d71s76e3jp1c739hlp1g-a/selen" 
) 
def connect_db(): 
return psycopg2.connect(DATABASE_URL) 
@app.route("/ziyaretciler", methods=["GET", "POST"]) 
def ziyaretciler(): 
conn = connect_db() 
cur = conn.cursor() 
cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim 
TEXT)") 
if request.method == "POST":
isim = request.json.get("isim") 
if isim: 
cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)", (isim,))
