import requests 
import json
#import logging
class Config:
    # OpenAI API endpoint and key
    OPENAI_API_URL = "http://127.0.0.1:8000/"
    OPENAI_MODEL = 'whisper-1'
    OPENAI_API_KEY = "love1"
    
    
    
    # interact through HTTP protocal
    def transcribe(self, audio_data, prompt):
        with open(audio_data, "rb") as f:
            files = {"file": f}
            data = {"model": Config.OPENAI_MODEL, "prompt": prompt}
            headers = {"Authorization": f"Bearer {Config.OPENAI_API_KEY}"}
            response = requests.post(Config.OPENAI_API_URL,
                                     files=files,
                                     data=data, 
                                     headers=headers)
            
            #logger = logging.getLogger(__name__)
            #logger.warning(f"{response.json()}")
            response.raise_for_status()
            transcript = response.json()
    
            return transcript['text']

config = Config()

if __name__ == "__main__":
    prompt = "This is a test"
    audio_data ='test.wav'
    text = config.transcribe(audio_data, prompt)
    print(text)