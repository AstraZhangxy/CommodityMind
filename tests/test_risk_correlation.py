from src.data.fetcher import CommodityFetcher
from src.data.cleaner import DataCleaner
from src.features.indicators import FeatureEngineer

from src.analytics.risk import RiskAnalyzer
from src.analytics.correlation import CorrelationAnalyzer



fetcher = CommodityFetcher()
cleaner = DataCleaner()
engineer = FeatureEngineer()


risk = RiskAnalyzer()
corr = CorrelationAnalyzer()



# Gold

gold = fetcher.load("gold")

gold = cleaner.clean(gold)

gold = engineer.add_features(gold)



print("=" * 50)

print("Risk Report")

print(
    risk.risk_summary(gold)
)



print("=" * 50)

print("Correlation Test")


oil = fetcher.load("oil")

oil = cleaner.clean(oil)

oil = engineer.add_features(oil)



print(
    corr.return_correlation(
        gold,
        oil,
        "Gold",
        "Oil"
    )
)