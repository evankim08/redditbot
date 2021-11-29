import praw
import random
import time
import datetime
from praw.reddit import Subreddit

# ----- COPY YOUR generate_function FUNCTION FROM THE MADLIBS ASSIGNMENT -----
madlibs = [

    'Arnold Schwarzenegger should run for [PRESIDENT] by [2024]. Then, he can [LEAD] America to the gym, and we will all become [BUFF]. As anyone knows, that would be [GREAT] for the economy.' ,

    'Arnold Schwarzenegger\'s last name is [HARD] to spell, that\'s true. But I would [CHOOSE] him to [REPRESENT] me in government rather than a [CANDIDATE] who has never [BENCHED 500 POUNDS] before.',

    'Arnold is a [FANTASTIC] actor. Haven\'t you seen [TERMINATOR]?  What makes you [BELIEVE] he [DOESN\'T DESERVE] another [CHANCE] in office? After all, politicians are [FANTASTIC] actors!',

    'From his time as governor of California, Arnold\'s [ACHIEVEMENTS] included [VICTORIES] on [ISSUES] regarding [ENVIRONMENTAL PROTECTION]. More importantly, however, I loved him in [TERMINATOR]. That\'s why I\'m [SUPPORTING] any future campaign for office.',

    'To be honest, I would [CHOOSE] an actor in office than a [CLOWN]. We have had a [DEPRESSINGLY] high number of those already. That\'s why I\'m [SUPPORTING] Arnold. There is no valid [REASON] for why you wouldn\'t vote for him if he runs again. It\'s Arnold Schwarzenegger!',

    'Arnold would be a [TERRIFIC] candidate for office. Think about how [COMPREHENSIVE] his workout plans were. Then, [CONVERT] that skill for [PUBLIC POLICY]. At the very least, maybe we could get free [LA FITNESS] memberships.'

    ]

replacements = {

    'PRESIDENT' : ['President', 'public office', 'the Presidency', 'national office'],
    '2024' : ['2028','2032','2036'],
    'LEAD' : ['lead', 'guide','steer','shepard','direct','usher'],
    'BUFF' : ['buff','fit','muscled','jacked'],
    'GREAT' : ['great','good','favorable','excellent','desirable','advantageous'],

    'HARD' : ['difficult', 'hard','troublesome','cumbersome','inconvenient'],
    'CHOOSE' : ['choose','elect for','prefer', 'opt for','rather have'],
    'REPRESENT' : ['represent', 'serve my interests','speak for my interests'],
    'CANDIDATE' : ['candidate', 'contender','nominee','governor'],
    'BENCHED 500 POUNDS' : ['benched 500 pounds', 'deadlifted 710 pounds','squatted 545 pounds','curled 200 pounds'],

    'FANTASTIC' : ['fantastic','phenomenal','talented','sensational','superb','marvelous','great','quality','convincing'],
    'TERMINATOR' : ['Terminator','Predator','Commando','Conan the Barbarian', 'The Expendables','Conan the Destroyer','Sabotage','Aftermath','The Last Stand'],
    'BELIEVE' : ['believe','think','suppose','feel'],
    'DOESN\'T DESERVE' : ['doesn\'t deserve', 'shouldn\'t have','is undeserving of','is unsuitable for','is unfit for','is not fit for'],
    'CHANCE' : ['chance','opportunity','try','round','term','session','cycle'],

    'ACHIEVEMENTS' : ['achievements','accomplishments','successes','highlights'],
    'VICTORIES' : ['victories','triumphs','progress','making headway'],
    'ISSUES' : ['issues','matters','affairs','subjects','topics','problems'],
    'ENVIRONMENTAL PROTECTION' : ['environmental protection','reducing greenhouse-gas emissions','the redistricting processes', 'equal educational opportunities','climate change'],
    'SUPPORTING' : ['supporting','backing','approving of','endorsing'],

    'CLOWN' : ['clown','buffoon','fool','joke'],
    'DEPRESSINGLY' : ['depressingly','unbelievably','distressingly','extremely','terribly','disturbingly','dreadfully','awfully','laughably'],
    'REASON' : ['reason','rationale','justification','explanation','rationalization','reasoning'],

    'COMPREHENSIVE' : ['comprehensive','complete','extensive','thorough','broad','exhaustive','detailed'],
    'TERRIFIC' : ['terrific','phenomenal','great','good','favorable','superb','desirable'],
    'PUBLIC POLICY' : ['public policy','politics','political strategy','administrative planning'],
    'CONVERT' : ['convert','translate','transform','adapt','remodel'],
    'LA FITNESS' : ['LA Fitness','Planet Fitness','24 Hour Fitness','Gold\'s Gym','Anytime Fitness']

    }

def generate_comment():
    x = random.choice(madlibs)
    for key in replacements.keys():
        x = x.replace('['+ key + ']', random.choice(replacements[key]))
    return x

# ----- CONNECT TO REDDIT -----
reddit = praw.Reddit('burgundybot')

# ----- SELECT A "HOME" SUBMISSION IN THE r/BotTown SUBREDDIT -----
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r0ynz0/test_submission/'
submission = reddit.submission(url=submission_url)

# ----- EACH ITERATION OF THIS LOOP POSTS A SINGLE COMMENT -> THIS IS A DAEMON -----
while True:

    # ----- INFORMATIVE OUTPUT -----
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # ----- TASK 0 : GET LIST OF ALL COMMENTS IN SUBMISSION -----
    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    print('Total # of Comments=',len(all_comments))

    # ----- TASK 1 : FILTER all_comments TO REMOVE COMMENTS GENERATED BY YOUR BOT -----
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'brokenburgundybottle':
            not_my_comments.append(comment)

    print('Total # of Comments That Aren\'t Mine =',len(not_my_comments))

    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented = ', has_not_commented)

    # ----- TASK 2 : IF NO COMMENT HAS BEEN MADE IN THREAD, POST A TOP-LEVEL COMMENT -----
    if has_not_commented:
        text = generate_comment()
        submission.reply(text)

    # ----- TASK 3 : FILTER THE not_my_comments LIST TO ALSO REMOVE COMMENTS ALREADY REPLIED TO -----
    
    else:
        comments_without_replies = []
        for comment in not_my_comments:
                for reply in comment.replies:
                    if str(reply.author) != 'brokenburgundybottle':
                        comments_without_replies.append(comment)
                    else:   
                        continue
            
        print('Total # of Comments Without My Replies =',len(comments_without_replies))

    # ----- TASK 4 : RANDOMLY SELECT A COMMENT FROM comments_without_replies LIST TO REPLY TO -----

    #comment = reddit.comment(id="dxolpyc")
    #comment.reply("reply")

    text = generate_comment()
    try:
        comment = random.choice(comments_without_replies)
        comment.reply(text)
        
    except praw.exceptions.APIException:
        print('This comment has been deleted and will not be replied to.')
    except IndexError:
        pass

    # ----- TASK 5 : SELECT A NEW SUBMISSION FROM THE 5 HOTTEST SUBMISSIONS FOR THE NEXT LOOP ITERATION -----
    hotsubmissions = []
    for entry in reddit.subreddit('BotTown2').hot(limit=5):
        hotsubmissions.append(entry)
    submission = random.choice(hotsubmissions)
    print('Next Submission Title =', submission.title)

    time.sleep(300)