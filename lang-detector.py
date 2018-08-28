import os
from google.cloud import translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './google-credentials.json'


def detect_language(text):
    """Detects the text's language."""
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    print('Text: {}'.format(text))
    print('Confidence: {}'.format(result['confidence']))
    print('Language: {}'.format(result['language']))


if __name__ == '__main__':
    name = 'Ryota Yamada'
    detect_language(name)
