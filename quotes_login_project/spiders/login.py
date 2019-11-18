# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):

        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
        yield FormRequest('http://quotes.toscrape.com/login', formdata={ 'csrf_token' : token,
         'username': 'eoin', 
         'password': 'pass'}, 
         callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.xpath('//a[@href="/logout"]'): 
            self.log(response.xpath('//a[@href="/logout"]/text()').extract_first())
            self.log("you managed to login yipee!!")