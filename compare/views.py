from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from  . import scraper
# Create your views here.
def front_end(request):
    if request.method == 'POST':
        request.POST
        url1 = request.POST.get('url1')
        url2 = request.POST.get('url2')
        #url2 = "https://www.flipkart.com/apple-iphone-14-blue-128-gb/p/itmdb77f40da6b6d?pid=MOBGHWFHSV7GUFWA&lid=LSTMOBGHWFHSV7GUFWA3AV8J8&marketplace=FLIPKART&q=apple&store=search.flipkart.com&spotlightTagId=BestsellerId_search.flipkart.com&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=ac3abe91-ae19-4200-91d4-f69ec60a6296.MOBGHWFHSV7GUFWA.SEARCH&ppt=sp&ppn=sp&ssid=scjguo8jj40000001699246498938&qH=1f3870be274f6c49"
        site1 = request.POST.get('site1')
        site2 = request.POST.get('site2')
        data ={
            'url1':{
                "price" : None,
                "ratings" : None,
                "reviews" : None,
                "image_url" : None,    
                "name" : None
            },
            'url2':{
                "price" : None,
                "ratings" : None,
                "reviews" : None,
                "image_url" : None,    
                "name" : None
            },
            'site_choice':[site1, site2]
        }
        siteScrap = None

        try:
            if site1 == 'amazon':
                siteScrap = scraper.Amazon(url1)
                data['url1']['price'] = siteScrap.get_price()
                data['url1']['ratings'] = siteScrap.get_ratings()
                data['url1']['reviews'] = siteScrap.get_review_count()
                data['url1']['image_url'] = siteScrap.get_image()
                data['url1']['name'] = siteScrap.get_id()
            elif site1 == 'snapdeal':
                siteScrap = scraper.Snapdeal(url1)
                data['url1']['price'] = siteScrap.get_price()
                data['url1']['ratings'] = siteScrap.get_ratings()
                data['url1']['reviews'] = siteScrap.get_review_count()
                data['url1']['image_url'] = siteScrap.get_image()
                data['url1']['name'] = siteScrap.get_id()
            elif site1 == 'flipkart':
                siteScrap = scraper.Flipkart(url1)
                data['url1']['price'] = siteScrap.get_price()
                data['url1']['ratings'] = siteScrap.get_ratings()
                data['url1']['reviews'] = siteScrap.get_review_count()
                data['url1']['image_url'] = siteScrap.get_image()
                data['url1']['name'] = siteScrap.get_id()

            if site2 == 'amazon':
                siteScrap = scraper.Amazon(url2)
                data['url2']['price'] = siteScrap.get_price()
                data['url2']['ratings'] = siteScrap.get_ratings()
                data['url2']['reviews'] = siteScrap.get_review_count()
                data['url2']['image_url'] = siteScrap.get_image()
                data['url2']['name'] = siteScrap.get_id()
            elif site2 == 'snapdeal':
                siteScrap = scraper.Snapdeal(url2)
                data['url2']['price'] = siteScrap.get_price()
                data['url2']['ratings'] = siteScrap.get_ratings()
                data['url2']['reviews'] = siteScrap.get_review_count()
                data['url2']['image_url'] = siteScrap.get_image()
                data['url2']['name'] = siteScrap.get_id()
            elif site2 == 'flipkart':
                siteScrap = scraper.Flipkart(url2)
                data['url2']['price'] = siteScrap.get_price()
                data['url2']['ratings'] = siteScrap.get_ratings()
                data['url2']['reviews'] = siteScrap.get_review_count()
                data['url2']['image_url'] = siteScrap.get_image()
                data['url2']['name'] = siteScrap.get_id()
        except Exception as e:
            return render(request,'compare/error.html',{'error':e})
        

        return render(request, 'compare/compare.html', data)
    return render(request, 'compare/compare.html')

@csrf_exempt
def compare(request):
    if request.method == 'POST':
        request.POST
        url1 = request.POST.get('url1')
        url2 = request.POST.get('url2')
        site1 = request.POST.get('site1')
        site2 = request.POST.get('site2')

        price = None
        ratings = None
        no_reviews = None
        image_url = None
        name = None

        siteScrap = None

        if site == 'amazon':
            siteScrap = scraper.Amazon(url)
            price = siteScrap.get_price()
            ratings = siteScrap.get_ratings()
            no_reviews = siteScrap.get_review_count()
            image_url = siteScrap.get_image()
            name = siteScrap.get_id()
        elif site == 'snapdeal':
            siteScrap = scraper.Snapdeal(url)
            price = siteScrap.get_price()
            ratings = siteScrap.get_ratings()
            no_reviews = siteScrap.get_review_count()
            image_url = siteScrap.get_image()
            name = siteScrap.get_id()
        elif site == 'flipkart':
            siteScrap = scraper.Flipkart(url)
            price = siteScrap.get_price()
            ratings = siteScrap.get_ratings()
            no_reviews = siteScrap.get_review_count()
            image_url = siteScrap.get_image()
            name = siteScrap.get_id()
        
    
        

        data ={
            'url1':{
                "price" : price,
                "ratings" : ratings,
                "reviews" : no_reviews,
                "image_url" : image_url,    
                "name" : name
            },
            'url2':{
                "price" : price,
                "ratings" : ratings,
                "reviews" : no_reviews,
                "image_url" : image_url,    
                "name" : name
            }
        }
        return JsonResponse(data)

# def set_price(price):
#     if price:
#         return price
#     else:
#         return "Oops! Error getting price"

# def set_name(name):
#     if name:
#         return name
#     else:
#         return "Oops! Error getting name"

# def set_rating():
#     if rating:
#         return rating
#     else:
#         return "Oops! Error getting rating"

# def set_no_reviews():
#     if no_reviews:
#         return no_reviews
#     else:
#         return "Oops! Error getting reviews"

# def set_image_url():
#     if image:
#         return image
#     else:
#         return "Oops! Error getting image"
