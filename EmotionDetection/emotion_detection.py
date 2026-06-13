"""
Emotion Detection module using Watson NLP library.
"""
import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the provided text using Watson NLP.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion
    """
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime'
           '.nlp.v1/NlpService/EmotionPredict')

    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    body = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=body, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions_predicted = (
        formatted_response['emotionPredictions'][0]['emotion']
    )

    anger_score = emotions_predicted['anger']
    disgust_score = emotions_predicted['disgust']
    fear_score = emotions_predicted['fear']
    joy_score = emotions_predicted['joy']
    sadness_score = emotions_predicted['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
