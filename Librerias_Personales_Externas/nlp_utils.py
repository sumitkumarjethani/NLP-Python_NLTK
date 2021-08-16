import nltk
from urllib import request
from bs4 import BeautifulSoup
from nltk import word_tokenize

# la funcion la podemos definir en el notebook y usar directamente
def freq_words(url, n, encoding = 'utf8'):
  req = request.urlopen(url)
  html = req.read().decode(encoding)
  raw = BeautifulSoup(html, 'html.parser')
  text = raw.get_text()
  tokens = word_tokenize(text)
  tokens = [t.lower() for t in tokens]
  fd = nltk.FreqDist(tokens)
  return [t for (t, _) in fd.most_common(n)]