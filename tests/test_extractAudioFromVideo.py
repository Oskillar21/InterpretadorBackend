import unittest
import os
from services import audioExtractor

class TestAudioExtractor(unittest.TestCase):
    def test_extract_audio_from_video_success(self):
        # Video de ejemplo 
        video_path = "tests/assets/prueba.mp4"
        output_dir = "tests/temp"

        if not os.path.exists(video_path):
            self.skipTest("Video de ejemplo no disponible.")

        audio_path = audioExtractor.extractAudioFromVideo(video_path, output_dir)
        self.assertTrue(os.path.exists(audio_path))
        self.assertTrue(audio_path.endswith(".mp3"))

        # Limpieza
        os.remove(audio_path)
        os.rmdir(output_dir)

    def test_extract_audio_from_invalid_video(self):
        with self.assertRaises(Exception):
            audioExtractor.extractAudioFromVideo("archivo_invalido.mp4")