"""
sentiment.py

Financial news sentiment analyzer.
"""


import re



class NewsSentimentAnalyzer:


    def __init__(self):

        # positive financial words

        self.positive_words = [

            "rise",
            "rally",
            "surge",
            "gain",
            "boost",
            "strong",
            "bullish",
            "higher",
            "increase",
            "support"

        ]


        # negative financial words

        self.negative_words = [

            "fall",
            "drop",
            "decline",
            "weak",
            "bearish",
            "lower",
            "loss",
            "risk",
            "crisis"

        ]



    def analyze(
            self,
            text
    ):


        """
        Simple financial sentiment scoring.

        return:
            score between -1 and 1

        positive:
            >0

        negative:
            <0
        """


        text = text.lower()



        # remove symbols

        text = re.sub(
            r"[^a-z\s]",
            "",
            text
        )



        words = text.split()



        positive_count = 0

        negative_count = 0



        for word in words:


            if word in self.positive_words:

                positive_count += 1



            if word in self.negative_words:

                negative_count += 1



        total = (
            positive_count
            +
            negative_count
        )



        if total == 0:

            return 0.0



        score = (
            positive_count
            -
            negative_count
        ) / total



        return round(
            score,
            2
        )