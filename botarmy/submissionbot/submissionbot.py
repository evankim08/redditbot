import praw
import random
import time
import datetime
from praw.reddit import Subreddit

# ----- EXTRA CREDIT 4 : MAKE YOUR BOT CREATE NEW SUBMISSION POSTS INSTEAD OF JUST NEW COMMENTS -----

reddit = praw.Reddit('bluebot')
subreddit1 = reddit.subreddit('Showerthoughts')
subreddit2 = reddit.subreddit('LifeProTips')
bottown = reddit.subreddit('BotTown2')
reddit.validate_on_submit = True

selfpostcount = 0
urlpostcount = 0

subreddit1list = []
subreddit2list = []
bottownlist = []

for sub in subreddit1.top(limit=1000):
    subreddit1list.append(sub)

for sub in subreddit2.top(limit=1000):
    subreddit2list.append(sub)

for sub in bottown.new(limit = None):
    bottownlist.append(sub)


while True:
    print()
    decision = random.choice([0,1])

    if decision == 0:
        submission = random.choice(subreddit1list)
  
        if submission in bottownlist:
            print('Duplicate Submission!')
            time.sleep(5)
            print('Beginning new iteration...')
            continue

        else:
            print('New URL Post!')
            urlpostcount += 1
            print('URL Post Count =', urlpostcount)
            
            bottown.submit(title=submission.title, url=submission.url)
            print('Submission Title = ', submission.title)
            time.sleep(300)
 
    elif decision == 1:
        submission = random.choice(subreddit2list)

        if submission in bottownlist:
            print('Duplicate Submission!')
            time.sleep(5)
            print('Beginning new iteration...')
            continue

        else:
            print('New Self Post!')
            selfpostcount += 1
            print('Self-Post Count =', selfpostcount)

            bottown.submit(title=submission.title,selftext=submission.selftext)
            print('Submission Title = ', submission.title)
            time.sleep(300)

    #print('Self-Post Count =', selfpostcount)
    #print('URL Post Count =', urlpostcount)
