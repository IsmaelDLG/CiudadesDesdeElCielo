# -*- coding: latin-1 -*-
import scrapy
import urllib
import json
import requests

API_KEY = "8UvakkzGb7Pej0zUOn7FURAs5dppeCip"

API_URL = "http://open.mapquestapi.com/geocoding/v1/reverse?location=%s,%s&key=%s"



def to_write(uni_str):
    return urllib.parse.unquote(uni_str.encode('utf8')).decode('utf8')


class ObraNuevaBarcelonaSpider(scrapy.Spider):
    name = "obranuevabarcelona"
    start_urls = [
        'https://www.obranuevabarcelona.cat/inmuebles-obra-nueva/proximas-promociones/',
        # More urls here if needed
    ]

    def parse(self, response):

        # Follow links
        
        for link in response.css('div.rh_list_card__details a'):
            yield response.follow(link, callback=self.parse_details)

    def parse_details(self, response):
        pattern = "propertyMapData = "

        page = response.text
        
        beg = page.find(pattern) + len(pattern)
        end = page.find("\n", beg) - 1
        
        data = page[beg:end]
        # self.log(data)

        data = json.loads(data)
        # self.log(data['lat'])
        # self.log(data['lng'])

        r = requests.get(API_URL % (data['lat'],data['lng'],API_KEY))
        #self.log(r.headers['Content-Type'])

        res = r.json()['results']

        for item in res:
            for addr in item['locations']:

                yield {
                    'cp'    :   addr['postalCode'],
                    'dir'   :   addr['street'],
                    'ca'    :   addr['adminArea3'],
                    'prov'  :   addr['adminArea5'],
                    'pais'  :   addr['adminArea1'],
                    'uso'   :   'OBRA_NUEVA'
                }

        



