from flask import Flask, request
import json
import Score
import os

app = Flask(__name__)

@app.route("/get-score", methods=['POST'])
def get_score():
    data = json.loads(request.data)
    string = data['string']
    score = Score.calculate_score(string)
    return json.dumps({
        'success': True,
        'score': score
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))