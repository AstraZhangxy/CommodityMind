"""
charts.py

Visualization module for CommodityMind.

Generate:
- Price trend chart
- Return chart
- Moving average chart
"""

import matplotlib.pyplot as plt


class CommodityVisualizer:
    """
    Visualize commodity market data.
    """

    def plot_price(self, df, title="Commodity Price"):
        """
        Plot closing price trend.
        """

        plt.figure(figsize=(10, 5))

        plt.plot(
            df["Date"],
            df["Close"]
        )

        plt.title(title)

        plt.xlabel("Date")
        plt.ylabel("Close Price")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()


    def plot_returns(self, df, title="Daily Return"):
        """
        Plot daily return.
        """

        plt.figure(figsize=(10, 5))

        plt.plot(
            df["Date"],
            df["Daily_Return"]
        )

        plt.title(title)

        plt.xlabel("Date")
        plt.ylabel("Return")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()


    def plot_moving_average(
        self,
        df,
        title="Moving Average"
    ):
        """
        Plot MA5 and MA20.
        """

        plt.figure(figsize=(10, 5))

        plt.plot(
            df["Date"],
            df["Close"],
            label="Close"
        )

        plt.plot(
            df["Date"],
            df["MA5"],
            label="MA5"
        )

        plt.plot(
            df["Date"],
            df["MA20"],
            label="MA20"
        )


        plt.title(title)

        plt.xlabel("Date")
        plt.ylabel("Price")

        plt.legend()

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()
