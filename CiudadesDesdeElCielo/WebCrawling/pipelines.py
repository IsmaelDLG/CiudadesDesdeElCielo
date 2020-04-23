# -*- coding: latin-1 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class JsonWriterPipeline(object):
    def remove_special_chars(self, myStr):
        return (
            myStr.replace("à", "a")
            .replace("á", "a")
            .replace("è", "e")
            .replace("é", "e")
            .replace("ì", "i")
            .replace("í", "i")
            .replace("ò", "o")
            .replace("ó", "o")
            .replace("ù", "u")
            .replace("ú", "u")
        )

    def open_spider(self, spider):
        self.file = open("items.jl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        # line = self.remove_special_chars(line)
        self.file.write(line)
        return item


class CiudadesdesdeelcieloPipeline(object):
    def process_item(self, item, spider):
        return item
