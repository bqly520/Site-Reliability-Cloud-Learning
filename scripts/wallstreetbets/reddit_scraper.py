# Implement a reddit web-scraper that analyzes if there's an effect between sub-reddit WallStreetBets vs. Stock Prices
# Specifically, we will be analyzing users who uses the word Bear vs. Bull to determine if the market
# will either move in an up-trend or down-trend because of the commonality of these words

# Importing sys is needed to externalize the secrets

import praw
import pprint
import sys
sys.path.insert(1, '/Users/bryan/Documents/Configurations/reddit')
import redditconf

def retrieveToken (): 
    reddit = praw.Reddit(client_id=redditconf.client_id[0],
                         client_secret=redditconf.client_secret[0],
                         user_agent=redditconf.user_agent[0])
    return reddit

# Including main so methods within this module can be reused
# pprint.pprint(vars(post)) can be used to display attributes of[Comment, Message, Redditor, Submission]
if __name__ == '__main__':
    # Retrieving lurker token
    reddit = retrieveToken()

    hot_posts = reddit.subreddit('wallstreetbets').hot(limit=1)
    for post in hot_posts:
        url_post = post.url
        submission = reddit.submission(url=url_post)
        for top_level_comment in submission.comments:
            print(top_level_comment.body)