from flask import Flask, render_template, request, jsonify, abort, session
import os
from pathlib import Path
from sys import path
import json
from urllib.parse import urlparse, parse_qs
import wiki


app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/globe')
def globe():
    return render_template('globe.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_history_summary', methods=['GET'])
def get_history_summary():
    country_name = request.args.get('country', default='Japan')
    start_year = int(request.args.get('start_year', default=1800))
    end_year = start_year+100
    
    history_text = wiki.fetch_history(country_name)
    relevant_text = wiki.extract_years(history_text, start_year, end_year)
    
    summary = wiki.promp_GPT("Provide a summary for: " + relevant_text, "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")
    
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug = True)