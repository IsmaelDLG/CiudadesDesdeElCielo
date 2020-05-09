# -*- coding: latin-1 -*-
import scrapy
import urllib
import json
import requests

API_KEY = "8UvakkzGb7Pej0zUOn7FURAs5dppeCip"

API_URL = "http://open.mapquestapi.com/geocoding/v1/reverse?location=%s,%s&key=%s"



def to_write(uni_str):
    return urllib.parse.unquote(uni_str.encode('utf8')).decode('utf8')


class HabitacliaSpider(scrapy.Spider):
    name = "habitaclia"
    categories = ['oficinas', 'viviendas', 'naves_industriales']
    start_urls = []
    for each in categories:
        start_urls.append('https://www.habitaclia.com/obra_nueva-%s-en-barcelona/buscadorpromocion.htm' % each)


    def parse(self, response):
        if (len(response.css('div.noHayResultadoslista')) == 0):
            final_links = response.css('div.datos a')
            if (len(final_links) != 0):
                for link in final_links:
                    yield response.follow(link, callback=self.parse_details)
            else:
                # Follow links
                for link in response.css('div#enlacesmapa ul li a'):
                    yield response.follow(link, callback=self.parse)

    def parse_details(self, response):
        beg_pattern = "GMapsConfig : JSON.parse(\""
        end_pattern = "\"),\r\n\t\t\trutaMenu:"
        page = response.text
        
        beg = page.find(beg_pattern) + len(beg_pattern)
        end = page.find(end_pattern, beg)
        if beg != -1 and end != -1:
            data = page[beg:end]
            data = data.replace('\\', '')
            print(data)
            data = json.loads(data)

            if data != None: 
                r = requests.get(API_URL % (data['VGPSLat'],data['VGPSLon'],API_KEY))

                res = r.json()['results']

                # https://www.habitaclia.com/obra_nueva-naves_industriales-en-terrassa/promo_1014003554965?geo=a
                url_info = response.url.split("/")[-2].split("-")

                obra_nueva = True if url_info[0] == 'obra_nueva' else False
                if url_info[1] == 'naves_industriales':
                    uso1 = 'otros'
                    uso2 = 'industrial'
                elif url_info[1] == 'viviendas':
                    uso1 = 'residencial'
                    uso2 = 'residencial'
                elif url_info[1] == 'oficinas':
                    uso1 = 'oficina'
                    uso2 = 'oficina'

                for item in res:
                    for addr in item['locations']:

                        yield {
                            'lat'   :   data['VGPSLat'],
                            'lon'   :   data['VGPSLon'],
                            'err'   :   None,
                            'gruas' :   None,
                            'cp'    :   addr['postalCode'],
                            'dir'   :   addr['street'],
                            'num'   :   None,
                            'ca'    :   addr['adminArea3'],
                            'prov'  :   addr['adminArea5'],
                            'pais'  :   addr['adminArea1'],
                            'uso1'  :   uso1,
                            'uso2'  :   uso2,
                            'obra_nueva'   :   obra_nueva,
                        }

        



