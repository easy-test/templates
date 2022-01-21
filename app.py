#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-01-07 01:10:17
# @Author  : zzz {easy-quest@vk.com}
# @Link    : https://github.com/easy-quest/
# @Version : 1.0.0

# app.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()
