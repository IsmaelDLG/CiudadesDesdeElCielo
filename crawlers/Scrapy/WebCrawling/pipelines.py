# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import sqlite3


class JsonWriterPipeline(object):
    def remove_special_chars(self, myStr):
        def remove_special_vowels(myStr):
            return (
                myStr.replace("à", "a")
                .replace("á", "a")
                .replace("è", "e")
                .replace("é", "e")
                .replace("ì", "i")
                .replace("í", "i")
                .replace("ï", "i")
                .replace("ò", "o")
                .replace("ó", "o")
                .replace("ù", "u")
                .replace("ú", "u")
                .replace("ü", "u")
            )
        def remove_special_consonants(myStr):
            return (
                myStr.replace("ç","c")
                .replace("ñ","n")
            )

        return remove_special_consonants(remove_special_vowels(myStr))

    def open_spider(self, spider):
        self.file = open("items.jl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        # line = self.remove_special_chars(line)
        self.file.write(line)
        return item

class DatabasePipeline(object):
    def __init__(self, db, user, passwd, host, db_used):
        self.db = db
        self.user = user
        self.passwd = passwd
        self.host = host
        self.db_used = db_used
    
    def remove_special_chars(self, myStr):
        def remove_special_vowels(myStr):
            return (
                myStr.replace("à", "a")
                .replace("á", "a")
                .replace("è", "e")
                .replace("é", "e")
                .replace("ì", "i")
                .replace("í", "i")
                .replace("ï", "i")
                .replace("ò", "o")
                .replace("ó", "o")
                .replace("ù", "u")
                .replace("ú", "u")
                .replace("ü", "u")
            )
        def remove_special_consonants(myStr):
            return (
                myStr.replace("ç","c")
                .replace("ñ","n")
            )

        return remove_special_consonants(remove_special_vowels(myStr))

    @classmethod
    def from_crawler(cls, crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")

        if not db_settings:
            raise NotConfigured

        db_used = crawler.settings.get("DB_USED")

        db = db_settings[db_used]['db']
        user = db_settings[db_used]['user']
        passwd = db_settings[db_used]['passwd']
        host = db_settings[db_used]['host']


        return cls(db, user, passwd, host, db_used)

    def open_spider(self, spider):
        if (self.db_used == "sqlite3"):
            self.conn = sqlite3.connect(self.db)
            self.cursor = self.conn.cursor()
            try:
                create = """CREATE TABLE IF NOT EXISTS Obra (
                                latitud   REAL DEFAULT 0,
                                longitud  REAL DEFAULT 0,
                                radio_error   REAL DEFAULT 99999999,
                                n_gruas   INTEGER DEFAULT 0,
                                direccion TEXT DEFAULT '???',
                                num   TEXT DEFAULT '???',
                                cp    TEXT DEFAULT '???',
                                provincia TEXT DEFAULT '???',
                                comunidad TEXT DEFAULT '???',
                                pais  TEXT DEFAULT '???',
                                uso1  TEXT DEFAULT 'otros' CHECK(uso1 in ('residencial', 'oficina', 'retail', 'terciario', 'hotel', 'otros')),
                                uso2  TEXT DEFAULT 'otros',
                                obra_nueva    INTEGER DEFAULT 1,
                                precio_min   INTEGER DEFAULT 0,
                                precio_medio   INTEGER DEFAULT 0,
                                PRIMARY KEY("latitud","longitud")
                            );"""
                self.cursor.execute(create)
                self.conn.commit()
            except Error as e:
                print(e)
        else:
            raise ConnectionError

    def process_item(self, item, spider):
        sql = 'INSERT INTO Obra VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

        for (key, value) in item.items():
            if isinstance(value, str):
                item[key] = self.remove_special_chars(value.lower())

        self.cursor.execute(sql, 
             (
                item.get("lat"),
                item.get("lon"),
                item.get("err"),
                item.get("gruas"),
                item.get("dir"),
                item.get("num"),
                item.get("cp"),
                item.get("prov"),
                item.get("ca"),
                item.get("pais"),
                item.get("uso1"),
                item.get("uso2"),
                1 if item.get("obra_nueva") else 0,
                item.get("min_price"),
                item.get("avg_price")
             )
            )
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.conn.close()

class CiudadesdesdeelcieloPipeline(object):
    def process_item(self, item, spider):
        return item
