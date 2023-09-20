from playwright.sync_api import sync_playwright
import pandas as pd
def scrapper(page):
    page.wait_for_timeout(3000)
    #download = page.query_selector('button.export-to-excel-btn')
    #download.click()
    #page.wait_for_timeout(1000)

    mytitleList = []
    mystockList = []
    mybrandsList = []
    myskusList = []
    mympnsList = []
    mypricesList = []

    print("Titles")
    titles = page.query_selector_all('.productMainLink')
    for title in titles:
        print(title.inner_text())
        mytitleList.append(title.inner_text())

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

    print("Skus")
    skus = page.query_selector_all('.skuBlock')
    for sku in skus:
        print(sku.inner_text())
        myskusList.append(sku.inner_text())

    print("Mpns")
    mpns = page.query_selector_all('.mpnBlock')
    for mpn in mpns:
        print(mpn.inner_text())
        mympnsList.append(mpn.inner_text())

    page.wait_for_timeout(3000)

    print("Prices")
    prices = page.query_selector_all('.list-view-item .product-list-price.InnerProductListItem .PLPInnerRight .price')
    for price in prices:
        print(price.inner_text())
        mypricesList.append(price.inner_text())


    df = pd.DataFrame(list(zip(mytitleList, mympnsList, myskusList, mypricesList, mybrandsList, mystockList)),
                      columns=['Title', 'MPN', 'SKU', 'Price', 'Brands', 'Stock'])
    print(df)
    # append data frame to CSV file
    df.to_csv('exert.csv', mode='a', index=False, header=False)

    # print message
    print("Data appended successfully.")
    try:
        nextpage = page.query_selector('li.next a')
        nextpage.click()
        page.wait_for_timeout(1000)
        scrapper(page)
    except:
        print("End of Pagination")



def main():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        page.goto('https://store.exertis.co.uk/')
        page.wait_for_timeout(1000)
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

        page.query_selector('//*[@href="/"]').click()

        page.wait_for_timeout(1000)

        page.query_selector('//*[@href="/Laptops/Chromebooks/c/CHROMEBOOK"]').click()
        scrapper(page)

        #quotes=page.query_selector_all('[class="quote"]')
        #for quote in quotes:
         #   print(quote.query_selector('.text').inner_text())





        browser.close()


if __name__=='__main__':
    main()
