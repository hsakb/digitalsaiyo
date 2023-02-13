import scrapy


class DitialsaiyoSpider(scrapy.Spider):
    name = 'ditialsaiyo'
    allowed_domains = ['herp.careers']
    start_urls = ['https://herp.careers/v1/digitalsaiyo']

    def parse(self, response):
	h2_list = response.css('h2.requisition-list-card__header.with-heading__heading.heading::text').getall()
	for h2 in h2_list:
		item = {
			'test': 'test',
			'h2': h2
		}
        	yield item
