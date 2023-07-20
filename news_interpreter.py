import openai
from dotenv import load_dotenv
import os

load_dotenv(".env")
openai.api_key = "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"



raw_content = os.popen('node .').read()

def get_important_data_code(raw_html):
    messages = [
        {"role": "user", "content": "Generate code that will extract the important information from the following HTML file: "+ raw_html},
    ]

    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    print(res["choices"][0]["message"]["content"])

article_content = "Analyze the following article: US sues 'consent farm' operator for 'massive' telemarketing deception By Jonathan Stempel July 17 (Reuters) - The U.S. government on Monday sued a New York-based company for allegedly operating a so-called massive 'consent farm' enterprise to trick nearly 1 million people a day into providing personal information and consent to receive telemarketing calls. Fluent LLC was accused of having since 2011 used deceptive ads and websites to promise free rewards, including from familiar brands such as Amazon and Walmart, that were impossible to obtain, and interviews for jobs that did not exist. The Department of Justice and Federal Trade Commission said Fluent's true purpose was to sell 'leads' to telemarketers that later inundated consumers with robocalls, texts and emails about auto warranties, debt reduction, for-profit education, pain cream, solar energy and other products and services. According to a complaint filed in the West Palm Beach, Florida federal court, tens of millions of people were deceived, including many on the National Do-Not-Call Registry, with Fluent in 2018 and 2019 alone generating $93.4 million in revenue from selling more than 620 million leads. Fluent operates under such names as Flash Rewards, the National Consumer Center, The Reward Genius, Up Rewards, FindDreamJobs, JobsOnDemand and StartACareerToday, the complaint said. A lawyer for the company did not immediately respond to requests for comment. The complaint seeks civil penalties and an injunction against further violations of federal telemarketing laws. On Tuesday the FTC, in conjunction with 101 federal and state law enforcers, plans to announce 'Operation Stop Scam Calls,' a crackdown on telemarketers, lead generators and others responsible for billions of illegal telemarketing calls. The case is U.S. v. Fluent LLC et al, U.S. District Court, Southern District of Florida, No. 23-81045. (Reporting by Jonathan Stempel in New York; Editing by Aurora Ellis)"

def get_sentiment(article_content_):
    messages = [
        {"role": "system", "content": "You are a full-time stock analyst, and wise investor. You have been tasked with determining the sentiment of a given news article to decide whether to invest in the stock mentioned in the article."},
        {"role": "user", "content": article_content_},
    ]

    res = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages
    )

    print(res["choices"][0]["message"]["content"])
    
#get_sentiment(article_content)

#get_important_data_code(raw_content)

from bs4 import BeautifulSoup

html = raw_content

soup = BeautifulSoup(html, 'html.parser')

product_info = []

for li in soup.find_all('li', {'class': 'a-carousel-card'}):
    item = {}

    # Extract product title and link
    product_a = li.find('a', {'class': 'a-link-normal'})
    item['product_title'] = product_a['href'].split("/")[-3]
    item['link'] = 'https://www.amazon.com' + product_a['href']

    # Extract image source
    item['img_src'] = li.find('img', {'class': 'p13n-sc-dynamic-image'})['src']
    
    # Extract rating
    stars = li.find('span', {'class': 'a-icon-alt'}).text
    item['rating'] = stars.split()[0]

    # Extract number of reviews
    reviews = li.find('span', {'class': 'a-size-small'}).text
    item['num_reviews'] = reviews.replace(',','')
    
    # Extract price
    price = li.find('span', {'class': '_cDEzb_p13n-sc-price_3mJ9Z'}).text
    item['price'] = price.replace('$', '')

    product_info.append(item)

print(product_info)

#The above code will create a list of dictionaries where each dictionary contains the above extracted information for each product.

