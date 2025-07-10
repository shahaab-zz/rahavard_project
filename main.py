# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import urllib.request
import json

app = Flask(__name__)

AUTH_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NTE4MjE1MDEsImp0aSI6IjVmOTc3ZDA3YWY5ODQ0ODBiY2IzMzBlM2NlZTBjNjM0Iiwic3ViIjoiMTc4MTE4MyIsIm5iZiI6MTc1MTgyMTUwMSwiZXhwIjoxNzU5NTk3NTYxLCJpc3MiOiJjb20ubWFibmFkcC5hcGkucmFoYXZhcmQzNjUudjEifQ.nWrNfmZvFXfjBylDhaDq6yT1Tirdk4yyXXyVUJ7-TnHF2NzRIhRH08trAD82Fm3Mm3rAJOadN1RbeFe05tQIRECe68oyGKgKOS4cst0fRUfDr-AHDZHOPNYY6MPpshe18_vueFoNWkahPpLNxbx7obIMT_elK_2UALMKDxh1BL8mTYSquJoo3xwfscUT55GPi9X0hMxUu_igXcoC-ZoKEDji4nqcYmUZ7UKJ9yreb0hIN_uu5I3KH8hGFOETBx39z7WjK2KwwcFs3J2K-FrefExkd1ynsrxgHbbiaWyNbWil5o7CP13SZ3P9PYjNPZqabGQzMl07wP4V6NbIEPEjDw"

RAHAVARD_URL = (
    "https://rahavard365.com/api/v2/chart/bars?"
    "countback=334&"
    "symbol=exchange.asset:673:real_close:type0&"
    "resolution=D&"
    "from=2022-07-06T00:00:00Z&"
    "to=2023-10-16T00:00:00Z"
)

HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "platform": "web",
    "application-name": "rahavard"
}

@app.route('/')
def home():
    return "🚀 سرور پروکسی فعال است! برای تست از مسیر /api/nouri استفاده کنید."

@app.route('/api/nouri')
def get_nouri_data():
    req = urllib.request.Request(RAHAVARD_URL, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.load(response)
            return jsonify({"status": "✅ موفق", "data": data})
    except Exception as e:
        return jsonify({"status": "⛔ خطا در اتصال به ره‌آورد", "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
