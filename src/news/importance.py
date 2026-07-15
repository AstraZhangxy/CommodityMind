"""
importance.py

Financial news importance scoring.
"""


import re



class NewsImportanceAnalyzer:



    def __init__(self):


        # high impact financial keywords

        self.high_impact_words = [

            "fed",

            "federal reserve",

            "interest rate",

            "inflation",

            "cpi",

            "gdp",

            "recession",

            "war",

            "sanction",

            "crisis",

            "central bank",

            "rate cut",

            "rate hike"

        ]


        # commodity related keywords

        self.commodity_words = [

            "gold",

            "silver",

            "oil",

            "commodity",

            "metal",

            "currency"

        ]



    def analyze(
            self,
            text
    ):


        """
        Calculate importance score.

        return:
            0 - 1

        higher:
            more important
        """



        text = text.lower()



        text = re.sub(
            r"[^a-z\s]",
            "",
            text
        )



        score = 0



        # -------------------
        # financial keywords
        # -------------------

        for word in self.high_impact_words:


            if word in text:

                score += 0.15



        # -------------------
        # commodity relevance
        # -------------------

        for word in self.commodity_words:


            if word in text:

                score += 0.1



        # -------------------
        # length factor
        # -------------------

        length = len(text)



        if length > 200:

            score += 0.1


        elif length > 100:

            score += 0.05



        # limit score

        if score > 1:

            score = 1



        return round(
            score,
            2
        )