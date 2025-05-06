#to use the async function in next file
from googletrans import Translator

translator = Translator() 
txt = 'comment allez vous ?'

output = translator.translate(txt, dest='en')
print(output.text)
