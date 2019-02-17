import tweepy

consumer_key = "mGRAQmAI1HASoWtgf5H5yD4Jd"
consumer_secret = "2k7CpUpArBTejF4UgEmkHfYUgSwhywKiBrEfATlZmgACA5sicr"
access_key = "775671340451921925-zu5xRPYnKZUV7zcKRhGnK5zGZzGC19m"
access_secret = "DqitlGs2NW79ewGaBvda3lNGEJiVrqrARnrp8EffmuZFf"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

u1= input("Give 1st user's username")
u2 = input("Give 2nd user's username")


##word count part .....

user1_status=api.user_timeline(screen_name=u1,count=10, tweet_mode="extended")
user2_status=api.user_timeline(screen_name=u2, count=10, tweet_mode="extended")


user1_word_counter=0
temp1=0
for tweet in user1_status:
  #print (tweet.full_text.split()) >>> print splited list
  #print (len(tweet.full_text.split())) >>> print total words in each status
  temp1=len(tweet.full_text.split())
  user1_word_counter = user1_word_counter + temp1

print(u1+ " total words in last 10 statuses: "+str(user1_word_counter)) #>> print total words for 10 statuses of user1

user2_word_counter=0
temp2=0
for tweet in user2_status:
    #print (tweet.full_text.split()) >>> print splited list
    #print (len(tweet.full_text.split())) >>> print total words in each status
    temp2=len(tweet.full_text.split())
    user2_word_counter= user2_word_counter + temp2

print(u2+" total words in last 10 statuses: " +str(user2_word_counter)) #>> print total words for 10 statuses of user2

##followers count part...

user1_followers=api.get_user(u1)
user2_followers=api.get_user(u2)

print(u1+" total followers: "+str(user1_followers.followers_count))
print(u2+ " total followers: "+str(user2_followers.followers_count))

final1=user1_word_counter*user1_followers.followers_count
final2=user2_word_counter*user2_followers.followers_count

if final1>final2:
    print("Biggest sum is user's: "+u1+" and it's: "+str(final1))
else:
    print("Biggest sum is user's: "+u2+" and it's: "+str(final2))
