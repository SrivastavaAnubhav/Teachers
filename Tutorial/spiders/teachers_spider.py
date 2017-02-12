import scrapy

class QuotesSpider(scrapy.Spider):
	name = "teachers"
	
	def start_requests(self):
		start_url = "https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange"
		yield scrapy.Request(url=start_url, callback=self.parse)

	def parse(self, response):
		# Bounds recursion depth
		if (response.meta['depth'] < 3):
			# If metadata exists (ie this node is not directly connected to the start), set your name to it
			myID = response.meta['myID'] if 'myID' in response.meta else "Joseph-Louis Lagrange"

			# For each table row, check if the first column is "____ advisor" or "___ student"
			for pairsel in response.xpath('//tr'):
				field = pairsel.xpath('th').extract_first()
				if field is not None:
					if "student" in field:
						names = pairsel.xpath('td/a/text()').extract()

						# There may be more than one student/advisor
						# The relationship should be read as: *relative* is the *relationship* of *myID*
						if names is not None:
							for name in range(len(names)):
								yield {
									"relative": names[name],
									"relationship":"student",
									"myID": myID
								}

								next_page = pairsel.css('td a::attr(href)').extract()[name]
								if next_page is not None:
									next_page = response.urljoin(next_page)
									newmeta = response.meta
									# Pass the next node their own name so that they know what it is
									newmeta['myID'] = names[name]
									yield scrapy.Request(next_page, callback=self.parse, meta=newmeta)
					elif "advisor" in field:
						names = pairsel.xpath('td/a/text()').extract()
						if names is not None:
							# keeping the name as a number so that we can reference the link later
							for name in range(len(names)):
								yield {
									"relative": names[name],
									"relationship":"advisor",
									"myID": myID
								}

								pagestofollow = pairsel.css('td a::attr(href)').extract()
								if pagestofollow is not None:
									next_page = pagestofollow[name]
									next_page = response.urljoin(next_page)
									newmeta = response.meta
									newmeta['myID'] = names[name]
									yield scrapy.Request(next_page, callback=self.parse, meta=newmeta)
