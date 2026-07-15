from src.data.fetcher import CommodityFetcher


fetcher = CommodityFetcher()

print("Available datasets:")
print(fetcher.available())

print()

gold = fetcher.load("gold")

print(gold.head())

print()

print(gold.info())