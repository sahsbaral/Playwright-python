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

#Verify that all product names are displayed correctly
def test_product_names(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    #Now check the real names of the products displayed
    expected_products=["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket","Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)"]
    products=page.locator(".inventory_item_name") 
    #There is a diff between ".inventory_item" and ".inventory_item_name".
    #The first one gives the whole card information while the second one gives Product Names specifically.
    assert products.all_text_contents() == expected_products

#Verify all the correct prices are displayed
def test_verify_prices(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    expected_prices=["$29.99","$9.99","$15.99","$49.99","$7.99","$15.99"]
    products=page.locator(".inventory_item_price")

    assert products.all_text_contents() == expected_prices

#Products Sorting A-Z
def test_products_sort_az (page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    expected_products_after_az=["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket","Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)"]

    #This code only sorts the product in A-Z format
    page.locator(".product_sort_container").select_option("az")

# After sorting, locate all the product names
    products= page.locator(".inventory_item_name")

    assert products.all_text_contents() == expected_products_after_az

#Products Sorting Z-A
def test_products_sort_za (page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    expected_products_after_za=["Test.allTheThings() T-Shirt (Red)","Sauce Labs Onesie","Sauce Labs Fleece Jacket","Sauce Labs Bolt T-Shirt","Sauce Labs Bike Light","Sauce Labs Backpack"]

    #This code only sorts the product in Z-A format
    page.locator(".product_sort_container").select_option("za")

# After sorting, locate all the product names
    products=page.locator(".inventory_item_name")

    #Assert and Check
    assert products.all_text_contents() == expected_products_after_za

#After Sorting Prices, Low -> High
def test_price_lowhigh (page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    expected_prices_lh=["$7.99","$9.99","$15.99","$15.99","$29.99","$49.99"]

 #Sort The Prices from Low to High
    page.locator(".product_sort_container").select_option("lohi")

# After sorting, locate all the product names
    products=page.locator(".inventory_item_price")

# Verify actual product prices match the expected low-to-high order
    assert products.all_text_contents() == expected_prices_lh

#After Sorting Prices, High -> Low
def test_price_highlow (page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    expected_prices_hl=["$49.99","$29.99","$15.99","$15.99","$9.99","$7.99"]

 #Sort The Prices from High to Low
    page.locator(".product_sort_container").select_option("hilo")

# After sorting, locate all the product names
    products=page.locator(".inventory_item_price")

# Verify actual product prices match the expected low-to-high order
    assert products.all_text_contents() == expected_prices_hl

    
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

#Add Multiple Products in Cart and Verify
def test_multiple_products_to_cart(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button",name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

#Sort the Products List to be shown acc to the price Low -> High
    page.locator(".product_sort_container").select_option("lohi")

 #After the sorting, choose 3 products 
    page.get_by_role("button",name="Add to Cart").nth(0).click()
    page.get_by_role("button",name="Add to Cart").nth(1).click()
    page.get_by_role("button",name="Add to Cart").nth(2).click()

#Verfiy the Shopping Cart Badge shows 3
    expect(
    page.locator(".shopping_cart_badge")
    ).to_have_text("3")

# Verify multiple products are visible in the cart
def test_multiple_products_in_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    #Sort the Products List to be shown acc to the price Low -> High
    page.locator(".product_sort_container").select_option("lohi")

    # Add three products after sorting
    page.get_by_role("button", name="Add to cart").nth(0).click()
    page.get_by_role("button", name="Add to cart").nth(1).click()
    page.get_by_role("button", name="Add to cart").nth(2).click()

    # Open cart
    page.locator(".shopping_cart_link").click()

    # Verify the three products are visible
    expect(
        page.get_by_text("Sauce Labs Onesie")
    ).to_be_visible()

    expect(
        page.get_by_text("Sauce Labs Bike Light")
    ).to_be_visible()

    expect(
        page.get_by_text("Sauce Labs Bolt T-Shirt")
    ).to_be_visible()

#Remove one product and verify the shopping cart badge and the product should be hidden as well..
def test_remove_one_product_from_cart(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    #Sort the Products List to be shown acc to the price Low -> High
    page.locator(".product_sort_container").select_option("lohi")

    # Add the 1st lowest-priced product
    page.locator(".inventory_item").nth(0).get_by_role(
    "button", name="Add to cart"
    ).click()

    # Add the 2nd lowest-priced product
    page.locator(".inventory_item").nth(1).get_by_role(
    "button", name="Add to cart"
    ).click()

    # Add the 3rd lowest-priced product
    page.locator(".inventory_item").nth(2).get_by_role(
    "button", name="Add to cart"
    ).click()

    # Open cart
    page.locator(".shopping_cart_link").click()

    #Verify whether the products are there in a cart or notttt..
    expect( 
            page.get_by_role("link",name="Sauce Labs Onesie")
        ).to_be_visible()
    
    expect(
            page.get_by_role("link",name="Sauce Labs Bike Light")
        ).to_be_visible()
    
    expect(
            page.get_by_role("link",name="Sauce Labs Bolt T-Shirt")
        ).to_be_visible()

    #Remove One Product from cart
    page.locator("#remove-sauce-labs-bolt-t-shirt").click() 

#After the Removal, the cart badge should show 3->2s
    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("2")

#Since i removed the Sauce Labs Bolt Tshirts, It should be hidden from the page 
    expect(
        page.get_by_role("link",name="Sauce Labs Bolt T-Shirt")
    ).to_be_hidden()

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
    