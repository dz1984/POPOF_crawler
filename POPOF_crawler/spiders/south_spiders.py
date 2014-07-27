# -*- coding: utf-8 -*-
import re

from scrapy.http import Request
from scrapy.spider import Spider
from scrapy.selector import Selector

from POPOF_crawler.items import PopofItem

class SouthSpider(Spider):

    name = "south"
    code = "S"
    domain = "http://www.fnps.gov.tw/"

    start_urls = [
        "http://www.fnps.gov.tw/NPBO_S/Web/CFT-1.php",

    ]
    def __init__(self,*args, **kwargs):
        super(SouthSpider, self).__init__(*args, **kwargs)

        pass

    def parse(self, response):

        sel = Selector(response)

        urls = sel.xpath("//a[contains(@href,'http') and re:test(text(),'(%s|%s)')]/@href" % (u"南區分署",u"辦事處")).extract()

        for url in urls:
            target_url = url
            yield Request(url=target_url,callback=self.parse_items)

    def parse_items(self, response):

        def extract_data(td):
            result = td.xpath("text()").extract()
            return result[0].encode('utf-8') if len(result)>0 else ''

        def extract_div_data(td):
            return td.xpath("div/text()").extract()[0].encode('utf-8')

        def extract_span_data(td):
            return td.xpath("span/text()").extract()[0].encode('utf-8')

        def extract_div_span_data(td):
            return td.xpath("div/span/text()").extract()[0].encode('utf-8')

        def generate_id(year, batch_no, serial_no):
            return self.code + year.zfill(3) + batch_no.zfill(2)  + serial_no.decode('utf-8').zfill(2)
        sel = Selector(response)

        # catch the case_title
        try:
            case_title = sel.xpath("//td[re:test(text(),'(%s)')]/text()" % (u'財政部')).extract()[0]
        except:
            case_title = sel.xpath("//td/span[@class='word8']/text()").extract()[0]

        year, batch_no = re.findall(u".*[分署|辦事處](\d+)年.*第(\d+)批.*", case_title)[0]

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

                item['id'] = prev_item['id']
                item['security_deposits'] = prev_item['security_deposits']
                item['notes'] = prev_item['notes']
                item['stop'] = prev_item['stop']
            else:
                item['id'] = generate_id(year, batch_no ,extract_data(tds[0]))
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
