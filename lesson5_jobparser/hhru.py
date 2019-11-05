


import requests
from pprint import pprint
import json
from bs4 import BeautifulSoup as bs
import re
from lxml import html
import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

# headers = {'accept': '*/*','user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
# -*- coding: utf-8 -*-



class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['https://hh.ru/search/vacancy?area=1&st=searchVacancy&text=python']

    def parse(self, response:HtmlResponse):
        next_page = response.css('a.HH-Pager-Controls-Next::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)
        vacancy = response.css('div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)').extract()
        for link in vacancy:
            yield  response.follow(link, self.vacancy_parse)

    def vacancy_parse(self, response):
        name = response.css('div.vacancy-title h1.header::text').extract_first()
        salary = response.css('div.vacancy-title p.vacancy-salary::text').extract_first()
        href_vac = response.css('a.HH-LinkModifier::attr(href)').extract_first()

        site = ('hh.ru')
        salary_min = response.css('span.value meta.minValue::text').extract_first()
        salary_max = response.css('meta.maxValue::text').extract_first()

        print(href_vac, salary_min, salary_max)
        yield JobparserItem(name=name, salary = salary)



