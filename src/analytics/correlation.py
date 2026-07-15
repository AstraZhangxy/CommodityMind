"""
correlation.py

Commodity correlation analysis.
"""

import pandas as pd


class CorrelationAnalyzer:
    """
    Analyze correlation between commodities.
    """


    def price_correlation(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        name1="Commodity1",
        name2="Commodity2"
    ):
        """
        Calculate price correlation.
        """

        merged = pd.DataFrame(
            {
                name1:
                    df1["Close"],

                name2:
                    df2["Close"]
            }
        )


        correlation = (
            merged
            .corr()
            .loc[name1, name2]
        )


        return correlation



    def return_correlation(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        name1="Commodity1",
        name2="Commodity2"
    ):
        """
        Calculate return correlation.
        """

        merged = pd.DataFrame(
            {
                name1:
                    df1["Daily_Return"],

                name2:
                    df2["Daily_Return"]
            }
        )


        correlation = (
            merged
            .corr()
            .loc[name1, name2]
        )


        return correlation