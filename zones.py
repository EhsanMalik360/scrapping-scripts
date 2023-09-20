from playwright.sync_api import sync_playwright
import pandas as pd
def scrapper(page):
    page.wait_for_timeout(500)




    #download = page.query_selector('button.export-to-excel-btn')
    #download.click()
    #page.wait_for_timeout(1000)

    myurlList = []
    mytitleList = []
    mystockList = []
    mybrandsList = []
    myskusList = []
    mympnsList = []
    mypricesList = []


    #print("Urls")
    urls = page.query_selector_all('a.on')
    for url in urls:
        #print(url.get_attribute('href'))
        myurlList.append(url.get_attribute('href'))
        
    #print("Titles")
    titles = page.query_selector_all('.on')
    for title in titles:
        #print(title.inner_text())
        mytitleList.append(title.inner_text())
    """
    print("Stocks")
    stocks = page.query_selector_all('.productStockLevel')
    for stock in stocks:
        print(stock.inner_text())
        mystockList.append(stock.inner_text())

    print("Brands")
    brands = page.query_selector_all('.brandBlock')
    for brand in brands:
        print(brand.inner_text())
        mybrandsList.append(brand.inner_text())

   
    """

    #print("Skus")
    skus = page.query_selector_all('.zcd-sku-number')
    for sku in skus:
        #print(sku.inner_text())
        myskusList.append(sku.inner_text())

    #print("Mpns")
    mpns = page.query_selector_all('.mfr_text')
    for mpn in mpns:
        #print(mpn.inner_text())
        mympnsList.append(mpn.inner_text())


    #print("Prices")
    prices = page.query_selector_all('.product-price')
    for price in prices:
        #print(price.inner_text())
        mypricesList.append(price.inner_text())


    df = pd.DataFrame(list(zip(myurlList, mytitleList, mympnsList, myskusList, mypricesList)),
              columns=['Url', 'Title', 'MPN', 'SKU', 'Price'])
    #print(df)
    # append data frame to CSV file
    df.to_csv('zoneveritasrerun.csv', mode='a', index=False, header=False)

    # print message
    try:
        nextpage = page.query_selector('.serp-results+ .serp-pagination .next')
        nextpage.click()
        page.wait_for_timeout(1000)
        scrapper(page)
    except:
        print("End of Pagination")



def main():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://www.zones.com/site/locate/refine.html?Ntx=mode+matchallpartial&Ntk=BasicSearch&Ne=689&N=4294965887&Ntt=1&preserve=true')
        page.wait_for_timeout(1000)
        """
        #heading= page.query_selector('//h1/a')
        #print(heading.inner_text())
        page.query_selector('[id="cookiescript_accept"]').click()
        login=page.query_selector('.loginHeaderLink')
        login.click()
        page.wait_for_timeout(1000)

        input_acc=page.query_selector('[id="j_accountNumber"]')
        input_acc.type("100011054")
        input_user=page.query_selector('[id="j_username"]')
        input_user.type("purchase@stockyfy.com")
        input_pass = page.query_selector('[id="j_password"]')
        input_pass.type("bZ*dwYb347WKX@SAP")

        page.query_selector('[id="loginSubmit"]').click()
        page.wait_for_timeout(1000)
"""
        #page.query_selector('//*[@href="https://www.zones.com/site/locate/search.html?N=4294963558+22401"]').click()

        page.wait_for_timeout(1000)

       # page.query_selector('//*[@href="/Laptops/Chromebooks/c/CHROMEBOOK"]').click()
        scrapper(page)

        #quotes=page.query_selector_all('[class="quote"]')
        #for quote in quotes:
         #   print(quote.query_selector('.text').inner_text())





        browser.close()


if __name__=='__main__':
    main()
