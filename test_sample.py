from playwright.sync_api import sync_playwright, Page
import pytest

@pytest.fixture(autouse=True)
def page() -> Page: # type: ignore
    with sync_playwright() as play:
        browser = play.firefox.launch(args=['--start-maximized'], headless=False)
        page = browser.new_page(no_viewport=True)
        page
        yield page
        page.close()
    
def test_google_1(page:Page):
    page.goto("https://www.google.com")
    print("Chrome browser is opened")
    search_box  = page.locator(selector="//*[@name='q']")
    search_box.fill("Vignesh Dhakshnamoorthy")
    search_box.press("Enter")
    print(page.title())
    page.wait_for_timeout(3000)
    page.go_back()
    search_box.clear()
    search_box.fill("Vignesh Dhesna")
    search_box.press("Enter")
    print(page.title())
    page.wait_for_timeout(3000)

def test_google_2(page:Page):
    page.goto("https://www.bing.com")
    print("Chrome browser is opened")
    print(page.title())
    page.wait_for_timeout(3000)
