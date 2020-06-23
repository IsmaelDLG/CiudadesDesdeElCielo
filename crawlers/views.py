from django.shortcuts import render
import os

from pathlib import Path

# Create your views here.
def index(request):
    return render(request, Path('crawlers/index.html'))

def runSpiders(request):
    # https://stackoverflow.com/questions/1853662/how-to-show-page-loading-div-until-the-page-has-finished-loading
    spiders = Path(__file__).absolute().parent / Path("Scrapy/WebCrawling/spiders")
    
    print("Launching all spiders")
    for spider in spiders.iterdir():
        if spider.is_file() and spider.name[-1*len('_spider.py'):] == '_spider.py':
            print("    Launching " + str(spider.name))
            res = os.system("cd " + str(Path(__file__).absolute().parent) + " && " + "scrapy crawl " + str(spider.name.replace('_spider.py', '')))
    
    with open(str(Path(__file__).absolute().parent / Path("items.jl")), 'r') as f:
        text = f.read().split("\n")
    return render(request, Path('crawlers/results.html'), {
        'results' : text,
        'num' : len(text)
    })
