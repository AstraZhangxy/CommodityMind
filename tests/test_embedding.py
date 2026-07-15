"""
test_embedding.py

Test BGE-M3 embedding.
"""


from src.news.collector import NewsCollector

from src.news.processor import NewsProcessor

from src.news.embedding import NewsEmbedding




collector = NewsCollector()


processor = NewsProcessor()


embedding = NewsEmbedding()




rss = (

    "https://news.google.com/rss/search?"

    "q=gold+price"

)




news_list = collector.collect_from_rss(

    rss,

    commodity="Gold",

    limit=3

)



for news in news_list:


    print("="*60)



    print("Original:")


    print(

        news.to_dict()

    )



    processed = processor.process(

        news

    )



    vector = embedding.embed(

        processed

    )



    print()


    print("Embedding dimension:")


    print(

        len(vector)

    )


    print()


    print("First 10 values:")


    print(

        vector[:10]

    )