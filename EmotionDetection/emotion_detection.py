import requests
import json


def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    request_json = { "raw_document": { "text": text_to_analyse } }

    default_response_json = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }


    if not text_to_analyse:
        status_code = 400

    else:
        response = requests.post(url, headers=headers, json=request_json)
        status_code = response.status_code

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

    # Make sure status code is within 200 range i.e. 2xx (Succesful responses)
    if status_code == 400:
        return default_response_json, 400
    elif status_code // 100 != 2:
        return {'ERROR' : 'RESPONSE WAS NOT SUCCESSFUL'}, status_code


    return response_json, 200
