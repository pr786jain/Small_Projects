# pip install googletrans
import asyncio
from googletrans import Translator

async def main():
    translator = Translator() 
    #txt = 'comment allez vous ?'
    txt1 =' Hello how are you?'
    output = await translator.translate(txt1, dest='hi')
    print(output.text)

# Run the async function
asyncio.run(main())


#to use the async function in next file
# from googletrans import Translator

# translator = Translator() 
# txt = 'comment allez vous ?'

# output = translator.translate(txt, dest='en')
# print(output.text)