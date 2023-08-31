import torch
from pydub import AudioSegment
import simpleaudio as sa
import tempfile

class Text2Speech:
    def __init__(self, engine='coqui'):
        self.engine = engine

        if self.engine == 'coqui':
            # Set default model
            self.tts_model = "tts_models/en/ljspeech/glow-tts"

    def set_engine(self, engine):
        self.engine = engine

    def play_audio(self, file_path):
        audio = AudioSegment.from_file(file_path)
    
        # Export audio to a temporary WAV file
        temp_wav = tempfile.NamedTemporaryFile(delete=False)
        temp_wav.close()
        audio.export(temp_wav.name, format='wav')
        
        # Play the temporary WAV file
        wave_obj = sa.WaveObject.from_wave_file(temp_wav.name)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        
    def convert_text_to_speech(self, text):
        if self.engine == 'coqui':
            return self._convert_text_to_speech_coqui(text)

        # Add more elif conditions to support additional engines

    def _convert_text_to_speech_coqui(self, text):
        from TTS.api import TTS

        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Init TTS with the target model name
        tts = TTS(model_name=self.tts_model).to(device)

        wav_file_path = 'output.wav'
        
        tts.tts_to_file(text=text, file_path=wav_file_path)

        return wav_file_path
    
if __name__ == "__main__":
    tts = Text2Speech()
    tts.convert_text_to_speech("Hello, I'm Sorena V Robot, Developed at CAST in iran. I'm fifth generation of eranian Humanoid Robots, Do you have any quesstion from me?")
    tts.play_audio("output.wav")
    