# Scrapy settings for POP_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'POPOF_crawler'

SPIDER_MODULES = ['POPOF_crawler.spiders']
NEWSPIDER_MODULE = 'POPOF_crawler.spiders'

DOWNLOAD_DELAY = 5

FEED_EXPORTERS = {
    'csv': 'POPOF_crawler.feedexport.CSVkwItemExporter'
}

ITEM_PIPELINES = {
    'POPOF_crawler.pipelines.PopofCrawlerPipeline'
}

# By specifying the fields to export, the CSV export honors the order
# rather than using a random order.
EXPORT_FIELDS = [
    'addr',
    'area',
    'category',
    'security_deposits',
    'notes',
    'stop',
]

CONCURRENT_REQUESTS = 1
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'POPOF_crawler (+http://www.yourdomain.com)'
