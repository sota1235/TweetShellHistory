#!/usb/bin/python

###
#
# その日使ったコマンドをTweet
#
###

import datetime

# 今日の日付
tmp = str(datetime.datetime.today())
date = "/".join([tmp[5:7], tmp[8:10], tmp[0:4]])

# commands
tweets = {}

# open command and make tweets
f = open("./history", "r")
for line in f:
    if line.split()[1] == date:
        command = line.split()[3]
        # いくつかのケースを弾く
        blackList = ["sota1235", "./a.out"]
        if command in blackList: continue
        # 配列に追加
        if command in tweets:
            tweets[command] += 1
        else:
            tweets[command] = 1
f.close()

# write tweets to tweet.txt
tweet = "今日は"
c = 0 # tweetするコマンド数
f = open("./tweet.txt", "w")
for key, val in sorted(tweets.items(), key=lambda x:x[1], reverse=True):
    tweet += key + "を" + str(val) + "回、"
    c += 1
    if c == 13: break
tweet = tweet[:-1] + "実行した。"
f.write(tweet)
f.close()
