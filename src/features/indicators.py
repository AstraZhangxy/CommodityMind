#indicator属于特征的一种形式，为0-1指示变量/哑变量
#Factor因子本质是量化中用于预测收益风控的自变量，本质是筛选后的用于建模的优质特征。

"""
indicators.py

Financial feature engineering module.

Generate:
- Daily Return
- Log Return
- Moving Average
- Rolling Volatility
"""

import numpy as np
import pandas as pd


class FeatureEngineer:
    """
    Generate financial indicators for commodity data.
    """

    def add_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add quantitative features.

        Parameters
        ----------
        df : pd.DataFrame
            Clean commodity dataframe.

        Returns
        -------
        pd.DataFrame
            Dataset with financial features.
        """

        # 防止修改原数据
        df = df.copy()

        # Daily Return
        df["Daily_Return"] = (
            df["Close"]
            .pct_change()
        )

        # Log Return
        df["Log_Return"] = np.log(
            df["Close"] /
            df["Close"].shift(1)
        )

        # Moving Average
        df["MA5"] = (
            df["Close"]
            .rolling(window=5)
            .mean()
        )

        df["MA20"] = (
            df["Close"]
            .rolling(window=20)
            .mean()
        )

        # Rolling Volatility
        df["Volatility"] = (
            df["Daily_Return"]
            .rolling(window=20)
            .std()
        )

        return df