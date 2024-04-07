from flask import Flask, render_template, request, jsonify, abort, session
import os
from pathlib import Path
from sys import path
import json
from urllib.parse import urlparse, parse_qs
import wiki
import yaml
import openai


app = Flask(__name__)
app.config.from_object('config.Config')

with open("config.yml", 'r') as stream:
    config = yaml.safe_load(stream)

@app.route('/globe')
def globe():
    return render_template('globe.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_history_summary', methods=['GET'])
def get_history_summary():
    country_name = request.args.get('country')
    
    start_year = int(request.args.get('start_year'))
    end_year = start_year + 100
    if(end_year > 2023):
        end_year = 2023
        
    complexity = request.args.get('complexity')
    history_text = wiki.fetch_history(country_name)
    relevant_text = wiki.extract_years(history_text, start_year, end_year)
    prompt = f"Provide a {complexity} summary only within the time frame from {start_year} to {end_year} of the following information: " + relevant_text
    summary = wiki.promp_GPT(prompt, config['api_key'])
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug = True)