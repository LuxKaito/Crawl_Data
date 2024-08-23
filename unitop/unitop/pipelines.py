# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import json
# from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv

class JsonDBUnitopPipeline:
    def process_item(self, item, spider):
        with open('jsondataunitop.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(line)
        return item

class CSVDBUnitopPipeline:
    '''
    mỗi thông tin cách nhau với dấu $
    Ví dụ: coursename$lecturer$intro$describe$courseUrl
    Sau đó, cài đặt cấu hình để ưu tiên Pipline này đầu tiên
    '''
    def process_item(self, item, spider):
        with open('csvdataunitop.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter='$')
            writer.writerow([
                item['coursename'],
                item['lecturer'],
                item['intro'],
                item['describe'],
                item['courseUrl'],
                item['votenumber'],
                item['rating'],
                item['newfee'],
                item['oldfee'],
                item['lessonnum']
            ])
        return item
    pass
