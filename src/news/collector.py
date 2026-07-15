"""
collector.py

Commodity news collector.
RSS based version.
"""


import feedparser

from datetime import datetime

from src.news.model import NewsItem



class NewsCollector:


    def collect_from_rss(
            self,
            rss_url,
            commodity="Gold",
            limit=5
    ):


        feed = feedparser.parse(
            rss_url
        )


        news_list = []


        for item in feed.entries[:limit]:


            # -----------------------
            # title
            # -----------------------

            title = (
                item.get(
                    "title",
                    ""
                )
            )


            # -----------------------
            # source extraction
            # -----------------------

            source = "Unknown"


            if "-" in title:

                source = (
                    title
                    .split("-")
                    [-1]
                    .strip()
                )


            elif "source" in item:

                source = item.source.title



            # -----------------------
            # content
            # -----------------------

            content = (
                item.get(
                    "summary",
                    title
                )
            )


            # -----------------------
            # publish time
            # -----------------------

            if "published_parsed" in item:

                publish_time = datetime(
                    *item.published_parsed[:6]
                ).strftime(
                    "%Y-%m-%d"
                )


            else:

                publish_time = datetime.now().strftime(
                    "%Y-%m-%d"
                )



            # -----------------------
            # url
            # -----------------------

            url = (
                item.get(
                    "link",
                    ""
                )
            )


            # -----------------------
            # NewsItem object
            # -----------------------

            news = NewsItem(

                commodity=commodity,


                title=title,


                content=content,


                source=source,


                url=url,


                publish_time=publish_time,


                sentiment_score=None,


                importance_score=None

            )


            news_list.append(
                news
            )



        return news_list