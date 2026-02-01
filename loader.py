import requests
import io
from bs4 import BeautifulSoup


if __name__ == "__main__":
    print(f"\nKérlek futtasd a main.py -t!\n")
    exit


class Title:
    def __init__(self, text):
        self.text = text


def webmapper(url):
    content = requests.get(url)
    html_content = content.text

    soup = BeautifulSoup(html_content, 'html.parser')
    
    return soup

def printFiltered(content, level):
    for Title.text in content.find_all(level):
        print(Title.text.text)

def fileWrite(content, level, filename):
    with io.open(filename, "w", encoding="utf8") as f:
        for Title.text in content.find_all(level):
            f.write(Title.text.text)
    
    print(f"*** {filename} - elkészült! ***")
