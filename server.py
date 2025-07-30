from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)


@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    input_json = request.get_json()
    statement = input_json.get('text', '')
    result = emotion_detector(statement)
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response


if __name__ == '__main__':
    app.run()
