import requests
import config as c

bearer = c.twitter_credentials['bearer_token']
search_url = "https://api.twitter.com/2/tweets/search/recent"


def bearer_oauth(r):
    r.headers['Authorization'] = f'Bearer {bearer}'
    r.headers['User-Agent'] = 'v2RecentSearchPython'
    return r


def get_params():
    # the tweet.fields dictionary is where you specify the details of the tweet needed.
    # in this case, I'm retrieving the tweets date and attachments, if any.
    return {
        'query': '(excel OR MS Excel OR Microsoft Excel) -is:retweet lang:en',
        'tweet.fields': 'created_at,attachments',
        'max_results': 10,
        'next_token': {},
        # '-is': 'replies,retweets',
        'expansions': 'attachments.media_keys',
        'media.fields': 'url'

    }


# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
# query_params = {
#     'query': 'excel OR MS Excel OR Microsoft Excel',
#     'tweet.fields': 'created_at,author_id',
#     'max_results': 100
# }


def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def display_results(tweets):
    for tweet in tweets['data']:
        print(tweet['text'])
        print('------------------------------------------------------------------------')


def twitter_response():
    params = get_params()
    try:
        json_response = connect_to_endpoint(search_url, params)
        # display_results(json_response)
        return json_response
    except Exception as e:
        print(f'Exception: {e}')

# if __name__ == "__main__":
#     run()
