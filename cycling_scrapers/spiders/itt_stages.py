# -*- coding: utf-8 -*-
import scrapy

import re

distance_regex = re.compile('\((\d+\.?\d*)k\)')


class IttStagesSpider(scrapy.Spider):
    name = 'itt_stages'
    start_urls = [
            'https://www.procyclingstats.com/race/Vuelta_a_Espana_2017_Stage_16_ITT_Logrono/',
            'https://www.procyclingstats.com/race/Giro_dItalia_2017_Stage_10']

    def parse(self, response):
        race = response.xpath('//h1//text()').extract_first().replace('\xa0 \xbb \xa0 ', '').strip()
        stage, _, _, _, distance_str = response.xpath('//h2//text()').extract()
        distance = float(distance_regex.match(distance_str)[1])

        yield {
                'race': race,
                'stage': stage,
                'distance': distance
                }
