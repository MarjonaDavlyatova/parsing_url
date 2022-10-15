import requests
from bs4 import BeautifulSoup
# from gensim.summarization import summarize

url = 'https://pythonist.ru/7-interesnyh-modulej-python-kotorye-stoit-poprobovat/'
page = requests.get(url).text

soup = BeautifulSoup(page)

headline = soup.find('h1').get_text()
print(headline)

p_tags = soup.find_all('p')
# Get the text from each of the "p" tags and strip surrounding whitespace.
p_tags_text = [tag.get_text().strip() for tag in p_tags]
p_tags_text

sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
sentence_list

# Combine list items into string.
article = ' '.join(sentence_list)
# summary = summarize(article, ratio=0.3)
print(f'Length of original article: {len(article)}')
# print(f'Length of summary: {len(summary)} \n')
print(f'Headline: {headline} \n')
# print(f'Article Summary:\n{summary}')