import scrapy


class FranceUrl(scrapy.Spider):
    name = 'real'
    start_urls = [
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/',
    ]

    # products-list .product-name font
    def parse(self, response):
        for url in response.css('div.echMdB'):
            yield {
                'page': response,
                'urls': url.css('a.LinkComponent_anchor__2uAhr::attr("href")').get(),
                'Pr': url.css('div.card-price::text').get(),
                #'Size': url.css('li.cNMyen span::text').get(),
                #'Type': url.css('div.message::text').get(),
                'siz': url.xpath('//li/span[@class="VisuallyHiddenstyles__StyledVisuallyHidden-rui__aoql8k-0"]/text()').get(),
                #'Price': url.css('div.Price__Component-rui__x3geed-0::text').get(),
                #'Price': url.xpath('//div[@data-testid="card-price"]/text()').get(),
                ##'Size': url.xpath('//span[@data-testid="screen-reader-value"]/text()').get(),
                ##'Addd1': url.xpath('//div[@data-testid="card-address-1"]/text()').get(),
                ##'Addd2': url.xpath('//div[@data-testid="card-address-2"]/text()').get(),
                #'Address': url.css('h1.LDPHomeFactsstyles__H1-sc-11rfkby-3::text').get(),
                ## 'urls':url.xpath('//h2/a/text()').get(),
            }

        #next_page = response.css('a.page-link::attr("href")').get()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
