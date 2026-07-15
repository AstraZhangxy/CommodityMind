"""
crawler.py

Fetch article content
from news url.
"""


import requests

from bs4 import BeautifulSoup




class NewsCrawler:



    def fetch_content(
            self,
            url
    ):


        try:


            headers = {

                "User-Agent":
                "Mozilla/5.0"

            }


            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )


            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )


            paragraphs = soup.find_all(
                "p"
            )


            content = " ".join(

                [
                    p.get_text()
                    for p in paragraphs
                ]

            )


            return content



        except Exception as e:


            print(
                "Crawler error:",
                e
            )


            return ""