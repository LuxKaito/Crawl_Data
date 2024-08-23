import scrapy
from unitop.items import UnitopItem

class UnitopCourseSpider(scrapy.Spider):
    name = "UnitopAppCrawler"
    allowed_domains = ["unitop.vn"]

    def start_requests(self):
        yield scrapy.Request(url='https://unitop.vn/', callback=self.parse)
        
    def parse(self, response):
        courseList = response.xpath('//div[@class="box-body"]/descendant::ul/li/div/a/@href').getall()
        for courseItem in courseList:
            item = UnitopItem()
            item['courseUrl'] = response.urljoin(courseItem)
            request = scrapy.Request(url = response.urljoin(courseItem), callback=self.parseCourseDetailPage)
            request.meta['datacourse'] = item
            yield request
            
    def parseCourseDetailPage(self, response):
        item = response.meta['datacourse']
        item['coursename'] = response.xpath('normalize-space(string(//h1))').get()
        item['lecturer'] = response.xpath('normalize-space(string(//a[@class="mentor"]))').get()
        item['intro'] = response.xpath('normalize-space(string(//div[@class="col-12"]/p[@class="course-desc"]))').get()
        item['describe'] = response.xpath('normalize-space(string(//div[@class="info-body"]/p))').get()
        votenumber = response.xpath('normalize-space(string(//*[@id="intro-head"]/div/div/div/div/div[1]/span))').get()
        votenumber = ''.join(filter(str.isdigit, votenumber))
        
        item['votenumber'] = votenumber
        
        start = response.xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]').get()
        sel = scrapy.Selector(text=start)
        item['rating'] = len(sel.xpath('//i').getall())
        item['newfee'] = response.xpath('normalize-space(string(//*[@id="reg-course"]/div/div[1]/span[1]))').get()
        item['oldfee'] = response.xpath('normalize-space(string(//*[@id="reg-course"]/div/div[1]/span[2]))').get()
        lessonnum = response.xpath('normalize-space(string(//*[@id="course-includes"]/li[1]/text()))').get()
        lessonnum = ''.join(filter(str.isdigit, lessonnum))
        item['lessonnum'] = lessonnum
        yield item