"""
fetcher.py

Download commodity market data from Yahoo Finance.
"""

from datetime import datetime

import pandas as pd
import yfinance as yf


class CommodityFetcher:
    """
    Fetch historical commodity market data.
    """

    def fetch(
        self,
        symbol: str,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
        """
        Download historical market data.

        Parameters
        ----------
        symbol : str
            Yahoo Finance ticker.

        start_date : str
            YYYY-MM-DD

        end_date : str
            YYYY-MM-DD

        Returns
        -------
        pandas.DataFrame
        """

        data = yf.download(
            symbol,
            start=start_date,
            end=end_date,
            auto_adjust=True,
            progress=False,
        )

        if data.empty:
            raise ValueError(
                f"No data returned for {symbol}"
            )

        data.index = pd.to_datetime(data.index)

        return data.sort_index()
