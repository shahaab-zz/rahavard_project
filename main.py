# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 سرور پروکسی فعال است! برای تست از مسیر /api/test استفاده کنید."

@app.route('/api/test')
def test_proxy():
    try:
        url = "https://www.iranjib.ir"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        html = response.text
        return jsonify({"status": "✅ موفق", "content_sample": html[:300]})  # فقط ۳۰۰ کاراکتر اول برای تست
    except Exception as e:
        return jsonify({"status": "⛔ خطا در اتصال", "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
