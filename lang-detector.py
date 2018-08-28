import os
import json
from google.cloud import translate
from tqdm import tqdm
import glob

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

    for d in tqdm(data):
        authors = d['authors']
        coutries = list(map(detect_language, authors))
        d['country'] = coutries

    return data


if __name__ == '__main__':
    input_files = glob.glob('data/ACL*.json')
    output_files = [f.split('.')[0]+'-labeled.json' for f in input_files]

    for input_file, output_file in zip(input_files, output_files):
        print(input_file)
        data = detect_language_from_json(input_file)

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4)
