from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

# CSV file path
csv_file_path = 'network_traffic.csv'  # Path to the CSV file

@app.route('/')
def index():
    df = pd.read_csv(csv_file_path)  # Read the CSV file into a DataFrame
    entries = df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
    json_entries = json.dumps(entries)  # Convert entries to JSON format
    return render_template('index.html', json_entries=json_entries)  # Pass JSON entries to the template

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
