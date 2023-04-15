from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import requests 
import json
import torch

#from rest_framework.decorators import api_view

import whisper
from whisper.tokenizer import get_tokenizer


model_name = "tiny"
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model(model_name).to(device)

@csrf_exempt
def transcribe(request):
    
    '''  
    assert result["language"] == "en"
    assert result["text"] == "".join([s["text"] for s in result["segments"]])
    '''
    
    audio_file = request.FILES.get('file')
    with open('api.wav', 'wb') as f:
        for chunk in audio_file.chunks():
            f.write(chunk)
    prompt = request.POST.get('prompt')
    result = model.transcribe(
        "api.wav" , prompt=prompt, temperature=0.0, word_timestamps=True
    )

    # Return the transcribed text as a JSON response
    return JsonResponse({'text': result['text']}, status=200)