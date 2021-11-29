# redditbot

For this project, I used Python and the PRAW API to create multiple Reddit bots. These bots were programmed to post comments supporting Arnold Schwarzenegger as a politician, primarily as a light-hearted joke. 



## Favorite Thread

My favorite [thread](https://old.reddit.com/r/BotTown2/comments/r2egby/steve_bannon_and_reince_priebus_push_audit_of/hm4l3at/) including my bot was very short, and included an interaction with another bot that converted the units in my comment:

<img width="869" alt="Screen Shot 2021-11-27 at 11 32 41 PM" src="https://user-images.githubusercontent.com/70280666/143733832-0969fc23-b070-4f13-af9b-d4b18f6aedc8.png">

I liked this interaction because at a basic level, it shows how different bots can take elements of comments generated by other bots in order to continue a conversation somewhat logically. In a way, it reminded me of real-life conversation, where humans often take a part of someone's statement and use it to drive or redirect the conversation. Also, it was entertaining to imagine Arnold Schwarzenegger, one of the greatest bodybuilders of all time, lifting 200 pounds of colorful pizza blankets.

## Output

Below are the outputs from running `bot_counter.py` for each of my bots:

1. **Bot Name:** _brokenbrownbottle_
```
evankim@Evans-MBP-2 brownbot % python3 bot_counter.py --username brokenbrownbottle
len(comments)= 622
len(top_level_comments)= 194
len(replies)= 428
len(valid_top_level_comments)= 192
len(not_self_replies)= 420
len(valid_replies)= 321
========================================
valid_comments= 513
========================================
```

2. **Bot Name:** _brokenburgundybottle_
```
evankim@Evans-MBP-2 burgundybot % python3 bot_counter.py --username brokenburgundybottle
len(comments)= 683
len(top_level_comments)= 197
len(replies)= 486
len(valid_top_level_comments)= 195
len(not_self_replies)= 482
len(valid_replies)= 385
========================================
valid_comments= 580
========================================
```

3. **Bot Name:** _brokenbrassbottle_
```
evankim@Evans-MBP-2 brassbot % python3 bot_counter.py --username brokenbrassbottle
len(comments)= 647
len(top_level_comments)= 188
len(replies)= 459
len(valid_top_level_comments)= 186
len(not_self_replies)= 451
len(valid_replies)= 356
========================================
valid_comments= 542
========================================
```

4. **Bot Name:** _brokenblackbottle_
```
evankim@Evans-MBP-2 blackbot % python3 bot_counter.py --username brokenblackbottle
len(comments)= 710
len(top_level_comments)= 227
len(replies)= 483
len(valid_top_level_comments)= 225
len(not_self_replies)= 482
len(valid_replies)= 377
========================================
valid_comments= 602
========================================
```

5. **Bot Name:** _brokenburntbottle_
```
evankim@Evans-MBP-2 burntbot % python3 bot_counter.py --username brokenburntbottle
len(comments)= 606
len(top_level_comments)= 168
len(replies)= 438
len(valid_top_level_comments)= 166
len(not_self_replies)= 433
len(valid_replies)= 346
========================================
valid_comments= 512
========================================
```
6. **Bot Name:** _brokenbeigebottle_
```
evankim@Evans-MBP-2 beigebot % python3 bot_counter.py --username brokenbeigebottle
len(comments)= 683
len(top_level_comments)= 199
len(replies)= 484
len(valid_top_level_comments)= 199
len(not_self_replies)= 477
len(valid_replies)= 389
========================================
valid_comments= 588
========================================
```

**Extra Credit #4 :** Below is the output of running `submissionbot.py`. This bot created new submission posts instead of just new comments. These submissions were pulled from _r/Showerthoughts_ and _r/LifeProTips_ and posted into the class subreddit _r/BotTown2_. By the final iteration, the bot had generated 278 unique submissions, some of which were self-posts and some of which were URL posts, as desired. 

```
Self-Post Count = 142
URL Post Count = 136
```

**Extra Credit #5 :** As seen above, I have created an army of 5+ reddit bots, each posting similar comments with different `praw.ini` files. Each bot posted 500+ valid comments, as desired.


**Extra Credit #6 :** Below is the output of running the final iteration of `topcommentbot.py` . This bot replies to the most highly upvoted comment that it hasn't already replied to, without ever replying to itself. 

```
Top Comment Reply Count = 134
```

**Extra Credit #7 :** Below is the output from running the final iteration of my `upvotebot.py` program, which used _TextBlob Sentiment Analysis_ to upvote any comment or submission that mentioned _Arnold_ or _Schwarzenegger_ with positive sentiment, and downvoted those with negative sentiment. Since there were not many submissions that mentioned Arnold Schwarzenegger, I also wrote the program so that it downvoted any mention of either _Trump_ or _Biden_. By the final iteration of the program, there were 500+ comments and 100+ submissions upvoted or downvoted, as desired. 

```
Current Comment Upvote Count = 8277
Current Comment Downvote Count = 22753
Current Submission Upvote Count = 0
Current Submission Downvote Count = 135
```

## Grading

**Required Tasks**

* *Task 1 :* Completed `bot.py` file | +18 Points |
* *Task 2 :* Completed GitHub repository | +2 Points |

**Optional Tasks**

* *Task 1 :* Getting at least 100 valid comments posted | +2 Points |
* *Task 2 :* Getting at least 500 valid comments posted | +2 Points |
* <s>*Task 3 :* Getting at least 1000 valid comments posted | +2 Points |</s>
* *Task 4 :* Making your bot create 200+ new submissions | +2 Points |
* *Task 5 :* Create an "army" of 5 bots that post 500+ valid comments each | +2 Points |
* *Task 6 :* Make your bot reply to the most highly upvoted comment | +2 Points |
  * *Additional:* Use the _TextBlob_ sentiment analysis library | +2 Points |
* *Task 7 :* Have your bot upvote any comment or submission that mentions your favorite candidate. | +2 Points |
* <s>*Task 8 :* Use a more sophisticated algorithm for generating the text of your comments | +5 Points |</s>

**Total Points :** 34/30
