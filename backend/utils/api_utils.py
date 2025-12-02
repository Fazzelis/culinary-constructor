import httpx
import asyncio
from configuration import settings


async def search_dish(product_name_ru):
    params = {
        'search_terms': product_name_ru,
        'json': 1,
        'page_size': 3,
        'search_simple': 1,
        'action': 'process'
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(settings.open_food_facts_url, params=params)
            data = response.json()

            if data['products']:
                for product in data['products']:
                    ru_name = product.get('product_name_ru') or product.get('product_name')
                    if ru_name and product_name_ru.lower() in ru_name.lower():
                        return extract_off_nutrition(product)

            return None
    except Exception as e:
        print(f"Ошибка поиска: {e}")
        return None


def extract_off_nutrition(product):
    nutriments = product.get('nutriments', {})

    return {
        'name': product.get('product_name_ru', product.get('product_name')),
        'calories': nutriments.get('energy-kcal'),
        'protein': nutriments.get('proteins', 0),
        'fat': nutriments.get('fat', 0),
        'carbs': nutriments.get('carbohydrates', 0)
    }


async def main():
    # Одиночный запрос
    result = await search_dish("123")
    print(result, result["calories"])


if __name__ == "__main__":
    asyncio.run(main())