# Web-Scraper
A scrapy spider that crawls wikipedia to find relationships between people and their doctoral students/advisors. You can find an **interactive** result [here](https://srivastavaanubhav.github.io/Web-Scraper/).

## Motivation
I have immense respect for teachers, professors, and educators everywhere (including parents). I am where I am today thanks to them. There are good and bad teachers, but that difference is hard to quantify, so I decided to instead mark how influential teachers are.

## Examples
Here's the result when I bound the recursion depth to 6 (and starting at Joseph-Louis Lagrange). You can see it's already a pretty large graph! I'll do higher values later (I don't anticipate allowing the user to generate this live for processing time reasons).

![Zoomed out photo](ZoomedOut.PNG)

---

Here's the cleanest part of the above graph, zoomed in. I encourage you to play around with the full thing.

![Zoomed in photo](ZoomedIn.PNG)

## Current state
The project currently takes in a name of a person and their Wikipedia page and recursively follows links to their teachers (could be doctoral advisors or academic influences) and their students (both of which are usually provided in the summary table on the right of their page, if it exists. I was amazed to see how quickly one could get to Euler and other big names.

The corresponding website for this project uses VisJS to visualize the tree-like layout, though it has some bugs in that it overlaps names quite often.

## Goals
- The overlapping WILL be fixed
- On selection of a node, bring up a brief profile
- I want to correlate influence (measured by H-index or some other metric) and colour-code respectively

## Running the project
If you have scrapy and its dependencies installed, running `scrapy crawl teachers` from command line should generate data.json, after which you should run `python parser.py` to convert data.json to myGraph.json, the Gephi-style format VisJS requires.
