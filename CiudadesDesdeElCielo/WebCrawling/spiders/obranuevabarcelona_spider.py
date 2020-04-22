import scrapy
import urllib
# -*- coding: utf-8 -*-

def to_write(uni_str):
    return urllib.parse.unquote(uni_str.encode('utf8')).decode('utf8')


class ObraNuevaBarcelonaSpider(scrapy.Spider):
    name = "obranuevabarcelona"
    start_urls = [
        'https://www.obranuevabarcelona.cat/inmuebles-obra-nueva/proximas-promociones/',
        # More urls here if needed
    ]

    def parse(self, response):

        # Parses info in files
        
        for card in response.css('div.rh_list_card__details'):
            yield {
                'title': card.css('a::text').get(),
                'link': card.css('a').attrib['href']
            }

        # Follow links
        
        
        for link in response.css('div.rh_list_card__details a'):
            yield response.follow(link, callback=self.parse_details)

    def parse_details(self, response):
        units = response.css('div.floor-plan-title')

        res = {}

        index = 0
        for row in units:
            # alldata = response.css('div.floor-plan-meta p::text').getall()
            try:
                res[row.css('div.title h3::text').get()] = {
                    'surface': row.css('div.floor-plan-meta p::text')[0].get(),
                    'rooms' : row.css('div.floor-plan-meta p::text')[1].get(),
                    'bathrooms' : row.css('div.floor-plan-meta p::text')[2].get()
                }
            except IndexError:
                continue
            

        return res


        



