import scrapy

class QuotesSpider(scrapy.Spider):
	name = "teachers"
	
	def start_requests(self):
		start_url = "https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange"
		yield scrapy.Request(url=start_url, callback=self.parse)

	def parse(self, response):
		filename = 'teachers.html'
		if (response.meta['depth'] < 2):
			myID = response.meta['myID'] if 'myID' in response.meta else "Joseph-Louis Lagrange"
			for pairsel in response.xpath('//tr'):
				field = pairsel.xpath('th').extract_first()
				if field is not None:
					if "student" in field:
						names = pairsel.xpath('td/a/text()').extract()
						if names is not None:
							for name in range(len(names)):
								yield {
									"myID": names[name],
									"relative": myID,
									"relationship":"student"
								}

								next_page = pairsel.css('td a::attr(href)').extract()[name]
								if next_page is not None:
									next_page = response.urljoin(next_page)
									newmeta = response.meta
									newmeta['myID'] = names[name]
									yield scrapy.Request(next_page, callback=self.parse, meta=newmeta)
					elif "advisor" in field:
						names = pairsel.xpath('td/a/text()').extract()
						if names is not None:
							for name in range(len(names)):
								yield {
									"myID": names[name],
									"relative": myID,
									"relationship":"advisor"
								}

								next_page = pairsel.css('td a::attr(href)').extract()[name]
								if next_page is not None:
									next_page = response.urljoin(next_page)
									newmeta = response.meta
									newmeta['myID'] = names[name]
									yield scrapy.Request(next_page, callback=self.parse, meta=newmeta)