Program:

import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

url	= "https://www.amazon.com/Apple-iPhone-15-Pro-Max/dp/B0CMZ4FQL4/ref=sr_1_3?crid=3QMBEFGC59HGD&dib=eyJ2IjoiMSJ9.dqOafv5-z-dxnH_27AjJZ8Klc3OzpST16i9y4egPxCj5CRFuIyzjNF8w-7Tg2ebVR7U1J2Kz2X0Z7rlPmcm9SbYVmNl26_lnNCmTekQNgO_uWJb6R8uYyAH4qjUC_ftEr__lRtYwi-rHctEG4C7cdNvDn9YeeJNNmHubA2RIdw4YixydaiJzaMD3i_CibaCKqDiGc7y6yo4GCXvFTSVpD35WN1Ayhw2jH9cuD1-QlLM.Y8tcpJVkmI_E9anXuurLbKxwaC4UJDpP0m4FXefACtI&dib_tag=se&keywords=iphone%2B15%2Bpro%2Bmax&qid=1715672316&sprefix=iphone%2B15%2Bpro%2Bmax%2B%2Caps%2C291&sr=8-3&th=1"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

text = soup.get_text()

stopwords = set(STOPWORDS)
stopwords.update(["said", "would", "could","the","is"])

wordcloud = WordCloud(width = 500, height = 300,  background_color ='white', stopwords = stopwords, min_font_size = 5).generate(text)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()

















Output:






Result:

 I have been successfully executed the program for web scrapping the reviews of e-commerce website into a word cloud
