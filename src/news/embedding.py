"""
embedding.py

Generate financial news embeddings
using BGE-M3 model.
"""


from sentence_transformers import SentenceTransformer




class NewsEmbedding:


    def __init__(self):


        """
        Load BGE-M3 embedding model.
        """


        self.model = SentenceTransformer(

            "BAAI/bge-m3"

        )




    def build_text(
            self,
            news
    ):


        """
        Combine important fields
        for embedding.
        """


        text = (

            news.title

            + "\n"

            + news.content

        )


        return text




    def embed(
            self,
            news
    ):


        """
        Convert NewsItem
        into vector.
        """


        text = self.build_text(

            news

        )



        vector = self.model.encode(

            text,

            normalize_embeddings=True

        )


        return vector.tolist()