import tweepy
from turtle import pos
from django.core.management.base import BaseCommand
from scraping.models import Post
from transformers import pipeline
import pandas as pd
from scraping.models import Post
from django.conf import settings



class Command(BaseCommand):
    summarizer = pipeline("summarization")
    help = "collect jobs"
    # define logic of command


    def handle(self, *args, **options):
        

        posts = Post.objects.all()
        post_dataframe = pd.DataFrame.from_records(posts.values())
        # print(post_dataframe.head())

        # post_dataframe['summarized_text'] = post_dataframe['text'].apply(lambda x: self.summ(x))
        # post_dataframe.loc[0, 'summarized_text'] = post_dataframe.iloc[0,:].apply(self.summ)
        

        for i in range(3):
            # Post.objects.filter(id=post_dataframe.loc[i,'id']).update(
                # summarized_text = post_dataframe.loc[i, 'summarized_text']
            # )
            if not post_dataframe.loc[i, 'twtpost']:
                if post_dataframe.loc[i, 'summarized_text'] != "NS":
                    print("going to tweet")
                    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_KEY_SECRET)
                    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
                    api = tweepy.API(auth)
                    api.update_status(post_dataframe.loc[i, 'summarized_text'][0:250])
                    post_dataframe.loc[i, 'twtpost'] = True
                    # print(post_dataframe.loc[i, 'twtpost'])
                    # str(list(post_dataframe.loc[i, 'summarized_text']).split(" ")[:10])




            print(post_dataframe.loc[0, 'summarized_text'])






# df['ns'] = df[sum'nt'].apply(lambda x: ht(x))
# df['hat'] = pd.DataFrame(hat)
# res = summarizer(df['ns'], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        self.stdout.write( 'tweet job complete' )
        
