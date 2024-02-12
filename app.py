from flask import Flask, request, jsonify
from flask_cors import CORS
from cuss_inspect import predict, predict_prob

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict_text():
    try:
        data = request.get_json(force=True)
        text = data['text']

        prediction = predict(text).tolist()  # Convert NumPy array to Python list
        probability = predict_prob(text).tolist()  # Convert NumPy array to Python list

        result = {
            'text': text,
            'prediction': prediction,
            'probability': probability
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
