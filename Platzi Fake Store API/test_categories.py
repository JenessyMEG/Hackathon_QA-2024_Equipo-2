import unittest
import requests

class TestCategoriesAPI(unittest.TestCase):
    BASE_URL = "https://api.escuelajs.co/api/v1/categories"
    category_id = None  # Variable para almacenar el ID de la categoría creada

    def setUp(self):
        # Crear una categoría antes de ejecutar las pruebas
        new_category = {
            "name": "Test Category",
            "image": "https://placeimg.com/640/480/any"
        }
        response = requests.post(self.BASE_URL, json=new_category)
        self.assertEqual(response.status_code, 201, f"Failed to create category. Status code: {response.status_code}, Response: {response.text}")
        data = response.json()
        self.category_id = data['id']

# Verifica que se obtienen todas las categorías correctamente.
    def test_get_all_categories(self):
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200, f"Failed to get all categories. Status code: {response.status_code}, Response: {response.text}")
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        for category in data:
            self.assertIn('id', category)
            self.assertIn('name', category)
            self.assertIn('image', category)

# Asegura que se pueda obtener una categoría por su ID.
    def test_get_category_by_id(self):
        if not self.category_id:
            self.fail("Category ID is not set. Ensure that category creation was successful.")
        response = requests.get(f"{self.BASE_URL}/{self.category_id}")
        self.assertEqual(response.status_code, 200, f"Failed to get category by ID. Status code: {response.status_code}, Response: {response.text}")
        data = response.json()
        self.assertEqual(data['id'], self.category_id)
        self.assertIn('name', data)
        self.assertIn('image', data)

# Comprueba que se puede crear una nueva categoría.
    def test_create_category(self):
        new_category = {
            "name": "Another Category",
            "image": "https://placeimg.com/640/480/any"
        }
        response = requests.post(self.BASE_URL, json=new_category)
        self.assertEqual(response.status_code, 201, f"Failed to create category. Status code: {response.status_code}, Response: {response.text}")
        data = response.json()
        self.assertEqual(data['name'], new_category['name'])
        self.assertEqual(data['image'], new_category['image'])
        self.assertIn('id', data)

# Verifica que se pueda actualizar una categoría existente.
    def test_update_category(self):
        if not self.category_id:
            self.fail("Category ID is not set. Ensure that category creation was successful.")
        updated_category = {
            "name": "Updated Category"
        }
        response = requests.put(f"{self.BASE_URL}/{self.category_id}", json=updated_category)
        self.assertEqual(response.status_code, 200, f"Failed to update category. Status code: {response.status_code}, Response: {response.text}")
        data = response.json()
        self.assertEqual(data['id'], self.category_id)
        self.assertEqual(data['name'], updated_category['name'])

# Asegura que se pueda eliminar una categoría existente.
    def test_delete_category(self):
        if not self.category_id:
            self.fail("Category ID is not set. Ensure that category creation was successful.")
        response = requests.delete(f"{self.BASE_URL}/{self.category_id}")
        self.assertEqual(response.status_code, 200, f"Failed to delete category. Status code: {response.status_code}, Response: {response.text}")
        self.assertEqual(response.json(), True)

# Verifica que se puedan obtener los productos de una categoría específica.
    def test_get_products_by_category(self):
        if not self.category_id:
            self.fail("Category ID is not set. Ensure that category creation was successful.")
        response = requests.get(f"{self.BASE_URL}/{self.category_id}/products")
        self.assertEqual(response.status_code, 200, f"Failed to get products by category. Status code: {response.status_code}, Response: {response.text}")
        data = response.json()
        self.assertIsInstance(data, list)
        for product in data:
            self.assertIn('id', product)
            self.assertIn('title', product)
            self.assertIn('price', product)
            self.assertIn('description', product)
            self.assertIn('category', product)
            self.assertIn('images', product)

if __name__ == '__main__':
    unittest.main()