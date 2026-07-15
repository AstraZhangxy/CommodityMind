"""
model.py

Data structure definition
for financial news.
"""


from dataclasses import dataclass
from typing import Optional



@dataclass
class NewsItem:


    commodity: str

    title: str

    content: str

    source: str

    url: str


    publish_time: str


    sentiment_score: Optional[float] = None

    importance_score: Optional[float] = None



    def to_dict(self):

        return {

            "commodity":
                self.commodity,


            "title":
                self.title,


            "content":
                self.content,


            "source":
                self.source,


            "url":
                self.url,


            "publish_time":
                self.publish_time,


            "sentiment_score":
                self.sentiment_score,


            "importance_score":
                self.importance_score

        }