"""
risk.py

Risk analytics module for CommodityMind.

Functions:
- Annualized volatility
- Maximum drawdown
- Risk summary
"""

import numpy as np
import pandas as pd


class RiskAnalyzer:
    """
    Calculate commodity risk metrics.
    """

    def annual_volatility(
        self,
        df: pd.DataFrame,
        trading_days: int = 252
    ):
        """
        Calculate annualized volatility.

        Formula:
        daily volatility * sqrt(252)
        """

        if "Daily_Return" not in df.columns:
            raise ValueError(
                "Daily_Return column required."
            )

        volatility = (
            df["Daily_Return"]
            .std()
            *
            np.sqrt(trading_days)
        )

        return volatility


    def maximum_drawdown(
        self,
        df: pd.DataFrame
    ):
        """
        Calculate maximum drawdown.

        MDD = (price - peak) / peak
        """

        if "Close" not in df.columns:
            raise ValueError(
                "Close column required."
            )

        cumulative_max = (
            df["Close"]
            .cummax()
        )

        drawdown = (
            df["Close"]
            -
            cumulative_max
        ) / cumulative_max


        max_drawdown = (
            drawdown
            .min()
        )

        return max_drawdown


    def risk_summary(
        self,
        df: pd.DataFrame
    ):
        """
        Return complete risk report.
        """

        return {
            "Annual Volatility":
                self.annual_volatility(df),

            "Maximum Drawdown":
                self.maximum_drawdown(df)
        }