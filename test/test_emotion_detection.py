from EmotionDetection.emotion_detection import emotion_detector
import unittest
import json



class TestEmotionDetection(unittest.TestCase):

    def test_for_joy(self):
        input_text = "I am glad this happened"

        response = emotion_detector(input_text)

        dominant_emotion = response['dominant_emotion']

        self.assertEquals(dominant_emotion, "joy")


    def test_for_anger(self):
        input_text = "I am really mad about this"

        response = emotion_detector(input_text)

        dominant_emotion = response['dominant_emotion']

        self.assertEquals(dominant_emotion, "anger")


    def test_for_disgust(self):
        input_text = "I feel disgusted just hearing about this"

        response = emotion_detector(input_text)

        dominant_emotion = response['dominant_emotion']

        self.assertEquals(dominant_emotion, "disgust")

    def test_for_sadness(self):
        input_text = "I am so sad about this"

        response = emotion_detector(input_text)

        dominant_emotion = response['dominant_emotion']

        self.assertEquals(dominant_emotion, "sadness")

    def test_for_fear(self):
        input_text = "I am really afraid that this will happen"

        response = emotion_detector(input_text)

        dominant_emotion = response['dominant_emotion']

        self.assertEquals(dominant_emotion, "fear")