import unittest
import requests

class TestAPI(unittest.TestCase):
    base_url = "http://localhost:5000"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjI1MzQ4NywianRpIjoiNzY2YTg1OGMtZGI5YS00ODcxLWIxNTUtNmNiZWVkYzQ2YTdiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IlNoYXNoYW5rLXNoYXJtYSIsIm5iZiI6MTcwNjI1MzQ4NywiY3NyZiI6Ijc5NDNkYWI0LThiOTktNDRjOC1iNzY1LTlkYjQzZDZlMmI4NyIsImV4cCI6MTcwNjI1NDM4N30.Ctt6vZ83I8mZhzaA55TVrxBGRBH7c1Q--mbLbACQn3U"

    def test_create_book(self):
        url = f"{self.base_url}/book/create"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        payload = {
            "title": "48lawsofpower",
            "author": "Robert Greene",
            "isbn": 5956956954,
            "price": 150,
            "quantity": 200
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_book(self):
        url = f"{self.base_url}/book/5956956954"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        url = f"{self.base_url}/book/update/bca4e706-1b99-412c-8d87-83cd7fd4f206"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        payload = {
            "title": "48lawsofpower",
            "author": "Robert Greene",
            "isbn": 5956956954,
            "price": 250,
            "quantity": 220
        }
        response = requests.put(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        url = f"{self.base_url}/book/delete/bca4e706-1b99-412c-8d87-83cd7fd4f206"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_all_books(self):
        url = f"{self.base_url}/book/all"
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    # Add tests for login and registration endpoints

if __name__ == '__main__':
    unittest.main()
