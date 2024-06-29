from django.shortcuts import render
from .models import *
import requests
from bs4 import BeautifulSoup


def scrape_web_content(request):
    # Make a GET request to the URL to fetch the HTML content
    if request.method=='POST':
        
        url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-11-10&'
       'sortBy=popularity&'
       'apiKey=177d1430613d447e97bd3bd4dda5f58c')

        response = requests.get(url)

        # print(r.json)
        
        topic=request.POST.get('topic')
        url=f'https://timesofindia.indiatimes.com/topic/{topic}'
        response = requests.get(url)

        if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the content you want (for example, extracting all paragraphs)
            all_paragraphs = soup.find_all('p')

        # Join all paragraphs to create a single string of content
            content_text = '\n'.join([p.get_text() for p in all_paragraphs])
            content=NewsScrping.objects.create(news_topic=topic,news_description=content_text)
            content.save()

            data={'topic' : topic,
                  'content':content_text }
            # print(data)
            
            return render(request,'news.html',{"response":data})
        else:
            data={'error':"unable to fetch data "}
            return render(request,'news.html',{"response":data})
    return render(request,'news.html')


   


