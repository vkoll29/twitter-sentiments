import requests


def generate_languages(headers, lang_url, docs):
    try:
        response = requests.post(lang_url, headers=headers, json=docs)
        return response.json()
    except Exception as e:
        print(f'Exception: {e}')