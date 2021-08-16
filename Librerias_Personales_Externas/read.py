import re

# la funcion la podemos definir en el notebook y usar directamente
def get_text(file):
  '''Read Text from file'''
  text = open(file, "r", encoding="utf-8").read()
  text = re.sub(r'<.*?>', ' ', text)
  text = re.sub(r'\s+', ' ', text)
  return text