from seleniumbase import BaseCase


class HomePage(BaseCase):

    logo_icon = ".custom-logo-link"
    get_started_btn = "#get-started"
    heading_text = "h1"
    copyright_text = ".tg-site-footer-section-1"
    menu_links = "//*[@id='primary-menu']//*[starts-with(@id,'menu-item')]"
    username = "#username"
    password = "#password"
    login_btn = "button[name=login]"
    logout_btn = ".woocommerce-MyAccount-content a[href*=logout]"

    def open_page(self):
        self.open("https://practice.automationbro.com")

    def login(self):
        self.open("https://practice.automationbro.com/my-account")
        self.add_text(self.username, "testuser")
        self.add_text(self.password, "PracticeSite123!!")
        self.click(self.login_btn)
        self.assert_text("Log out", ".woocommerce-MyAccount-content")

    def logout(self):
        self.open("https://practice.automationbro.com/my-account")
        self.click(self.logout_btn)
        self.assert_element_visible(self.login_btn)
