from seleniumbase import BaseCase

class ContactTest(BaseCase):
    def test_contact_page(self):
        #  open page
        self.open("https://practice.automationbro.com/contact")
        # fill in all the fields
        self.send_keys('.contact-name input', 'TestName')
        self.send_keys('.contact-email input', 'test@email.com')
        self.send_keys('.contact-phone input', '555-555-1212')
        self.send_keys('.contact-message textarea', 'This is a message')

        # click submit button
        self.click("#evf-submit-277")

        # verify submit button

        self.assert_text("Thanks for contacting us! We will be in touch with you shortly", "div[role=alert]")
