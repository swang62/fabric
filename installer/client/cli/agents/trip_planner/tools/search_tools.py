import json
import os

import requests
from langchain.tools import tool


class SearchTools:

    @tool("Search")
    def search_internet_query(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        top_result_to_return = 4
        url = "https://search.mildlybrewed.com/search"
        headers = {
            "X-API-KEY": os.environ.get("SERPER_API_KEY", ""),
            "content-type": "application/json",
        }
        response = requests.request(
            "GET", url, headers=headers, params={"q": str(query), "format": "json"}
        )
        # check if there is an organic key
        if "results" not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with your api key."
        else:
            results = response.json()["results"]
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append(
                        "\n".join(
                            [
                                f"Title: {result['title']}",
                                f"Link: {result['url']}",
                                f"Snippet: {result['content']}",
                                "\n-----------------",
                            ]
                        )
                    )
                except KeyError:
                    next

            return "\n".join(string)

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        top_result_to_return = 4
        url = "https://search.mildlybrewed.com/search"
        headers = {
            "X-API-KEY": os.environ.get("SERPER_API_KEY", ""),
            "content-type": "application/json",
        }
        response = requests.request(
            "GET", url, headers=headers, params={"q": str(query), "format": "json"}
        )
        # check if there is an organic key
        if "results" not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with your api key."
        else:
            results = response.json()["results"]
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append(
                        "\n".join(
                            [
                                f"Title: {result['title']}",
                                f"Link: {result['url']}",
                                f"Snippet: {result['content']}",
                                "\n-----------------",
                            ]
                        )
                    )
                except KeyError:
                    next

            return "\n".join(string)
