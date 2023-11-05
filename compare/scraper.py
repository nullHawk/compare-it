import requests
from bs4 import BeautifulSoup


class Amazon:
    url = None
    response = None
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    soup = None

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        if self.response.status_code != 200:
            print("Failed to retrieve the Amazon page")

    def get_price(self):
        price = self.soup.find('span', {'class': 'a-price-whole'})
        if price:
            return price.get_text(strip=True)
        else:
            return None
    
    def get_ratings(self):
        rating = self.soup.find('span', {'class': 'a-size-medium a-color-base'})
        if rating:
            return rating.get_text(strip=True)
        else:
            return None
    
    def get_image(self):
        image = self.soup.find('img', {'id': 'landingImage'})
        if image:
            return image.get('src')
        else:
            return None
    
    def get_id(self):
        name = self.soup.find('span',{'id':'productTitle'})
        if name :
            return name.get_text(strip=True)
        else:
            return None
        
    def get_review_count(self):
        review = self.soup.find('span',{'data-hook':'total-review-count'})
        if review:
            review_txt = review.get_text(strip=True)
            temp = ""
            for i in review_txt:
                if i.isdigit():
                    temp += i
                else:
                    break
            return temp
        else:
            return None

class Flipkart:
    url = None
    response = None
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }


    soup = None

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        if self.response.status_code != 200:
            print("Failed to retrieve the Flipkart page")

    def get_price(self):
        price = self.soup.find('div', {'class': '_30jeq3 _16Jk6d'})
        if price:
            return price.get_text(strip=True)
        else:
            return None
    
    def get_ratings(self):
        rating = self.soup.find('div', {'class': '_3LWZlK'})
        if rating:
            return rating.get_text(strip=True)
        else:
            return None
    
    def get_image(self):
        image = self.soup.find('img', {'class': '_396cs4'})
        if image:
            return image.get('src')
        else:
            return None
    
    def get_id(self):
        name = self.soup.find('span',{'class':'B_NuCI'})
        if name :
            return name.get_text(strip=True)
        else:
            return None
        
    def get_review_count(self):
        review = self.soup.find('span',{'class':'_2_R_DZ'})
        if review:
            temp = review.get_text(strip=True)
            return temp.split('&')[1]
        else:
            return None
    
class Snapdeal:
    url = None
    response = None
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
    }


    soup = None

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        if self.response.status_code != 200:
            print("Failed to retrieve the Flipkart page")

    def get_price(self):
        price = self.soup.find('span', {'class': 'pdp-final-price'})
        if price:
            return price.get_text(strip=True)
        else:
            return None
    
    def get_ratings(self):
        rating = self.soup.find('span', {'class': 'avrg-rating'})
        if rating:
            return f"{rating.get_text(strip=True)[1:-1]} out of 5"
        else:
            return None
    
    def get_image(self):
        image = self.soup.find('img', {'class': 'cloudzoom'})
        if image:
            return image.get('src')
        else:
            return None
    
    def get_id(self):
        name = self.soup.find('h1', {'itemprop': 'name'})
        if name :
            return name.get_text(strip=True)
        else:
            return None
        
    def get_review_count(self):
        review = self.soup.find('span',{'class':'total-rating showRatingTooltip'})
        if review:
            return review.get_text(strip=True).split()[0]
        else:
            return None



# url = "https://www.amazon.in/Battalion-Frontline-Shimano-Claris-Lightweight/dp/B0C3XW9H46/ref=asc_df_B0C3XW9H46/?tag=googleshopdes-21&linkCode=df0&hvadid=649240562562&hvpos=&hvnetw=g&hvrand=8914965104114629000&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007824&hvtargid=pla-2196095026065&th=1"
# url = "https://www.flipkart.com/apple-iphone-14-midnight-128-gb/p/itm9e6293c322a84?pid=MOBGHWFHECFVMDCX&lid=LSTMOBGHWFHECFVMDCXSSCYWA&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=2d86913b-8e78-499c-b08b-fc0978c68748.MOBGHWFHECFVMDCX.SEARCH&ppt=sp&ppn=sp&ssid=p2n8mreh5c0000001699215352128&qH=0b3f45b266a97d70"
url = "https://www.snapdeal.com/product/boat-airdopes-381-on-ear/634621916769#bcrumbSearch:boat"
amazon = Snapdeal(url)
print(amazon.get_id())
print(amazon.get_price())
print(amazon.get_ratings())
print(amazon.get_image())
print(amazon.get_review_count())