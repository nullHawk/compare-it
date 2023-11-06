import requests
from bs4 import BeautifulSoup


class Amazon:
    url = None
    response = None
    headers = {"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
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
            return "₹"+price.get_text(strip=True)[:-1]
        else:
            return "Oops! Error getting the data"
    
    def get_ratings(self):
        rating = self.soup.find('span', {'class': 'a-size-medium a-color-base'})
        if rating:
            return rating.get_text(strip=True)
        else:
            return "Oops! Error getting the data"
    
    def get_image(self):
        image = self.soup.find('img', {'id': 'landingImage'})
        if image:
            return image.get('src')
        else:
            return "Oops! Error getting the data"
    
    def get_id(self):
        name = self.soup.find('span',{'id':'productTitle'})
        if name :
            return name.get_text(strip=True)
        else:
            return "Oops! Error getting the data"
        
    def get_review_count(self):
        review = self.soup.find('span',{'data-hook':'total-review-count'})
        if review:
            review_txt = review.get_text(strip=True)
            return review_txt.split()[0] + " Reviews"
        else:
            return "Oops! Error getting the data"

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
            return "Oops! Error getting the data"
    
    def get_ratings(self):
        rating = self.soup.find('div', {'class': '_3LWZlK'})
        if rating:
            return rating.get_text(strip=True)
        else:
            return "Oops! Error getting the data"
    
    def get_image(self):
        image = self.soup.find('img', {'class': '_396cs4'})
        if image:
            return image.get('src')
        else:
            return "Oops! Error getting the data"
    
    def get_id(self):
        name = self.soup.find('span',{'class':'B_NuCI'})
        if name :
            return name.get_text(strip=True)
        else:
            return "Oops! Error getting the data"
        
    def get_review_count(self):
        review = self.soup.find('span',{'class':'_2_R_DZ'})
        if review:
            temp = review.get_text(strip=True)
            return temp.split('&')[1]
        else:
            return "Oops! Error getting the data"
    
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
            return "Oops! Error getting the data"
    
    def get_ratings(self):
        rating = self.soup.find('span', {'class': 'avrg-rating'})
        if rating:
            return f"{rating.get_text(strip=True)[1:-1]} out of 5"
        else:
            return "Oops! Error getting the data"
    
    def get_image(self):
        image = self.soup.find('img', {'class': 'cloudzoom'})
        if image:
            return image.get('src')
        else:
            return "Oops! Error getting the data"
    
    def get_id(self):
        name = self.soup.find('h1', {'itemprop': 'name'})
        if name :
            return name.get_text(strip=True)
        else:
            return "Oops! Error getting the data"
        
    def get_review_count(self):
        review = self.soup.find('span',{'class':'total-rating showRatingTooltip'})
        if review:
            return review.get_text(strip=True).split()[0] + " Reviews"
        else:
            return "Oops! Error getting the data"