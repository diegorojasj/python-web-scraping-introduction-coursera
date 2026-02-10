from bs4 import BeautifulSoup
import requests

def get_html(url: str) -> BeautifulSoup:
    """Download a file from a URL"""
    return BeautifulSoup(requests.get(url).content, 'html.parser')