import praw
import prawcore
import random
import time
import datetime
from textblob import TextBlob
from praw.reddit import Subreddit

# ----- EXTRA CREDIT 7 : HAVE YOUR BOT UPVOTE ANY COMMENT OR SUBMISSION THAT MENTIONS YOUR FAVORITE CANDIDATE ----- 

# ----- CONNECT TO REDDIT -----
reddit = praw.Reddit('bitterbot')

# ----- SELECT A "HOME" SUBMISSION IN THE r/BotTown2 SUBREDDIT -----
url = 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=url)
subreddit = reddit.subreddit('BotTown2')

words = ['arnold','schwarzenegger']

upvotecount = 0
downvotecount = 0
subupvotecount = 0
subdownvotecount = 0

while True:

    print()
    print('New Iteration At:',datetime.datetime.now())
    print('Current Submission =',submission.title)

# ----- UPVOTE/DOWNVOTE PROGRAM FOR SUBMISSIONS -----

    blob = TextBlob(str(submission.selftext))
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    for word in words:   
        if word in submission.title.lower() and polarity > 0.5:
            submission.upvote()
            print('Submission Has Been Upvoted via TextBlob')
            subupvotecount += 1
            break
        
        if word in submission.title.lower() and subjectivity > 0:
            submission.upvote()
            print('Submission Has Been Upvoted via TextBlob')
            subupvotecount += 1
            break

        if word in submission.title.lower() and polarity < 0.5:
            submission.downvote()
            print('Submission Has Been Downvoted via TextBlob')
            subdownvotecount += 1
            break

        if word in submission.title.lower() and subjectivity < 0:
            submission.downvote()
            print('Submission Has Been Downvoted via TextBlob')
            subdownvotecount += 1
            break

        if 'trump' in submission.title.lower():
            submission.downvote()
            print('Submission Has Been Downvoted via TextBlob due to alternative politician exposure.')
            subdownvotecount += 1
            break

        if 'biden' in submission.title.lower():
            submission.downvote()
            print('Submission Has Been Downvoted via TextBlob due to alternative politican exposure.')
            subdownvotecount += 1
            break
        
        else:
            print('The key word(s) could not be found in this submission\'s title.')

# ----- UPVOTE/DOWNVOTE PROGRAM FOR COMMENTS -----

    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    not_my_comments = []

    for comment in all_comments:
        if str(comment.author) != 'brokenbitterbottle':
            not_my_comments.append(comment)

    for comment in not_my_comments:

        blob = TextBlob(str(comment.body))
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        for word in words:

            if word in comment.body.lower() and polarity > 0.5:
                comment.upvote()
                comment.refresh
                print('Comment Has Been Upvoted via TextBlob')
                upvotecount += 1
                break

            if word in comment.body.lower() and subjectivity > 0:
                comment.upvote()
                comment.refresh
                print('Comment Has Been Upvoted via TextBlob')
                upvotecount += 1
                break
            
            if word in comment.body.lower() and polarity < 0.5:
                comment.downvote()
                comment.refresh()
                print('Comment Has Been Downvoted via TextBlob')
                downvotecount += 1
                break

            if word in comment.body.lower() and subjectivity < 0:
                comment.downvote()
                comment.refresh()
                print('Comment Has Been Downvoted via TextBlob')
                downvotecount += 1
                break

            if 'trump' in comment.body.lower():
                comment.downvote()
                print('Comment Has Been Downvoted via TextBlob due to alternative politician exposure.')
                downvotecount += 1
                break
            
            if 'biden' in submission.title.lower():
                comment.downvote()
                print('Comment Has Been Downvoted via TextBlob due to alternative politican exposure.')
                downvotecount += 1
                break

            else:
                print('The key word(s) could not be found in this comment.')
    
    print()
    print('Current Comment Upvote Count =', upvotecount)
    print('Current Comment Downvote Count =', downvotecount)
    print('Current Submission Upvote Count =' , subupvotecount)
    print('Current Submission Downvote Count =' , subdownvotecount)
    print()

    hotsubmissions = []
    for entry in reddit.subreddit('BotTown2').top(limit=250):
        hotsubmissions.append(entry)
    submission = random.choice(hotsubmissions)

    print('Next Submission Title =', submission.title)
    print()
    print('taking a breath before the next iteration...')
    time.sleep(20)