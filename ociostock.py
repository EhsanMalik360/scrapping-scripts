from playwright.sync_api import sync_playwright
import pandas as pd
import time


def scrapper(page):


    # page.wait_for_timeout(1000)
    # count = page.query_selector('.top-margin div.small::text()')
    # print(count.inner_text())
    # download = page.query_selector('button.export-to-excel-btn')
    # download.click()
    # page.wait_for_timeout(1000)
    myUrlList = []

    page.wait_for_timeout(1000)
    for i in range(100):  # make the range as long as needed
        page.mouse.wheel(0, 15000)
        time.sleep(5)
        i += 1

    print("Urls")
    urls = page.query_selector_all('.nombreProducto a')
    for url in urls:
        try:
            myurl=url.get_attribute('href')
        except:
            myurl="NA"
        myUrlList.append(myurl)


    """
    print("Titles")

    titles = page.query_selector_all('.textosProducto')
    for title in titles:
        try:
            mytitle=title.inner_text()
        except:
            mytitle="NA"
        print(mytitle)
        mytitleList.append(mytitle)

    print("Brands")
    brands = page.query_selector_all('a.fotoMarca')
    for brand in brands:
        try:
            mybrand=brand.get_attribute('href')
        except:
            mybrand="NA"
        print(mybrand)
        mybrandsList.append(mybrand)

    print("Articles")
    articles = page.query_selector_all('//span[@class="referenciaDatosProducto"]')
    for article in articles:
        try:
            myarticle=article.inner_text()
        except:
            myarticle="NA"
        myarticleList.append(myarticle)

    # print("Eans")
    #eans = page.query_selector_all('.no-margin li:nth-child(2)')
    #for ean in eans:
        # print(ean.inner_text())
        #myeanList.append(ean.inner_text())

    print("Stock")
    stocks = page.query_selector_all('#availability')
    for stock in stocks:
        try:
            print(stock.inner_text())
            mystockList.append(stock.inner_text())
        except:
            mystockList.append("None")

    print("Prices")
    prices = page.query_selector_all('.precio_final')
    for price in prices:
        try:
            print(price.inner_text())
            mypricesList.append(price.inner_text())
        except:
            mypricesList.append("None")
            
            
"""

    df = pd.DataFrame(
        list(zip(myUrlList)),
        columns=['Url'])
    print(df.shape)
    df.to_csv('ocio_urls_5.csv', mode='a', index=False, header=False)

    # print message
    # print("Data appended successfully.")

    #print(page)

    #page.query_selector(
     #   '[id="ctl00_ctl00_ctl00_SiteContent_SiteContent_SiteContent_SolrProductDisplay_BulkPagerBottom_ButtonNext"]').click()
    #page.wait_for_timeout(3500)
    #scrapper(page)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.ociostock.com/')
        page.wait_for_timeout(1000)
        # heading= page.query_selector('//h1/a')
        # print(heading.inner_text())
        page.query_selector('[class="botonPrincipal"]').click()
        login = page.query_selector('#atitLoginTop')
        login.click()
        page.wait_for_timeout(2000)

        # input_acc=page.query_selector('[id="j_accountNumber"]')
        # input_acc.type("100011054")
        input_user = page.query_selector(
            '[name="log"]')
        input_user.type("sourcing@stockyfy.com")
        input_pass = page.query_selector(
            '[name="pas"]')
        input_pass.type("Electro123*")

        page.query_selector(
            '[name="entrar"]').click()
        page.wait_for_timeout(1000)

        # page.query_selector('.dropdown:nth-child(1) .has-arrow').click()

        myurls=[
            "https://www.ociostock.com/funko-lp-1-50-marca-11/",
        ]

        for url in myurls:
            page.goto(url)
            page.wait_for_timeout(1000)
            scrapper(page)
        # page.wait_for_timeout(1000)

        # quotes=page.query_selector_all('[class="quote"]')
        # for quote in quotes:
        #   print(quote.query_selector('.text').inner_text())

        browser.close()


if __name__ == '__main__':
    main()
