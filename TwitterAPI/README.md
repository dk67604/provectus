
Features of the respository

1) Using Beautiful Soup python, extracted all the tweets #CDCgrandrounds. Used scraping method to load the data until all the tweet get fetched.
2) Using Tweepy package, created OAuth Handler for fetching specific tweet_id, and user information.
3) Run the job using Apache Spark on standalone server to fetch the complete information.
4) Added Unicodecsv package to handle UTF-8 characters present in the tweet information.

Steps to run the file:
1) Run twitter_scrapper.py // Genearate the tweet information
2) Run twitter_spark.py // Extract the tweet_id from the output of above python file and interact with Twitter REST API for extracting complete information.
