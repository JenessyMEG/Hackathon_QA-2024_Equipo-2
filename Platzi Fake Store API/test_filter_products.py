import unittest
import requests
import logging

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestProductFiltering(unittest.TestCase):
    base_url = "https://api.escuelajs.co/api/v1/products/"

    def get_response(self, params):
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP de error
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            self.fail(f"Request failed: {e}")

# Prueba el filtrado por título del producto (seleccionar un título valido para cada prueba)
    def test_filter_by_title(self):
        response = self.get_response(
            {"title": "Animo chicoooos"})  # Se cambia "Generic" por un título valido obtenido en Postman al generar una lista de productos
        products = response.json()
        print("Filter by title response:", products)
        self.assertTrue(any("Animo chicoooos" in product.get('title', '') for product in products),
                        "No products with title 'Animo chicoooos' found")

# Prueba el filtrado por precio exacto
    def test_filter_by_price(self):
        response = self.get_response({"price": 100})
        products = response.json()
        logger.info("Filter by price response: %s", products)
        self.assertTrue(all(product.get('price') == 100 for product in products),
                        "Not all products have the price 100")

# Prueba el filtrado por rango de precios
    def test_filter_by_price_range(self):
        response = self.get_response({"price_min": 900, "price_max": 1000})
        products = response.json()
        logger.info("Filter by price range response: %s", products)
        self.assertTrue(all(900 <= product.get('price', 0) <= 1000 for product in products),
                        "Not all products are within the price range 900 to 1000")

# Prueba el filtrado por categoría
    def test_filter_by_category(self):
        response = self.get_response({"categoryId": 1})
        products = response.json()
        logger.info("Filter by category response: %s", products)
        self.assertTrue(all(product.get('category', {}).get('id') == 1 for product in products),
                        "Not all products belong to category 1")

# Prueba el filtrado con múltiples parámetros combinados
    def test_filter_with_multiple_params(self):
        response = self.get_response({
            "title": "Generic",
            "price_min": 10,
            "price_max": 1000,
            "categoryId": 1
        })
        products = response.json()
        logger.info("Filter with multiple params response: %s", products)
        self.assertTrue(all(
            "Generic" in product.get('title', '') and
            900 <= product.get('price', 0) <= 1000 and
            product.get('category', {}).get('id') == 1
            for product in products
        ), "Not all products match the combined filters")

# Prueba el filtrado con límite y desplazamiento (paginación)
    def test_filter_with_limit_and_offset(self):
        response = self.get_response({
            "price_min": 10,
            "price_max": 1000,
            "offset": 10,
            "limit": 10
        })
        products = response.json()
        logger.info("Filter with limit and offset response: %s", products)
        self.assertEqual(len(products), 10, "The number of products returned is not 10")

if __name__ == '__main__':
    unittest.main()
