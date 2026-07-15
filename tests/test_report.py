from src.data.fetcher import CommodityFetcher
from src.data.cleaner import DataCleaner
from src.features.indicators import FeatureEngineer

from src.analytics.risk import RiskAnalyzer

from src.report.generator import ReportGenerator



fetcher = CommodityFetcher()
cleaner = DataCleaner()
engineer = FeatureEngineer()

risk = RiskAnalyzer()

reporter = ReportGenerator()



# Load gold data

gold = fetcher.load("gold")


# Clean

gold = cleaner.clean(gold)


# Feature engineering

gold = engineer.add_features(gold)



# Risk analysis

risk_result = (
    risk.risk_summary(gold)
)



# Generate report

report = reporter.generate(
    "Gold",
    risk_result
)


print(report)