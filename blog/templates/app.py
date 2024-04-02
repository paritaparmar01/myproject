from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data = [
    {"name": "Data 1", "date": "2024-01-01"},
    {"name": "Data 2", "date": "2024-01-05"},
    {"name": "Data 3", "date": "2024-01-10"},
    {"name": "Data 4", "date": "2024-01-20"},
    {"name": "Data 5", "date": "2024-01-25"}
]

# Endpoint to filter data by date range
@app.route('/search-data', methods=['POST'])
def search_data():
    request_data = request.json
    start_date = request_data['start_date']
    end_date = request_data['end_date']
    
    filtered_data = [item for item in data if start_date <= item['date'] <= end_date]
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
