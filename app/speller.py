import httpx

SPELLER_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


# Асинхронная функция для проверки орфографии через Яндекс.Спеллер
async def check_spelling(text: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(SPELLER_URL, params={"text": text})
        corrections = response.json()
        for correction in corrections:
            word = correction["word"]
            suggestions = correction["s"][0] if correction["s"] else word
            text = text.replace(word, suggestions)
    return text
