import scrapy


class FranceUrl(scrapy.Spider):
    name = 'realsold'
    start_urls = [
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-23',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-24',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-25',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-26',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-27',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-28',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-29',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-30',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-31',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-32',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-33',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-34',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-35',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-36',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-37',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-38',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-39',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-40',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-41',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-42',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-43',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-44',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-45',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-46',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-47',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-48',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-49',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-50',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-51',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-52',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-53',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-54',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-55',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-56',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-57',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-58',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-59',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-60',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-61',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-62',
        'https://www.realtor.com/realestateandhomes-search/North-Carolina/type-land/show-recently-sold/pg-63',
    ]

    # products-list .product-name font
    def parse(self, response):
        for url in response.css('div.BasePropertyCard_propertyCardWrap__J0xUj'):
            yield {
                'urls': url.css('div.CardContent__StyledCardContent-rui__sc-7ptz1z-0 a::attr("href")').get(),
                'Sold': url.css('div.message::text').get(),
                #'Type': url.xpath('//div[@data-testid="forsale"]/text()').get(),
                #'Price': url.css('div.Price__Component-rui__x3geed-0::text').get(),
                'Price': url.xpath('//div[@data-testid="card-price"]/text()').get(),
                'Size': url.xpath('//span[@data-testid="screen-reader-value"]/text()').get(),
                'Addd1': url.xpath('//div[@data-testid="card-address-1"]/text()').get(),
                'Addd2': url.xpath('//div[@data-testid="card-address-2"]/text()').get(),
                #'Address': url.css('h1.LDPHomeFactsstyles__H1-sc-11rfkby-3::text').get(),
                ## 'urls':url.xpath('//h2/a/text()').get(),
            }

        #next_page = response.css('a.page-link::attr("href")').get()
        #if next_page is not None:
        #    yield response.follow(next_page, self.parse)
