
import re

from dateutil import parser
import scrapy

__base_url__ = ('https://crowdfunding-api.justgiving.com/projects/{}'
    +'/activities?pageNo={}&pageSize={}&type=pledge')

class JustgivingSpider(scrapy.Spider):
    name = "crowdfunding"
    allowed_domains = ['justgiving.com']

    def __init__(self, campaign=None, page_size=50):
        self.page_size = page_size
        assert not campaign is None
        self.campaign = campaign
        super().__init__()

    def start_requests(self):
        yield scrapy.Request('https://www.justgiving.com/crowdfunding/{}'.format(self.campaign))

    def parse(self, response):
        project = re.findall('(?<=projectId":")[0-9a-z\-]+', response.text)[0]

        yield scrapy.Request(__base_url__.format(project, 1, self.page_size),
            callback = self.parse_api, meta={'project': project, 'page': 1})

    def parse_api(self, response):
        try:
            acts = response.json()['activities']
        except:
            acts = []

        this_page = response.meta['page']
        project = response.meta['project']

        yield from [
            {
                'page': this_page,
                'timestamp': parser.parse(act['createdAt']).isoformat(),
                'name': act.get('name'),
                'user': act.get('userId'),
                'message': act.get('message'),
                'amount': act.get('donationAmount'),
                'currency': act.get('currencyCode')
            } for act in acts
        ]

        if acts:
            next_page = this_page + 1
            yield scrapy.Request(__base_url__.format(project, next_page, self.page_size),
                callback = self.parse_api, meta={'project': project, 'page': next_page})
