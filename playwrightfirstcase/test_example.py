from playwright.sync_api import sync_playwright

class MyAutomation:
    def __init__(self):
        self.browser = None
        self.page = None

    def launch_browser(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch()
            self.page = self.browser.new_page()
            self.page.goto('https://example.com')

    def click_element_by_xpath(self, xpath):
        if not self.page:
            raise Exception('Browser not launched. Call launch_browser() first.')
        
        self.page.click(xpath)

    def fill_input_by_selector(self, selector, value):
        if not self.page:
            raise Exception('Browser not launched. Call launch_browser() first.')
        
        self.page.fill(selector, value)

    def close_browser(self):
        if self.browser:
            self.browser.close()

# Example usage:
automation = MyAutomation()
automation.launch_browser()
automation.click_element_by_xpath('//button[@id="myButtonId"]')
automation.fill_input_by_selector('input[name="username"]', 'JohnDoe')
automation.close_browser()
