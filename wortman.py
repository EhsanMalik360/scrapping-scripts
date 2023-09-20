from playwright.sync_api import sync_playwright
import pandas as pd


def scrapper(page):

    page.wait_for_timeout(2000)


    # page.wait_for_timeout(1000)
    # count = page.query_selector('.top-margin div.small::text()')
    # print(count.inner_text())
    # download = page.query_selector('button.export-to-excel-btn')
    # download.click()
    # page.wait_for_timeout(1000)
    myUrlList = []
    mytitleList = []
    # mystockList = []
    mybrandsList = []
    myreferenceList = []
    myeanList = []
    mypricesList = []
    myarticleList = []

    #print("Urls")
    urls = page.query_selector_all('.product-description a')
    for url in urls:
        #print(url)
        myUrlList.append(url)

    #print("Titles")
    titles = page.query_selector_all('.product-description a')
    for title in titles:
        #print(title.inner_text())
        mytitleList.append(title.inner_text())

    #print("Brands")
    brands = page.query_selector_all('.no-margin li:nth-child(1)')
    for brand in brands:
        #print(brand.inner_text())
        mybrandsList.append(brand.inner_text())

    #print("Articles")
    articles = page.query_selector_all('.product-description .list-unstyled li')
    for article in articles:
        #print(article.inner_text())
        myarticleList.append(article.inner_text())

    #print("Eans")
    eans = page.query_selector_all('.no-margin li:nth-child(2)')
    for ean in eans:
        #print(ean.inner_text())
        myeanList.append(ean.inner_text())

    #print("References")
    references = page.query_selector_all('.no-margin li:nth-child(3)')
    for reference in references:
        #print(reference.inner_text())
        myreferenceList.append(reference.inner_text())

    #print("Prices")
    prices = page.query_selector_all('h2.no-margin')
    for price in prices:
        #print(price.inner_text())
        mypricesList.append(price.inner_text())

    df = pd.DataFrame(
        list(zip(myUrlList, mytitleList, myarticleList, mybrandsList, mypricesList, myreferenceList, myeanList)),
        columns=['Url', 'Title', 'Article', 'Brand', 'Price', 'Reference', 'Ean'])
    print(df.shape)
    df.to_csv('wortman.csv', mode='a', index=False, header=False)


    # print message
    #print("Data appended successfully.")
    
    


    print(page)



    page.query_selector('[id="ctl00_ctl00_ctl00_SiteContent_SiteContent_SiteContent_SolrProductDisplay_BulkPagerBottom_ButtonNext"]').click()
    page.wait_for_timeout(3500)
    scrapper(page)



def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.wortmann.de/')
        page.wait_for_timeout(2000)
        #heading= page.query_selector('//h1/a')
        #print(heading.inner_text())
        #page.query_selector('[id="cookiescript_accept"]').click()
        login=page.query_selector('#ctl00_ctl00_ctl00_LoginViewContainer_LoginLink')
        login.click()
        page.wait_for_timeout(1000)

        #input_acc=page.query_selector('[id="j_accountNumber"]')
        #input_acc.type("100011054")
        input_user=page.query_selector('[id="ctl00_ctl00_ctl00_SiteContent_SiteContent_SiteContent_B2xPanel1_B2CLoginControl1_LoginControl_UserName"]')
        input_user.type("purchase@stockyfy.com")
        input_pass = page.query_selector('[id="ctl00_ctl00_ctl00_SiteContent_SiteContent_SiteContent_B2xPanel1_B2CLoginControl1_LoginControl_Password"]')
        input_pass.type("4rjmrcib")

        page.query_selector('[id="ctl00_ctl00_ctl00_SiteContent_SiteContent_SiteContent_B2xPanel1_B2CLoginControl1_LoginControl_LoginButton"]').click()
        page.wait_for_timeout(2000)

        #page.query_selector('.dropdown:nth-child(1) .has-arrow').click()

        #page.wait_for_timeout(1000)
        page.goto('https://www.wortmann.de/de-de/product/distri_cable_ch/2010015/intel-cable-sff-8611-straight-to-right-angle-530mm.aspx')
        # page.query_selector('//*[@href="/en-US/search.aspx?q=*&attributes_producttype=2813&category=DISTRI_PERI_DA&attributes_1031_da_1_a00630=Wortmann"]').click()
        page.wait_for_timeout(8000)

        scrapper(page)

        # quotes=page.query_selector_all('[class="quote"]')
        # for quote in quotes:
        #   print(quote.query_selector('.text').inner_text())

        browser.close()


if __name__ == '__main__':
    main()
