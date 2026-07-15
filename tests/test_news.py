"""
test_news.py

Test news pipeline.

collector
    ↓
NewsItem
    ↓
processor
    ↓
sentiment
    ↓
importance
"""


from src.news.collector import NewsCollector

from src.news.processor import NewsProcessor




collector = NewsCollector()


processor = NewsProcessor()




rss = (

    "https://news.google.com/rss/search?"

    "q=gold+price"

)



news_list = collector.collect_from_rss(

    rss,

    commodity="Gold",

    limit=5

)




for news in news_list:



    print("=" * 60)


    print("Before Process:")


    print(

        news.to_dict()

    )



    print()



    processed = processor.process(

        news

    )



    print("After Process:")


    print(

        processed.to_dict()

    )