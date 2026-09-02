from playwright.sync_api import Page, expect
#Products Page Visibility
def test_products_page_visibility(page:Page): 
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

#All Products Visible
# Verify all products are displayed
def test_all_products_displayed(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    products = page.locator(".inventory_item")

    assert products.count() == 6

#Add the First Item to the Cart and Verify the Cart Badge
def test_add_to_cart(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_role("button",name="Add to cart").first.click()
    expect(
        page.locator(".shopping_cart_badge")).to_have_text("1")
    
 #Verify the product in a Cart 
def test_product_visible_in_cart(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button",name="Add to cart").click()

    page.locator(".shopping_cart_link").click()
    expect(
        page.get_by_text("Sauce Labs Backpack")
    ).to_be_visible()

    #Remove the product from the cart and verify that the cart is empty
def test_remove_product_from_cart(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name= "Add to cart").click()

    page.locator(".shopping_cart_link").click()
    page.get_by_role("button",name="Remove").click()
    #Verify product is removed
    expect( 
        page.get_by_text("Sauce Labs Backpack")
    ).to_be_hidden()
    
    #Verify whether the cart badge is gone or not
    expect(
        page.locator(".shopping_cart_badge")
        ).not_to_be_visible()
    