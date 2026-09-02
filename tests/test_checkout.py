from playwright.sync_api import Page, expect
#Login Page -> Products Page
def test_checkout(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()    
    expect (
        page.get_by_text("Products")
    ).to_be_visible()
#Click on the Sauce Labs Backpack and Add it to the Cart..the Cart Badge should show 1
    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button",name="Add to cart").click()
    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")

    page.locator(".shopping_cart_link").click()
#Click on the Checkout Button and Verify the Page Information
    page.get_by_role("button",name="Checkout").click()
    expect(
        page.get_by_text("Checkout: Your Information")
).to_be_visible()

#Verfiy that Checkout Information Fields are Visible 
def test_checkout_information_field_visible(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()
    expect(
    page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    #Open Cart
    page.locator(".shopping_cart_link").click()

    #ClickCheckout
    page.get_by_role("button",name="Checkout").click()

    #Verify Fields
    #FirstName
    expect(
        page.get_by_placeholder("First Name")
    ).to_be_visible()

    #LastName
    expect(
        page.get_by_placeholder("Last Name")
    ).to_be_visible()

    #Zip/PostalCode
    expect(
        page.get_by_placeholder("Zip/Postal Code")
    ).to_be_visible()

 #Enter the valid information in the available fields and continue

def test_checkout_information_field_filled(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()
    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    #Open Cart
    page.locator(".shopping_cart_link").click()

    #ClickCheckout
    page.get_by_role("button",name="Checkout").click()

    #EntertheFirstName
    page.get_by_placeholder("First Name").fill("Samikshya")
    page.get_by_placeholder("Last Name").fill("Baral")
    page.get_by_placeholder("Zip/Postal Code").fill("531965")

    page.get_by_role("button",name="Continue").click()
    expect(
        page.get_by_text("Checkout: Overview")
    ).to_be_visible()

#Empty FirstName Validation
def test_empty_firstname(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()
    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    #Open Cart
    page.locator(".shopping_cart_link").click()

    #ClickCheckout
    page.get_by_role("button",name="Checkout").click()

    #EmptyFirstName
    page.get_by_placeholder("Last Name").fill("Baral")
    page.get_by_placeholder("Zip/Postal Code").fill("531965")

    page.get_by_role("button",name="Continue").click()
    expect (
        page.get_by_text("Error: First Name is required")
    ).to_be_visible()

    #EmptyLastName
def test_empty_lastname(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()
    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    #Open Cart
    page.locator(".shopping_cart_link").click()

    #ClickCheckout
    page.get_by_role("button",name="Checkout").click()

    page.get_by_placeholder("First Name").fill("Samikshya")
    page.get_by_placeholder("Zip/Postal Code").fill("531965")
    
    page.get_by_role("button",name="Continue").click()
    expect (
        page.get_by_text("Error: Last Name is required")
        ).to_be_visible()

    #Empty Postal Code
def test_empty_postal_code(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()
    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    #Open Cart
    page.locator(".shopping_cart_link").click()

    #ClickCheckout
    page.get_by_role("button",name="Checkout").click()

    page.get_by_placeholder("First Name").fill("Samikshya")
    page.get_by_placeholder("Last Name").fill("Baral")
        
    page.get_by_role("button",name="Continue").click()
    expect(
        page.get_by_text("Error: Postal Code is required")
    ).to_be_visible()

#Verfiy Checkout Overview Page
def test_complete_checkout(page:Page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button",name="Login").click()
    expect(
        page.get_by_text("Products")
    ).to_be_visible()

    page.get_by_text("Sauce Labs Backpack").click()
    page.get_by_role("button", name="Add to cart").click()

    #Open Cart
    page.locator(".shopping_cart_link").click()

    #ClickCheckout
    page.get_by_role("button",name="Checkout").click()

    #EntertheFirstName
    page.get_by_placeholder("First Name").fill("Samikshya")
    page.get_by_placeholder("Last Name").fill("Baral")
    page.get_by_placeholder("Zip/Postal Code").fill("531965")

    #Verify Checkout Overview is Seen
    page.get_by_role("button",name="Continue").click()
    expect(
        page.get_by_text("Checkout: Overview")
    ).to_be_visible()

    #Verify Product
    expect(
    page.get_by_text("Sauce Labs Backpack")
    ).to_be_visible()

    #Verify Price
    expect(
        page.get_by_text("Item total: $29.99")
    ).to_be_visible()

    #ClickOnFinish
    page.get_by_role("button",name="Finish").click()
    expect(
        page.get_by_text("Checkout: Complete!")
    ).to_be_visible()

    expect(
        page.get_by_text("Thank you for your order!")
    ).to_be_visible()

  #After Order Confirmation, Click on Back Home ; should redirect to product page
    page.get_by_role("button",name="Back Home").click()
    expect(
        page.get_by_text("Products")
    ).to_be_visible()