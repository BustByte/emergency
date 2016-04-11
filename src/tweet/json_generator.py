from tweet.tweet import Tweet
from position.position import Position

class Json:

    @classmethod
    def generate_json(cls, tweets):
        json_tweets = []
        for tweet in tweets:
            json_tweet = {
                'id': tweet.id
            }
            if tweet.position.latitude != None and tweet.position.longitude != None:
                json_tweet['position'] = {
                    'lat': float(tweet.position.latitude),
                    'lng': float(tweet.position.longitude)
                }
            json_tweets.append(json_tweet)

        return json_tweets
