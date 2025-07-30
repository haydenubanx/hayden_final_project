import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    request_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=request_json)


    data = json.loads(response.text)
    emotions = data['emotionPredictions'][0]['emotion']

    response_json = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }


    return response_json
