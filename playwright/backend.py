import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/admin/login/?next=/admin/")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("fhffhfjfj")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("fffjfjj")
    page.get_by_role("button", name="Log in").click()

    # ---------------------
    context.tracing.stop(path = "trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
