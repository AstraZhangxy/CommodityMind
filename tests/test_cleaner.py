from src.data.fetcher import CommodityFetcher
from src.data.cleaner import DataCleaner


fetcher = CommodityFetcher()
cleaner = DataCleaner()

gold = fetcher.load("gold")

print("Before Cleaning")
print(gold)
print()

gold = cleaner.clean(gold)

print("After Cleaning")
print(gold)
print()

print(gold.info())