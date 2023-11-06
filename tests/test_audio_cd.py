import unittest

from library.audio_cd import AudioCD

class TestAudioCD(unittest.TestCase):
    def test_create_audio_cd(self):
        audio_cd = AudioCD("Audio CD 1", "Artist 1", 1, 60)
        self.assertEqual(audio_cd.title, "Audio CD 1")
        self.assertEqual(audio_cd.duration, 60)

if __name__ == "__main__":
    unittest.main()