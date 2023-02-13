import scrapy


class DigiSpider(scrapy.Spider):
    name = 'digi'
    allowed_domains = ['herp.careers']
    start_urls = ['https://herp.careers/v1/digitalsaiyo']

    def parse(self, response):
        links = response.css('a.with-heading::attr(href)').getall()
        for link in links:
            url = response.urljoin(link)
            self.logger.info(f'Following link: {url}')
            yield response.follow(url, self.parse_child)

    def parse_child(self, response):
        title =  response.css('h1.requisition-header__name::text').get()
        required_skill = response.xpath('/html/body/main/div[2]/div[3]/div[2]/div').css('div.multiline-text.js-autolink::text').get()
        preferred_skill = response.xpath('/html/body/main/div[2]/div[3]/div[3]/div').css('div.multiline-text.js-autolink::text').get()

        yield {
            'title': title,
            'required_skill': required_skill,
            'preferred_skill':preferred_skill 
        }
        # self.logger.info(f'Parsing child page with title: {title}')