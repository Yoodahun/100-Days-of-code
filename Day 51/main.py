from twitterBot import  InternetSpeedTwitterBot


PROMISED_DOWN = 350
PROMISED_UP = 10
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""

twitter_bot = InternetSpeedTwitterBot()

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider(TWITTER_USERNAME, TWITTER_PASSWORD)
