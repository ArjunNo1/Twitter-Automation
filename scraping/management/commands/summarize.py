
from turtle import pos
from django.core.management.base import BaseCommand
from scraping.models import Post
from transformers import pipeline
import pandas as pd
from scraping.models import Post


class Command(BaseCommand):
    summarizer = pipeline("summarization")
    help = "collect jobs"
    # define logic of command

    def ht(self,text):
        t = text.split(" ")
        tex = []
        h = []
        # print(t)
        for i in t:
            if "#" in i:
                h.append(i)
            else:
                tex.append(i)
        #   hat.append(" ".join(h))
        return " ".join(tex), " ".join(h)

    def summ(self,text):
        s, h = self.ht(text)
        res = self.summarizer(s, max_length=100, min_length=30, do_sample=False)
        # res+=h.split(" ")
        # print(type(res))
        # print(h)
        return res[0]['summary_text'] + '\n' + h


    def handle(self, *args, **options):
        

        posts = Post.objects.all()
        post_dataframe = pd.DataFrame.from_records(posts.values())
        print(post_dataframe.head())

        post_dataframe['summarized_text'] = post_dataframe['text'].apply(lambda x: self.summ(x))
        # post_dataframe.loc[0, 'summarized_text'] = post_dataframe.iloc[0,:].apply(self.summ)
        

        for i in range(len(post_dataframe)):
            Post.objects.filter(id=post_dataframe.loc[i,'id']).update(
                summarized_text = post_dataframe.loc[i, 'summarized_text']
            )
        print(post_dataframe.loc[0, 'summarized_text'])




# df['ns'] = df[sum'nt'].apply(lambda x: ht(x))
# df['hat'] = pd.DataFrame(hat)
# res = summarizer(df['ns'], max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        self.stdout.write( 'summarizing job complete' )
        
