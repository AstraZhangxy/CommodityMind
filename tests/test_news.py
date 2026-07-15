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
    "Gold"
)



for news in news_list:


    print("="*50)


    print("Before Process:")


    print(
        news.to_dict()
    )



    processed = processor.process(
        news
    )

    print(
        processed.to_dict()
    )