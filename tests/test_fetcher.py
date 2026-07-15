from src.data.fetcher import CommodityFetcher
from src.data.symbols import GOLD

fetcher = CommodityFetcher()

gold = fetcher.fetch(
    symbol=GOLD,
    start_date="2024-01-01",
    end_date="2024-12-31",
)

print(gold.head())
print(gold.tail())