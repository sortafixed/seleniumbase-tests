from page_objects.home_page import HomePage


class HomeTest(HomePage):

    def setUp(self):
        super().setUp()
        print("running before each test")
        # LOGIN
        self.login()
        # open home page
        self.open_page()

    def tearDown(self):
        print("running after each test")

        # Logout
        self.logout()

        super().tearDown()

    def test_home_page(self):

        # assert page title
        self.assert_title("Practice E-Commerce Site – Automation Bro")

        # assert logo
        self.assert_element(self.logo_icon)

        # click on the get started button and assert the url
        self.click(HomePage.get_started_btn)
        get_started_url = self.get_current_url()
        self.assert_equal(get_started_url, "https://practice.automationbro.com/#get-started")
        self.assert_true("get-started" in get_started_url)

        # get the text of the header and assert the value

        self.assert_text("Think different. Make different.", self.heading_text)

        self.scroll_to_bottom()

        self.assert_text("Copyright © 2020 Automation Bro", self.copyright_text)

    def test_menu_links(self):

        expected_links = ['Home', 'About', 'Shop', 'Blog', 'Contact', 'My account']

        # find menu link elements
        # pytest -k "test_menu_links" -s
        menu_links = self.find_elements(self.menu_links)

        # loop through menu links

        for i, link_el in enumerate(menu_links):
            print(i, link_el.text)
            self.assertEqual(expected_links[i], link_el.text)





