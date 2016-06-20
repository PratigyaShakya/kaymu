import scrapy
from ..items import KaymuItem
from scrapy.item import Item


class KaymuSpider(scrapy.Spider):
    name="k"
    allowed_domains=["kaymu.com.np"]
    start_urls=["http://www.kaymu.com.np/men-t-shirts/"]

    def parse(self, response):
        links = response.xpath("//a[@class='card-overlay block pr']/@href").extract()
        for link in links:
            full_link = "http://www.kaymu.com.np" + link
            yield scrapy.Request(full_link, callback = self.parse_details)
        
        next_page = response.xpath("//a[@class='page dif vh-center current']/following-sibling::a/@href").extract_first()
        if next_page:
            next_page_full_link = "http://www.kaymu.com.np" + next_page
            yield scrapy.Request(next_page_full_link, callback = self.parse)


    def parse_details(self, response):
        title= response.xpath('//h1[@class="s-bold fsize-15 mvm"]/text()').extract_first()
        cost = response.xpath('//div[@class="price-labels mvm"]/div/text()').extract_first()
        seller = response.xpath('//a[@class="gray-medium s-bold fsize-14 block"]/text()').extract_first()
        avg_rating_tot_reviews = response.xpath('//a[@class="fsize-13 s-bold mvm h-center"]/text()').extract_first()
        brand = response.xpath('//a[@href="/other/"]/text()').extract_first()
        product_location = response.xpath('//div[@class="full-width white-dark-bg mtm pam v-center"]/text()').extract_first()
        image_urls = response.xpath('//img[@class="full-width"]/@data-layzr').extract()
        gender = response.xpath('//label[@class="label valign-middle"][contains(text(), "Gender:")]/following-sibling::span/text()').extract_first()
        material = response.xpath('//label[@class="label valign-middle"][contains(text(), "Material:")]/following-sibling::span/text()').extract_first()
        weight = response.xpath('//label[@class="label valign-middle"][contains(text(), "Weight:")]/following-sibling::span/text()').extract_first()
        condition = response.xpath('//label[@class="label valign-middle"][contains(text(), "Condition:")]/following-sibling::span/text()').extract_first()
        occasion = response.xpath('//label[@class="label valign-middle"][contains(text(), "Occasion:")]/following-sibling::span/text()').extract_first()
        stiched_unstiched = response.xpath('//label[@class="label valign-middle"][contains(text(), "Stitched/Unstitched:")]/following-sibling::span/text()').extract_first()
        age_group = response.xpath('//label[@class="label valign-middle"][contains(text(), "Age Group:")]/following-sibling::span/text()').extract_first()
        url = response.url



        item = KaymuItem()
        item['title'] = title
        item['cost'] = cost
        item['seller'] = seller
        item['avg_rating_tot_reviews'] = avg_rating_tot_reviews
        item['brand'] = brand
        item['product_location'] = product_location 
        item['gender'] = gender
        item['material'] = material
        item['weight'] = weight
        item['condition'] = condition
        item['occasion'] = occasion
        item['stiched_unstiched'] = stiched_unstiched
        item['age_group'] = age_group
        item['url']=url
        item['image_urls'] = image_urls
        yield item

