# Tichi Login Automation (Task 3 – Optional)

Automated regression suite for the **Login** functionality of the Tichi
application, built with **Python + Selenium + pytest**, using the **Page
Object Model** pattern for maintainability.

## Project Structure

```
automation/
├── pages/
│   └── login_page.py      # Page Object for the Login page (locators + actions)
├── tests/
│   ├── conftest.py         # WebDriver fixture, config, test credentials fixture
│   └── test_login.py       # Test cases covering login scenarios
├── reports/                 # HTML execution report is generated here
├── pytest.ini
├── requirements.txt
└── README.md
```

## What is covered

| Test | Maps to Test Case |
|---|---|
| Valid login | TC_LOGIN_01 |
| Incorrect password | TC_LOGIN_02 |
| Unregistered email | TC_LOGIN_03 |
| Invalid email formats (parametrized: 5 variants) | TC_LOGIN_04 (regression for Defect DR-001) |
| Empty email | TC_LOGIN_05 |
| Empty password | TC_LOGIN_06 |
| Both fields empty | TC_LOGIN_07 |
| Email case-insensitivity | TC_LOGIN_13 |
| Password case-sensitivity | TC_LOGIN_14 |
| Forgot Password navigation | TC_LOGIN_15 |
| Sign Up link navigation | TC_LOGIN_16 |
| XSS payload sanitization | TC_LOGIN_29 |

## Setup

```bash
cd automation
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

You also need a **Chrome browser** and matching **chromedriver** on your
PATH (or use `webdriver-manager`, already listed in requirements.txt — see
the note in `conftest.py` if you want it to auto-manage the driver binary).

## Before running

The assignment states no credentials are provided, so:

1. Manually sign up for one test account on the staging app.
2. Provide those credentials to the suite via environment variables:

```bash
export TICHI_TEST_EMAIL="your_test_account@example.com"
export TICHI_TEST_PASSWORD="YourTestPassword123!"
```

## Running the suite

```bash
pytest
```

This generates a self-contained HTML execution report at:
`reports/execution_report.html`

Run only the smoke tests:
```bash
pytest -m smoke
```

## Important note on locators and execution

The exact DOM structure (element `id`/`name`/`class` attributes) of the
live Tichi staging app could not be inspected from the environment used to
prepare this submission (no browser/network access available there), so
`pages/login_page.py` uses a **layered locator strategy** (tries `id`,
then `name`, then common CSS/XPath patterns) to make the suite resilient
and easy to adapt. Before running the suite for real:

1. Open the app in a browser, inspect the Login page elements.
2. Confirm/update the `SELECTOR_CANDIDATES` lists at the top of
   `pages/login_page.py` to match the real attributes if they differ.
3. Run `pytest` to execute the suite and produce the real HTML report in
   `reports/execution_report.html`.

This structure means once locators are confirmed, no other file needs to
change to get accurate pass/fail results.
