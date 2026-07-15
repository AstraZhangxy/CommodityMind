from src.data.fetcher import CommodityFetcher
from src.data.cleaner import DataCleaner
from src.features.indicators import FeatureEngineer
from src.visualization.charts import CommodityVisualizer



fetcher = CommodityFetcher()
cleaner = DataCleaner()
engineer = FeatureEngineer()
visualizer = CommodityVisualizer()


# Load data

gold = fetcher.load("gold")


# Clean

gold = cleaner.clean(gold)


# Feature

gold = engineer.add_features(gold)


# Visualization

visualizer.plot_price(
    gold,
    "Gold Price Trend"
)


visualizer.plot_returns(
    gold,
    "Gold Daily Return"
)


visualizer.plot_moving_average(
    gold,
    "Gold Moving Average"
)