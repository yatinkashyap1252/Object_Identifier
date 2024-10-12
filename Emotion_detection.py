from textblob import TextBlob
from newspaper import Article
import pyttsx3
# import nltk
# nltk.download('punkt')

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",270)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# url='https://timesofindia.indiatimes.com/business/india-business/stock-market-crash-today-should-sensex-nifty-investors-be-worried-about-possible-us-recession-heres-what-experts-say-about-india/articleshow/112293325.cms' #negative news
url='https://www.indiatvnews.com/news/good-news/youngest-coronavirus-patient-discharged-from-hyderabad-hospital-coronavirus-pandemic-updates-news-706480'  #positive
# url='https://en.wikipedia.org/wiki/India'  #neutral
article=Article(url)

article.download()
article.parse()
article.nlp()

text=article.text  #gives all the text of article also along with the side notes and all
summary=article.summary
print(summary)
speak(summary)

blob=TextBlob(summary)
s=blob.sentiment.polarity
print(s)
# speak(s)

if s<=-0.9 and s>=-1:
    speak("devasted")
    print("devasted")
elif s<-0.5 and s>-0.9:
    speak("sad")
    print("sad")
elif s<0 and s>-0.5:
    print("irritated")
    speak("irritated")
elif s==0:
    speak("neutral")
    print("neutral")
elif s>0 and s<0.25:
    print("mildly positive")
    speak("mildly positive")
elif s>0.25 and s<0.5:
    speak("happy")
    print("happy")
elif s>0.5 and s<=0.9:
    print("very happy")
    speak("very happy")
elif s==1:
    print("very positive")
    speak("very positive")