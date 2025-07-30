from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    input_json = request.get_json()
    statement = input_json.get('text', '')
    result, status_code = emotion_detector(statement)

    if status_code == 200:
        response = jsonify(
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
        ), 200
    elif status_code == 400 or result['dominant_emotion'] == None:
        response =  jsonify({"message": "Invalid text! Please try again."}), 400
    else:
        response = jsonify({"message": "INTERNAL SERVER ERROR"}), 500
    return response


if __name__ == '__main__':
    app.run()
