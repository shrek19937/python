from autoscraper import AutoScraper
url = "https://stackoverflow.com/questions/2081586/web-scrapping-with-python"
wanted_list = [ "How to call an external command?" ]
scraper = AutoScraper()
result = scraper.build(url, wanted_list)
result = scraper.build(url, wanted_list)
print(*result, sep="\n")
