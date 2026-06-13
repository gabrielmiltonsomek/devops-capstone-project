"""
Unit Tests for Emotion Detection Module
Tests emotion_detector function with various inputs
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector function"""

    def test_emotion_detector_joy(self):
        """Test that joyful text returns joy as dominant emotion"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        """Test that angry text returns anger as dominant emotion"""
        result = emotion_detector("I am really angry about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        """Test that disgusting text returns disgust as dominant emotion"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_detector_sadness(self):
        """Test that sad text returns sadness as dominant emotion"""
        result = emotion_detector("I am really sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        """Test that fearful text returns fear as dominant emotion"""
        result = emotion_detector("I am really scared and afraid")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_detector_blank_input(self):
        """Test that blank input returns None for all fields"""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])


if __name__ == '__main__':
    unittest.main()
