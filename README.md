# qawa ☕

`qawa` stands for `QA Web Automation.`

It is a `template project` using Selenium that will help you quickly start writing maintainable UI tests for your web projects.

## Setup

After cloning, navigate to the repo folder and do the following:

#### Venv
* `python3 -m venv env`
* `source env/bin/activate`

#### Dependencies
* `pip install -r requirements.txt`

#### Precommit hook
* `pre-commit install`

#### Drivers
Documentation and download links:

* [ChromeDriver](https://chromedriver.chromium.org/) (or `brew install chromedriver`)
* [geckodriver](https://github.com/mozilla/geckodriver/releases) (or `brew install geckodriver`)

## Project structure
This project uses the `page object pattern`.

It is structured into 3 main packages:

* `pages`
    * Contains page classes.
    * All page classes should inherit from `BasePage`.
* `tests`
    * Contains the tests themselves.
    * All test classes should inherit from `BaseTest`
* `utilities`
    * `config.py` is used for defining the project-specific constants.
    * The rest are helper modules.
* `common`
    * `test_data.py` is used for defining various test data per environment.
    * `helpers.py` is used for various small, helpful functions.

Logging artifacts are stored in the following folders:

* `reports`
* `screenshots`

The test runner is found in the project root as:

* `runner.py`

Dependencies can be found in the project root as:

* `requirements.txt`

## Minimum setup for running tests
1. Change `URLS` in `config.py`.
2. Change the `PROJECT_NAME` and `REPORT_NAME` in `config.py`.
3. Create a page object class extending `BasePage` in the `pages` package.
4. Create a test class extending `BaseTest` in the `tests` package.
5. Run the test suite: `python3 runner.py` 

Examples of a page object class and a test class are provided.

All test methods need to be prefixed with `test_` in order to be automatically discovered by the test loader in `runner.py`.
An individual test can also be run by right-clicking on it and selecting "Run Unittests for..."

## Interface for specifying options
- Chrome is the default browser, but here is the full list of supported browsers:
    * `python3 runner.py --browser=chrome`
    * `python3 runner.py --browser=chrome-headless`
    * `python3 runner.py --browser=firefox`
- If you want to get HTML reports, use the `report` argument:
    * `python3 runner.py --report`
- The default environment is `dev`, buy you can specify a different one using the `env` argument:
    * `python3 runner.py --env=prod`
- You can specify test scope using the `scope` argument. You can run an entire class or just one test:
    * `python3 runner.py --scope=tests.blog_tests.BlogTests`
    * `python3 runner.py --scope=tests.blog_tests.BlogTests.test_navigate_to_shameless_posts`

## CircleCI setup
- See `circleci/config.yml`.
- The default config runs all tests on every push and nightly.
- It runs the following command: `python3 runner.py --browser=chrome --report`.
