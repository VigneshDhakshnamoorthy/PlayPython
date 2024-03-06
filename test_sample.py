from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(autouse=True)
def page():
    with sync_playwright() as play:
        browser = play.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        page.close()
    
def test_google_1(page):
    page.goto("https://www.google.com")
    print("Chrome browser is opened")
    print(page.title())
    page.wait_for_timeout(3000)

def test_google_2(page):
    page.goto("https://www.bing.com")
    print("Chrome browser is opened")
    print(page.title())
    page.wait_for_timeout(3000)
