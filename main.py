from helpers.search_tweets import twitter_response
from helpers.format_response import formatted_response
from helpers.connect_azure import connect_to_azure, azure_header
from helpers.az_generate_languages import generate_languages


def run():
    documents = formatted_response(twitter_response())
    cxn_props = connect_to_azure()
    az_results = generate_languages(headers=azure_header(), lang_url=cxn_props[0], docs=documents)
    for result in az_results['documents']:
        print(result)
        doc = next(item for item in documents['documents'] if item['id'] == result['id'])
        print(doc['text'])
        print(result['detectedLanguage']['name'])
        print('-------------------------------------')

if __name__ == '__main__':
    run()

