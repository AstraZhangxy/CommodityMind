"""
processor.py

Clean financial news text
before sentiment analysis,
importance scoring,
embedding and RAG.
"""


import re

from bs4 import BeautifulSoup


from src.news.model import NewsItem

from src.news.sentiment import NewsSentimentAnalyzer

from src.news.importance import NewsImportanceAnalyzer




class NewsProcessor:



    def __init__(self):


        self.sentiment_analyzer = (
            NewsSentimentAnalyzer()
        )


        self.importance_analyzer = (
            NewsImportanceAnalyzer()
        )



    def clean_text(
            self,
            text
    ):


        """
        Remove html,
        urls and useless characters.
        """


        if not text:

            return ""



        # remove html

        soup = BeautifulSoup(
            text,
            "html.parser"
        )


        text = soup.get_text(
            separator=" "
        )



        # remove url

        text = re.sub(
            r"http\S+",
            "",
            text
        )



        # remove extra spaces

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


        """
        Process NewsItem.

        Pipeline:

        NewsItem
            |
            ↓
        clean text
            |
            ↓
        sentiment score
            |
            ↓
        importance score
            |
            ↓
        NewsItem
        """



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



        importance_score = (

            self.importance_analyzer.analyze(

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


            importance_score=importance_score

        )



        return processed_news