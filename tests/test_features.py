from src.data.fetcher import CommodityFetcher
from src.data.cleaner import DataCleaner
from src.features.indicators import FeatureEngineer


# 初始化模块

fetcher = CommodityFetcher()
cleaner = DataCleaner()
engineer = FeatureEngineer()


# 1. 获取原始数据

gold = fetcher.load("gold")

print("=" * 50)
print("Raw Data")
print(gold)


# 2. 数据清洗

gold_clean = cleaner.clean(gold)

print("=" * 50)
print("Clean Data")
print(gold_clean)


# 3. 特征工程

gold_features = engineer.add_features(gold_clean)


print("=" * 50)
print("Feature Data")
print(gold_features)


# 查看字段

print("=" * 50)
print("Columns:")
print(gold_features.columns)