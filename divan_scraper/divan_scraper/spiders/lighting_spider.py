import scrapy

class Lighting_Spider(scrapy.Spider):
    name = 'lighting_spider'
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        products = response.css('div._Ud0k')
        for product in products:
            yield {
                'name': product.css('div.lsooF span::text').get(),
                'price': product.css('div.pY3d2 span::text').get(),
                'link': product.css('a').attrib['href']
            }



