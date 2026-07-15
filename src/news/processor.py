"""
processor.py

Clean financial news text
before sentiment analysis,
embedding and RAG.
"""


import re

from bs4 import BeautifulSoup

from src.news.model import NewsItem

from src.news.sentiment import NewsSentimentAnalyzer



class NewsProcessor:



    def __init__(self):

        self.sentiment_analyzer = (
            NewsSentimentAnalyzer()
        )



    def clean_text(
            self,
            text
    ):


        if not text:

            return ""


        soup = BeautifulSoup(
            text,
            "html.parser"
        )


        text = soup.get_text(
            separator=" "
        )


        text = re.sub(
            r"http\S+",
            "",
            text
        )


        text = re.sub(
            r"\s+",
            " ",
            text
        )


        return text.strip()



    def process(
            self,
            news: NewsItem
    ):


        cleaned_content = (

            self.clean_text(

                news.content

            )

        )


        sentiment_score = (

            self.sentiment_analyzer.analyze(

                cleaned_content

            )

        )



        processed_news = NewsItem(


            commodity=news.commodity,


            title=news.title,


            content=cleaned_content,


            source=news.source,


            url=news.url,


            publish_time=news.publish_time,


            sentiment_score=sentiment_score,


            importance_score=news.importance_score

        )



        return processed_news