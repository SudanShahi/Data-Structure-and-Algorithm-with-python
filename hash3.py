import hashlib


class URLShortener:
    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        digest = hashlib.md5((url + extra).encode()).hexdigest()
        return digest[:6]

    def shorten(self, url):
        if url in self.url_to_code:
            return self.url_to_code[url]

        code = self._make_code(url)
        counter = 1

        while code in self.code_to_url and self.code_to_url[code] != url:
            code = self._make_code(url, str(counter))
            counter += 1

        self.code_to_url[code] = url
        self.url_to_code[url] = code
        self.click_counts[code] = 0

        return code

    def open_url(self, code):
        if code not in self.code_to_url:
            return None

        self.click_counts[code] += 1
        return self.code_to_url[code]

    def get_stats(self, code):
        if code not in self.code_to_url:
            return None

        return {
            "code": code,
            "url": self.code_to_url[code],
            "clicks": self.click_counts[code]
        }


shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"

code1 = shortener.shorten(url1)
code2 = shortener.shorten(url2)
code3 = shortener.shorten(url3)
print("Codes:", code1, code2, code3)
print("Open code1:", shortener.open_url(code1))
print("Open code1 again:", shortener.open_url(code1))
print("Stats code1:", shortener.get_stats(code1))