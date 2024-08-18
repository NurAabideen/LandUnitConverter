from flask import Flask, render_template, request, jsonify
from conversion_data import conversion_data  # Use the same conversion data as before

app = Flask(__name__)

@app.route('/')
def index():
    units = list(set([unit for pair in conversion_data.keys() for unit in pair]))
    return render_template('index.html', units=units)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    value = float(data['value'])
    unit_from = data['unit_from']
    unit_to = data['unit_to']

    if unit_from != unit_to:
        conversion_factor = conversion_data.get((unit_from, unit_to)) or (1 / conversion_data.get((unit_to, unit_from)))
        result = value * conversion_factor
    else:
        result = value

    return jsonify({'result': round(result, 2)})

if __name__ == '__main__':
    app.run(debug=True)
