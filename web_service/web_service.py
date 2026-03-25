from flask import Flask, render_template_string, request, redirect 
import requests 
 
app = Flask(__name__) 
 
API_URL = "https://hello-cloud4.onrender.com" 
 
HTML = """ 
<!doctype html> 
<html> 
<head> 
    <title>Mikro Hizmetli Selam!</title> 
    <style> 
        body { font-family: Arial; text-align: center; padding: 50px; background: #eef2f3; } 
        h1 { color: #333; } 
        input { padding: 10px; font-size: 16px; } 
        button { padding: 10px 15px; background: #4CAF50; color: white; border: none; 
border-radius: 6px; cursor: pointer; } 
        li { background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 
5px; } 
    </style> 
</head> 
<body> 
    <h1>Mikro Hizmetli Selam!<
     <p>Adını yaz</p> 
    <form method="POST"> 
        <input type="text" name="isim" placeholder="Adını yaz" required> 
        <button type="submit">Gönder</button>
