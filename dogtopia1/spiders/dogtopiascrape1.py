import scrapy
from ..items import Dogtopia1Item

class Dogtopiascrape1Spider(scrapy.Spider):
    name = 'dogtopiascrape1'
    # allowed_domains = ['dogtopia.com']
    # start_urls = ['http://dogtopia.com/']

    def start_requests(self):
        url = r'https://www.dogtopia.com/wp-json/store-locator/v1/locations.json'
        yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        json_response = response.json()
        for i in json_response:
            items = Dogtopia1Item()
            row = i.get('store_info',{}).get('location_address_info',[])[0]
            url = i.get('store_info',{}).get('site_details',{}).get('siteurl','')
            timing = i.get('store_info',{}).get('location_hours_info',[])
            timing.append({})
            timing = timing[0]

            StoreTiminings = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            for k in range(7):
                open1 = '{}_open'
                close = '{}_close'
                StoreTiminings[k] = StoreTiminings[k].capitalize() + ' : ' + timing.get(open1.format(StoreTiminings[k]),'') + ' - ' + timing.get(close.format(StoreTiminings[k]),'')

            items = {
                'StoreID': i.get('id', ''), 
                'StoreName': i.get('title',{}).get('raw',''), 
                # 'Description': row.get('location_description',''),
                'Street': row.get('location_street_address', ''), 
                'City': row.get('location_city', ''), 
                'State': row.get('location_state_prov', ''), 
                'StoreTiminings': ' | '.join(StoreTiminings),
                'Phone': row.get('location_phone',''),
                'Fax': row.get('location_fax',''),
                'Email' : row.get('location_email',''),
                'URL': url,
                'Latitude': row.get('location_coordinates',{}).get('latitude',''),
                'Longitude': row.get('location_coordinates',{}).get('longitude',''),
                }
            yield items


    

