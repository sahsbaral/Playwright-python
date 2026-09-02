from playwright.sync_api import Page, expect


def test_valid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

def test_invalid_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("invalid_password")

    page.locator("#login-button").click()
    expect (
    page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()
    
def test_loginbutton_is_enabled(page:Page):
    page.goto("https://www.saucedemo.com/")

    expect(
        page.get_by_role("button",name="Login")
    ).to_be_enabled()

def test_empty_username(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Epic sadface: Username is required")
    ).to_be_visible()

def test_empty_password(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("")

    page.get_by_role("button",name="Login").click()
    expect(
        page.get_by_text("Epic sadface: Password is required")
    ).to_be_visible()