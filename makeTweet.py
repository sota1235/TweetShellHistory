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
tweet = ""
f = open("./tweet.txt", "w")
for key, val in tweets.items():
    tweet += key + "を" + str(val) + "回,"
tweet = tweet[:-1] + "実行した。"
f.write(tweet)
f.close()
