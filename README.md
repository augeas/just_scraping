
# just_scraping

This is a [Scrapy](https://scrapy.org/) [spider](https://docs.scrapy.org/en/latest/topics/spiders.html) for crawling
[JustGiving crowd-funder pages](https://www.justgiving.com/crowdfunding).

It was written to investigate crowd-funding for sacked Met Officers:

In July 2020, the Metropolitan Police stopped, searched, and restrained athletes Bianca Williams and Ricardo dos Santos, on supposed suspicion of possesion of drugs and weapons, despite their child being present in their car. A [misconduct hearing](https://www.policeconduct.gov.uk/news/statement-following-misconduct-hearing-over-stop-and-search-bianca-williams-and-ricardo-dos) found that this was wholly unjustified, and two officers were dismissed for gross misconduct.

Bianca Williams was [reportedly shocked](https://www.bbc.co.uk/news/uk-england-london-67261517) at the amount of money raised by a
[crowd-funder](https://web.archive.org/web/20231031124058/https://www.justgiving.com/crowdfunding/Clapham-Franks) for the two officers.
The page states that comments have been taken down to "respect the impending Appeal". In fact, enabling developer tools and observing the network tab shows that that comments are still transmitted by API calls, and just not displayed. Some donations have a "userId" associated with them, and it is a simple matter to gather data for the crowd-funding campaign.

* Not all donations for a campaign are returned, but about 90% of funds are recorded.
* The Met Police campaign differs significantly from others.
* Over half of donations recorded by the API are attributable to a single user-ID.

![cumulative donations](https://github.com/augeas/just_scraping/blob/master/met_crowdfunder_cumulative.png?raw=true)
![distribution of dontations](https://github.com/augeas/just_scraping/blob/master/met_crowdfunder_distro.png?raw=true)

You can experiment with capturing and investigating the data for yourself on [binderhub](https://mybinder.org)...


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/augeas/just_scraping/master?labpath=met_crowdfund.ipynb)

... or run the spider locally, capturing data to a .csv file as follows:

```
git clone https://github.com/augeas/just_scraping.git
python3 -m venv just_scraping
cd just_scraping
source ./bin/activate
pip install -r requirements.txt
scrapy crawl crowdfunding -a campaign=Clapham-Franks -o met.csv
```
