import config as c


def connect_to_azure():
    """
    Generate connection properties using credentials
    :return: a tuple containing all the variables needed to connect to the endpoint
    """
    language_api_url = f"{c.azure_credentials['endpoint']}text/analytics/v3.1/languages"
    sentiment_url = f"{c.azure_credentials['endpoint']}text/analytics/v3.1/sentiment"
    subscription_key = c.azure_credentials['key1']
    return language_api_url, sentiment_url, subscription_key


def azure_header():
    return {
        "Ocp-Apim-Subscription-Key": c.azure_credentials['key1']
    }