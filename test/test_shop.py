from page_objects.shop_page import ShopPage
from selenium.common.exceptions import NoSuchElementException

# pytest -k test_search --dashboard
# pytest --html=report.html
# pytest -k ShopTest --browser=firefox
# pytest -n=3 --browser=firefox --html=report.html
# pytest -k ShopTest --headless
# pip freeze > requirements.txt



class ShopTest(ShopPage):
    def test_search_products(self):
        # open page
        self.open_page()

        # search for prod

        self.send_keys(self.search_input, "Sunglasses")
        self.click(self.search_btn)

        # assert product image
        try:
            self.assert_element(self.product_img)
        except NoSuchElementException:
            self.assert_text("No products were found matching your selection." , self.no_products_txt)


