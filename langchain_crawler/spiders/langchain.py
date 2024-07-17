# langchain_crawler/spiders/langchain_spider.py

import scrapy
from bs4 import BeautifulSoup

class LangchainSpider(scrapy.Spider):
    name = "langchain"
    allowed_domains = ['python.langchain.com']
    start_urls = ['https://python.langchain.com/']

    def parse(self, response):
        # Filter URLs to only include relevant pages (e.g., exclude 'contact', 'about', etc.)
        if self.is_valid_url(response.url):
            page_content = response.text
            clean_text = self.clean_html(page_content)
            
            # Filter out low-quality content
            if self.is_high_quality_content(clean_text):
                yield {'url': response.url, 'content': clean_text}

        # Follow links to other pages
        for next_page in response.css('a::attr(href)').getall():
            next_page = response.urljoin(next_page)
            if self.is_valid_url(next_page) and self.is_within_depth(next_page):
                yield response.follow(next_page, self.parse)

    def clean_html(self, raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()  # Remove script and style elements

        # Extract content from specific HTML elements
        content = []
        for element in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li','span','code']):
            text = element.get_text(separator=" ", strip=True)
            if len(text) > 30:  # Exclude very short paragraphs
                content.append(text)

        return " ".join(content)

    def is_valid_url(self, url):
        # Define URL patterns to include/exclude
        exclude_patterns = ['contact', 'about', 'privacy', 'terms', 'login', 'signup']
        return not any(pattern in url for pattern in exclude_patterns)

    def is_within_depth(self, url):
        # Limit the depth of URLs to avoid deep links
        max_depth = 4
        return url.count('/') <= max_depth + 2  # +2 to account for 'https://' and domain part

    def is_high_quality_content(self, text):
        # Define content quality checks
        min_length = 50  # Minimum length of content

        if len(text) > min_length:
            return False

        return True
