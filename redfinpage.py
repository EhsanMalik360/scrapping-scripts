import scrapy


class FranceUrl(scrapy.Spider):
    name = 'redfinpage'

    # products-list .product-name font
    start_urls = [
        'https://www.redfin.com/county/2262/OK/Coal-County/filter/property-type=land,include=sold-3mo',

    ]
    def parse(self, response):
        for url in response.css('div.descriptionAndModeContainer'):
            yield {
                'page': response,
                'entries': url.css('div.homes::text').getall(),

                ##'urls': url.css('div.property-card-data a::attr("href")').get(),
                ##'ad': url.css('div.property-card-data a address::text').get(),
                ##'pr': url.css('div.kSsByo span::text').get(),
                ##'sz': url.css('ul.eYPFID li b::text').get(),
               # 'soldate': url.css('div.eclXWV span::text').get(),

                #'Type': url.css('div.message::text').get(),
                ##'Sold Date': url.xpath('//span[@class="ehTgwE"]/text()').get(),
                #'Price': url.css('div.Price__Component-rui__x3geed-0::text').get(),
                ##'Price': url.xpath('//span[@data-test="property-card-price"]/text()').get(),
                #'Size': url.xpath('//span[@data-testid="screen-reader-value"]/text()').get(),
                ##'LandSize': url.css('ul.StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 li b::text').get(),
                ##'Addd1': url.xpath('//div/a[@class="jnnxAW"]/address/text()').get(),
                #'Addd2': url.xpath('//div[@data-testid="card-address-2"]/text()').get(),
                #'Address': url.css('h1.LDPHomeFactsstyles__H1-sc-11rfkby-3::text').get(),
                ## 'urls':url.xpath('//h2/a/text()').get(),
            }

        #next_page = response.css('a.StyledButton-c11n-8-84-3__sc-wpcbcc-0::attr("href")').get()
        #if next_page is not None:
         #   yield response.follow(next_page, self.parse)
