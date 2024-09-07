import requests
import unittest


class ProductTests(unittest.TestCase):

        # Configuración inicial con URLs de la API
    def setUp(self):
        # URL base de la API
        self.base_url = "https://api.escuelajs.co/api/v1/products"
        self.category_url = "https://api.escuelajs.co/api/v1/categories"

        # Obtener un ID de categoría válido
        self.category_id = self.get_valid_category_id()

        # Datos del producto según los requisitos de la API
        self.payload = {
            "title": "Test Product",
            "price": 10,
            "description": "A description",
            "categoryId": self.category_id,
            "images": ["https://placeimg.com/640/480/any"]
        }

# Obtiene un ID de categoría válido desde la API.
    def get_valid_category_id(self):
        response = requests.get(self.category_url)
        if response.status_code == 200:
            categories = response.json()
            if categories:
                return categories[0]['id']  # Usar el ID de la primera categoría disponible
        raise ValueError("No valid categories found")

# Prueba para obtener todos los productos disponibles.
    def test_get_all_products(self):
        url = f"{self.base_url}"  # Endpoint para obtener todos los productos
        response = requests.get(url)
        print(f"Estado de la respuesta al obtener todos los productos: {response.status_code}")

        if response.status_code == 200:
            try:
                response_json = response.json()
                print(f"Cantidad de productos obtenidos: {len(response_json)}")
                print(f"Ejemplo de producto: {response_json[0]}")  # Muestra el primer producto
            except requests.exceptions.JSONDecodeError:
                print(f"La respuesta no es JSON: {response.text}")
        else:
            print(f"Fallo al obtener los productos, código de estado: {response.status_code}")
            print(f"Detalles de la respuesta: {response.text}")

# Prueba la obtención de un producto específico por su ID.
    def test_get_single_product(self):
        product_id = self.test_create_product()
        if product_id is None:
            self.fail("Failed to create product for retrieval.")

        url = f"{self.base_url}/{product_id}"
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            try:
                response_json = response.json()
                print(f"Response for GET single product: {response_json}")
            except requests.exceptions.JSONDecodeError:
                print(f"Response body is not JSON: {response.text}")
        else:
            print(f"Failed to retrieve product, status code: {response.status_code}")
            print(f"Response: {response.text}")

# Prueba la creación de un producto nuevo.
    def test_create_product(self):
        response = requests.post(self.base_url, json=self.payload)
        print(f"Response status code: {response.status_code}")

        if response.status_code in [200, 201]:
            try:
                response_json = response.json()
                print(f"Response for POST create product: {response_json}")
                return response_json.get('id')  # Asumiendo que devuelve un 'id'
            except requests.exceptions.JSONDecodeError:
                print(f"Response body is not JSON: {response.text}")
                return None
        else:
            print(f"Failed to create product, status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None

# Prueba la actualización de un producto existente.
    def test_update_product(self):
        product_id = self.test_create_product()
        if product_id is None:
            self.fail("Failed to create product for update.")

        url = f"{self.base_url}/{product_id}"
        updated_payload = {
            "title": "Updated Product",
            "price": 100
        }
        response = requests.put(url, json=updated_payload)
        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:
            try:
                response_json = response.json()
                print(f"Response for PUT update product: {response_json}")
            except requests.exceptions.JSONDecodeError:
                print(f"Response body is not JSON: {response.text}")
        else:
            print(f"Failed to update product, status code: {response.status_code}")
            print(f"Response: {response.text}")

# Prueba la eliminación de un producto existente.
    def test_delete_product(self):
        product_id = self.test_create_product()
        if product_id is None:
            self.fail("Failed to create product for deletion.")

        url = f"{self.base_url}/{product_id}"
        response = requests.delete(url)
        print(f"Response status code: {response.status_code}")

        if response.status_code == 200:  # 204 No Content es común para DELETE exitoso
            print(f"Product {product_id} deleted successfully.")
        else:
            print(f"Failed to delete product, status code: {response.status_code}")
            print(f"Response: {response.text}")


if __name__ == '__main__':
    unittest.main()
