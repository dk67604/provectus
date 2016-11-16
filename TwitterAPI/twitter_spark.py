
from __future__ import print_function
import unicodecsv
from pyspark.sql import SQLContext, Row, SparkSession
from twitter_rest import OAuthHandler
import tweepy

##################################################
# Code snippet for intializing Spark context
#################################################
spark = SparkSession \
    .builder \
    .appName("Twitter") \
    .getOrCreate()
sc = spark.sparkContext;
sqlContext = SQLContext(sc)
#############################################################
#Method to handle tweet data from Twitter Rest API
##############################################################
def tweetdata(tweet_info):

    tweet_data = {'Id': None, 'CreatedAt': None, 'Country': None, 'Country_Code': None, 'Place': None,
                  'Retweetstatus': None,
                  'UsrFavouriteCount': 0, 'Text': None, 'Lang': None, 'Usrname': None, 'Usrid': 0, 'UsrLang': None,
                  'Usrlocation': None,
                  'UsrFollowersCount': 0, 'UsrFriendsCount': 0, 'UsrVerified': None, 'UsrCreatedat': None,
                  'UsrDescription': None,
                  'UsrGeoenabled': None, 'UsrStatusescount': 0, 'UsrTimezone': None, 'UsrUtcOffset': 0,
                  'Retweeted': None,
                  'Retweet_count': 0,'Error_Msg':None}
    oauth=OAuthHandler()
    temp=tweet_info.split(',')
    try:
        row_json=oauth.get_tweet_info(tweed_id=temp[0])
        user_data = row_json.user
        tweet_data['Id'] = row_json.id
        tweet_data['CreatedAt'] = row_json.created_at
        tweet_data['Country'] = 'None'
        tweet_data['Country_Code'] = 'None'
        tweet_data['Place'] = 'None'
        tweet_data['Retweetstatus'] = row_json.retweeted
        tweet_data['UsrFavouriteCount'] = user_data.favourites_count
        tweet_data['Text'] = "".join(row_json.text.splitlines())
        tweet_data['Lang'] = row_json.lang
        tweet_data['Usrname'] = user_data.screen_name
        tweet_data['Usrid'] = user_data.id
        tweet_data['UsrLang'] = user_data.lang
        tweet_data['Usrlocation'] = user_data.location
        tweet_data['UsrFollowersCount'] = user_data.followers_count
        tweet_data['UsrFriendsCount'] = user_data.friends_count
        tweet_data['UsrVerified'] = user_data.verified
        tweet_data['UsrCreatedat'] = user_data.created_at
        tweet_data['UsrDescription'] =  "".join(user_data.description.splitlines())
        tweet_data['UsrGeoenabled'] = user_data.geo_enabled
        tweet_data['UsrStatusescount'] = user_data.statuses_count
        tweet_data['UsrTimezone'] = user_data.time_zone
        tweet_data['UsrUtcOffset'] = user_data.utc_offset
        tweet_data['Retweeted'] = row_json.retweeted
        tweet_data['Retweet_count'] = row_json.retweet_count
        return tweet_data

    except tweepy.TweepError as e:
        tweet_data['Id']=temp[0]
        tweet_data['CreatedAt'] = 'None'
        tweet_data['Country'] = 'None'
        tweet_data['Country_Code'] = 'None'
        tweet_data['Place'] = 'None'
        tweet_data['Retweetstatus'] ='None'
        tweet_data['UsrFavouriteCount'] = 'None'
        tweet_data['Text'] = 'None'
        tweet_data['Lang'] ='None'
        tweet_data['Usrname'] = 'None'
        tweet_data['Usrid'] ='None'
        tweet_data['UsrLang'] = 'None'
        tweet_data['Usrlocation'] ='None'
        tweet_data['UsrFollowersCount'] ='None'
        tweet_data['UsrFriendsCount'] = 'None'
        tweet_data['UsrVerified'] = 'None'
        tweet_data['UsrCreatedat'] = 'None'
        tweet_data['UsrDescription'] = 'None'
        tweet_data['UsrGeoenabled'] ='None'
        tweet_data['UsrStatusescount'] = 'None'
        tweet_data['UsrTimezone'] ='None'
        tweet_data['UsrUtcOffset'] = 'None'
        tweet_data['Retweeted'] = 'None'
        tweet_data['Retweet_count'] = 'None'
        return tweet_data




#########################################################
#Method to handle writing tweet information into CSV file
#########################################################
def writetoCsv(fianl_data,writer):
    for dict in fianl_data:
        if dict['Text'] is not None:
            dict['Text']=dict['Text'].replace('\n'," ")
        else:
            dict['Text']='None'
        if dict['UsrDescription'] is not None:
            dict['UsrDescription']=dict['UsrDescription'].replace('\n'," ")
        else:
            dict['UsrDescription']='None'


        row=[dict['Id'],dict['CreatedAt'],dict['Country'],dict['Country_Code'],dict['Place'],
             dict['Retweetstatus'],dict['UsrFavouriteCount'],dict['Text'].encode("UTF-8").replace(',',' '),
             dict['Lang'] ,dict['Usrname'],dict['Usrid'],
             dict['UsrLang'],dict['Usrlocation'],
             dict['UsrFollowersCount'],dict['UsrFriendsCount'],dict['UsrVerified'],
             dict['UsrCreatedat'],dict['UsrDescription'].encode("UTF-8").replace(',',' '),dict['UsrGeoenabled'],dict['UsrStatusescount'],
             dict['UsrTimezone'],dict['UsrUtcOffset'] ,
             dict['Retweeted'],dict['Retweet_count']]

        writer.writerow(row)
    return True
################################################
# Driver method to call the required function
###############################################
def main():
    raw_data=sc.textFile("/home/dharamendra/Vaccine/vaccine02.csv")
    print ("File reading completed...")
    #header = raw_data.first()
    #raw_data_skip_header = raw_data.filter(lambda l: l!=header)
    row_rdd=raw_data.map(lambda x:x.encode('utf-8'))
    tweet_data=row_rdd.map(lambda x:tweetdata(x))
    final_data=tweet_data.collect()
    final_data_sorted=sorted(final_data, key=lambda x: (x['Id']))

    print ("Data fetched successfuly")
    header=["Id", "CreatedAt","Country","Country_Code","Place","RetweetedStatus", "UsrFavouriteCount","Text","Lang",
            "UsrName","UsrId","UsrLang","UsrLocation","UsrFollowersCount","UsrFriendsCount","UsrVerified","UsrCreatedAt",
            "UsrDescription","UsrGeoEnabled","UsrStatuesCount","UsrTimeZone","UsrUtcOffset","Retweeted","Retweet_Cont"]
    with open('/home/dharamendra/Vaccine/output_vaccine_2.csv', 'wb') as data_file:
        writer = unicodecsv.writer(data_file, encoding='utf-8')
        writer.writerow(header)
        writetoCsv(final_data_sorted,writer)

if __name__ == '__main__':
    main()
