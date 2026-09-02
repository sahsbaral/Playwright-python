SauceDemo E-commerce Test Automation
Overview

This project is a UI test automation project built to practice and demonstrate end-to-end testing of an e-commerce application using Python, Playwright, and Pytest.

The tests are written against the SauceDemo application and cover important user flows from login through product selection, cart management, checkout, and order confirmation.

The main goal of this project is to build practical experience in writing reliable UI automation tests while following common QA practices.

Application Under Test

SauceDemo
https://www.saucedemo.com/

SauceDemo is a demo e-commerce application that provides common shopping workflows such as authentication, product browsing, cart management, and checkout.

Tech Stack
Python
Playwright
Pytest
Git
GitHub
VS Code
Testing Scope
Login

The login test suite covers:

Successful login with valid credentials
Login with invalid credentials
Empty username validation
Empty password validation
Login button state
Products and Cart

The product and cart tests cover:

Products page visibility
Adding a product to the cart
Verifying the cart badge
Verifying a product in the cart
Removing a product from the cart
Verifying an empty cart
Checkout

The checkout tests cover:

Navigating to the checkout page
Checkout information field visibility
Valid checkout information
First Name validation
Last Name validation
Postal Code validation
Checkout Overview verification
Product verification
Price verification
Completing an order
Order confirmation
Returning to the Products page
Project Structure
playwright-python/
│
├── tests/
│   ├── first_test.py
│   ├── test_login.py
│   ├── test_products.py
│   └── test_checkout.py
│
├── .gitignore
├── requirements.txt
└── README.md
Test Approach

The tests are designed around common QA principles such as:

Functional testing
Positive and negative test scenarios
UI validation
Form validation
End-to-end testing
Assertions for expected application behavior
Independent test execution

Playwright locators such as roles, placeholders, text, and CSS selectors are used to interact with and validate elements on the application.

Installation and Setup
1. Clone the repository
git clone <your-github-repository-url>
cd playwright-python
2. Create a virtual environment
python -m venv venv
3. Activate the virtual environment

Windows:

venv\Scripts\activate
4. Install dependencies
python -m pip install -r requirements.txt
5. Install Playwright browsers
python -m playwright install
Running the Tests

Run the complete test suite:

pytest -v

Run a specific test file:

pytest tests/test_login.py -v
pytest tests/test_products.py -v
pytest tests/test_checkout.py -v
Test Credentials

This project uses the publicly available SauceDemo test account:

Username: standard_user
Password: secret_sauce

These credentials are provided by the demo application and are used only for testing purposes.

Future Improvements

The project is currently being developed as a learning and portfolio project. Planned improvements include:

Pytest fixtures for reusable setup
Page Object Model implementation
Test data management
Parameterized testing
HTML test reports
Screenshots and traces for failed tests
API testing
Database validation using SQL
GitHub Actions for CI/CD
Cross-browser test execution