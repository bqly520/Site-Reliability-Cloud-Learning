# Implement a reddit web-scraper that analyzes if there's an effect between sub-reddit WallStreetBets vs. Stock Prices
# Specifically, we will be analyzing users who uses the word Bear vs. Bull to determine if the market
# will either move in an up-trend or down-trend because of the commonality of these words

# Importing sys is needed to externalize the secrets

import praw
import pprint
import datetime
import sys
sys.path.insert(1, '/Users/bryan/Documents/Configurations/reddit')
import redditconf

def getToken(): 
    reddit = praw.Reddit(client_id=redditconf.client_id[0],
                         client_secret=redditconf.client_secret[0],
                         user_agent=redditconf.user_agent[0])
    return reddit

def getTicker(tick):
    pass

# Sorts the top-level comments of a submission and returns an array with all of the comments
def sortComments(sort, num_comments):
    pass

# Counts keywords related to Call and Puts options
def countOptionKeywords():
    pass

# Calculating the stock trend by using 1 weeks worth of data and using variables like market open, close, and etc...
def calculateStockTrend():
    pass

# Compares the WSB trends versus the stock trends
def compareTrend():
    pass

# Including main so methods within this module can be reused
# pprint.pprint(vars(post)) can be used to display attributes of[Comment, Message, Redditor, Submission]
if __name__ == '__main__':
    # Retrieving lurker token
    reddit = getToken()

    hot_posts = reddit.subreddit('wallstreetbets').hot(limit=1)
    for post in hot_posts:
        url_post = post.url
        # Getting the submission object for the hottest reddit post on wallstreetbets
        submission = reddit.submission(url=url_post)
        print("Title of Reddit Post: " + submission.title)
        # A limit of 0 simply removes all MoreComments from the forest.
        submission.comments.replace_more(limit=0)
        submission.comment_sort = 'best'

        printComments = 4
        for top_level_comment in submission.comments:
            if printComments == 0:
                break
            else:
                printComments = printComments - 1
                print("Comment Message: " + top_level_comment.body)
                timestamp = datetime.datetime.fromtimestamp(top_level_comment.score)
                print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
                print("Number of upvotes: " + str(top_level_comment.score))
