# coding: Shift_JIS

from base64 import b64encode
from sys import argv
import json
import requests

ENDPOINT_URL = 'https://vision.googleapis.com/v1/images:annotate'
API_KEY = 'AIzaSyDliLYqFoAoCsQmSGaydW6VvtnA_m_05ws'

if __name__ == '__main__':
    image_filenames = argv[1:]

    img_requests = []
    for imgname in image_filenames:
        with open(imgname, 'rb') as f:
            ctxt = b64encode(f.read()).decode()
            img_requests.append({
                    'image': {'content': ctxt},
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': 5
                    }]
            })

    response = requests.post(ENDPOINT_URL,
                             data=json.dumps({"requests": img_requests}).encode(),
                             params={'key': API_KEY},
                             headers={'Content-Type': 'application/json'})

    for idx, resp in enumerate(response.json()['responses']):
        print(json.dumps(resp, indent=2))
