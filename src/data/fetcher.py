from pathlib import Path
import pandas as pd


class CommodityFetcher:

    def __init__(self):

        self.data_dir = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "raw"
        )

    def available(self):

        return sorted(
            [
                f.stem
                for f in self.data_dir.glob("*.csv")
            ]
        )

    def load(self, name: str):

        file = self.data_dir / f"{name}.csv"

        if not file.exists():

            raise FileNotFoundError(
                f"Dataset not found: {file}"
            )

        return pd.read_csv(file)