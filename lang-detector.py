import os
import json
from google.cloud import translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './google-credentials.json'


def detect_language(text):
    """Detects the text's language."""
    translate_client = translate.Client()
    result = translate_client.detect_language(text)

    # print('Text: {}'.format(text))
    # print('Confidence: {}'.format(result['confidence']))
    # print('Language: {}'.format(result['language']))

    return result['language']


def detect_language_from_json(file_path):
    with open(file_path) as f:
        data = json.load(f)

    for d in data:
        authors = d['authors']
        coutries = list(map(detect_language, authors))
        d['country'] = coutries

    return data


if __name__ == '__main__':
    input_file_path = 'data/test.json'
    output_file_path = 'data/test_detected.json'

    data = detect_language_from_json(input_file_path)

    with open(output_file_path, 'w') as f:
        json.dump(data, f, indent=4)
