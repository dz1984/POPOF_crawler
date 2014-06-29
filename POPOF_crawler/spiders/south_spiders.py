# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from POPOF_crawler.items import PopofItem

class SouthSpider(Spider):

    name = "south"
    domain = "http://www.fnps.gov.tw/"

    start_urls = [
        "http://www.fnps.gov.tw/NPBO_S/Web/CFT-1.php",

    ]
    def __init__(self,*args, **kwargs):
        super(SouthSpider, self).__init__(*args, **kwargs)

        pass

    def parse(self, response):

        sel = Selector(response)

        url = sel.xpath("//a[contains(text(),'%s')]/@href" % (u"南區分署"))

        target_url = url.extract()[0]

        print target_url

        yield Request(url=target_url,callback=self.parse_items)

    def parse_items(self, response):

        def extract_data(td):
            return td.xpath("text()").extract()[0].encode('utf-8')

        def extract_div_data(td):
            return td.xpath("div/text()").extract()[0].encode('utf-8')

        def extract_span_data(td):
            return td.xpath("span/text()").extract()[0].encode('utf-8')

        def extract_div_span_data(td):
            return td.xpath("div/span/text()").extract()[0].encode('utf-8')

        sel = Selector(response)

        # catch all tr tag of this table
        table_sel = sel.xpath("//table[@bordercolor='#A5D46F']")[1]

        tr_list = table_sel.xpath("tr")

        tr_list_len = len(tr_list)

        items = []

        for index in range(1, tr_list_len):
            item = PopofItem()

            tds = tr_list[index].xpath('td')

            td_count = len(tds)

            # need to pass some fiels if it's rowspan
            if td_count == 3:
                item['addr'] = extract_data(tds[0])
                item['area'] = extract_data(tds[1])
                item['category'] = extract_data(tds[2])

                prev_item = items[-1]

                item['security_deposits'] = prev_item['security_deposits']
                item['notes'] = prev_item['notes']
                item['stop'] = prev_item['stop']
            else:
                item['addr'] = extract_data(tds[1])
                item['area'] = extract_data(tds[2])
                item['category'] = extract_data(tds[3])
                item['price'] = extract_data(tds[4])
                item['security_deposits']  = extract_data(tds[5])
                item['notes'] = extract_data(tds[7])
                item['stop'] = extract_data(tds[8])

            items.append(item)
            pass

        return items
        pass
