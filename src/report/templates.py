"""
templates.py

Report templates for CommodityMind.
"""


RISK_LEVELS = {
    "low": "Low Risk",
    "medium": "Medium Risk",
    "high": "High Risk"
}


def risk_description(level):

    descriptions = {

        "Low Risk":
            "The commodity market shows relatively stable price movement.",

        "Medium Risk":
            "The commodity market shows moderate volatility and requires attention.",

        "High Risk":
            "The commodity market experiences significant volatility and uncertainty."

    }

    return descriptions[level]