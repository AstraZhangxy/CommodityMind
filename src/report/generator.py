"""
generator.py

Generate commodity market reports.
"""

from src.report.templates import (
    RISK_LEVELS,
    risk_description
)


class ReportGenerator:
    """
    Generate financial market reports.
    """


    def calculate_risk_level(
        self,
        volatility
    ):
        """
        Classify risk based on volatility.
        """

        if volatility < 0.15:

            return RISK_LEVELS["low"]

        elif volatility < 0.30:

            return RISK_LEVELS["medium"]

        else:

            return RISK_LEVELS["high"]



    def generate(
        self,
        asset_name,
        risk_summary
    ):
        """
        Generate commodity report.

        Parameters
        ----------
        asset_name:
            Commodity name

        risk_summary:
            Dictionary from RiskAnalyzer

        """

        volatility = (
            risk_summary["Annual Volatility"]
        )

        drawdown = (
            risk_summary["Maximum Drawdown"]
        )


        risk_level = (
            self.calculate_risk_level(
                volatility
            )
        )


        report = f"""
==============================
CommodityMind AI Report
==============================


Asset:
{asset_name}


Market Risk Level:
{risk_level}


Market Overview:

{risk_description(risk_level)}


Key Metrics:

Annual Volatility:
{volatility:.2%}


Maximum Drawdown:
{drawdown:.2%}


Risk Consideration:

Investors should monitor market
conditions and volatility changes.

==============================
"""


        return report