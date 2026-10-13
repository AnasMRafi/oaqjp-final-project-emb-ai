"""Root-level compatibility wrapper for emotion_detector.

This module provides backwards compatibility for code importing emotion_detector
directly from the root level rather than from the EmotionDetection package.
"""
from EmotionDetection.emotion_detection import emotion_detector

__all__ = ['emotion_detector']
