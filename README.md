# POPOF_crawler

抓取[財政部國有財產署](http://www.fnp.gov.tw)各分區之標租不動產資訊。

+ [北區分署](http://www.fnpn.gov.tw/ct/CFT.php?page=CFTMain&area=N000)
+ [中區分署](http://www.fnpc.gov.tw/html/ch/CFT.php?page=CFTMain&area=C000)
+ [南區分署](http://www.fnps.gov.tw/NPBO_S/Web/index-ch.php)

## 安裝套件

+  Scrapy 套件 (可參考 [Scrapy Document - Installation guide](http://doc.scrapy.org/en/latest/intro/install.html))

## 使用方式

```shell
# 北區分署
$ scrapy crawl north -t csv -o north.csv

# 中區分署
$ scrapy crawl center -t csv -o center.csv

# 南區分署
$ scrapy crawl south -t csv -o south.csv

```

## License 

The MIT license (MIT)