import asyncio
from googletrans import Translator

async def main():
    translator = Translator() 
    txt = 'Hello, how are you?'

    # List of target languages
    languages = {
        'hi': 'Hindi',
        'fr': 'French',
        'es': 'Spanish',
        'de': 'German'
    }

    for code, name in languages.items():
        translation = await translator.translate(txt, dest=code)
        print(f"{name}: {translation.text}")

# Run the async function
asyncio.run(main())
