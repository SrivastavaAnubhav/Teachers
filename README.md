# Web-Scraper
A scrapy spider that crawls wikipedia to find relationships between people and their doctoral students/advisors.

<h2>Motivation</h2>
I have immense respect for teachers, professors, and educators everywhere (including parents). I am where I am today thanks to them. There are good and bad teachers, but that difference is hard to quantify, so I decided to instead mark how influential teachers are.

<h2>Current state</h2>
The project currently takes in a name of a person and their Wikipedia page and recursively follows links to their "_______ advisor" (could be doctoral or academic) and their students (both of which are usually provided in the summary table on the right of their page, if it exists. I was amazed to see how quickly one could get to Euler and other big names.

The corresponding website for this project uses VisJS to visualize the tree-like layout, though it has some bugs in that it overlaps names quite often.

<h2>Running the project</h2>
If you have scrapy and its dependencies installed, running `scrapy crawl teachers` from command line should generate data.json, after which you should run `python parser.py` to convert data.json to myGraph.json, the Gephi-style format VisJS requires.
