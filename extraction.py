from bs4 import BeautifulSoup
import requests

def extract_html(url: str) -> BeautifulSoup:
    """Extract a BeautifulSoup object from a URL"""
    return BeautifulSoup(requests.get(url).content, 'html.parser')