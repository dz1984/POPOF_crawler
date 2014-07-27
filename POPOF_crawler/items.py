# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class PopofItem(Item):
    # define the fields for your item here like:
    id = Field()
    addr = Field()
    area = Field()
    category = Field()
    price = Field()
    security_deposits = Field()
    notes = Field()
    stop = Field()
    pass
