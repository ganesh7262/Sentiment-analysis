import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAAOabQEAAAAAQDoJtk%2FE5Z%2Fp%2BxaMck%2FVofm1o04%3DIxZQW8LNNDU7FGWWYA6hi6anIq7FdLDbY9j7B0MbzwyeL9BuHU'

# search_url = "https://api.twitter.com/2/tweets/search/recent"
search_url="https://api.twitter.com/2/tweets/search/all"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
def params_(query):
    return {'query': f'{query} -is%3Aretweet' +'&max_results=100' + " -filter:retweets"}
# query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main(query):
    params=params_(query)
    json_response = connect_to_endpoint(search_url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    query=input('Enter the tag: ')
    while True:
        main(query)