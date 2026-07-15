"""
cleaner.py

Data preprocessing module for CommodityMind.

Functions:
- Convert date column to datetime
- Sort by date
- Remove duplicate rows
- Remove missing values
- Reset index
"""

import pandas as pd


class DataCleaner:
    """Data cleaning class for commodity datasets."""

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean raw commodity data.

        Parameters
        ----------
        df : pd.DataFrame
            Raw dataset.

        Returns
        -------
        pd.DataFrame
            Cleaned dataset.
        """

        # 创建副本，避免修改原数据
        df = df.copy()

        # Date 转 datetime
        if "Date" in df.columns:
            df["Date"] = pd.to_datetime(df["Date"])

        # 按日期排序
        if "Date" in df.columns:
            df = df.sort_values("Date")

        # 删除重复行
        df = df.drop_duplicates()

        # 删除缺失值
        df = df.dropna()

        # 重置索引
        df = df.reset_index(drop=True)

        return df
