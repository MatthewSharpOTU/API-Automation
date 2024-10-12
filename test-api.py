import unittest
import requests

class TestReqResAPI(unittest.TestCase):
    BASE_URL = "https://reqres.in"

    def test_get_single_user(self):
        """Test GET request for a single user"""
        response = requests.get(f"{self.BASE_URL}/api/users/2")
        print(response.status_code)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['data']['id'], 2)

    # def test_create_user(self):
    #     """Test POST request to create a user"""
    #     payload = {
    #         "name": "morpheus",
    #         "job": "leader"
    #     }
    #     response = requests.post(f"{self.BASE_URL}/users", json=payload)
    #     self.assertEqual(response.status_code, 201)
    #     data = response.json()
    #     self.assertEqual(data['name'], "morpheus")
    #     self.assertEqual(data['job'], "leader")

    # def test_update_user(self):
    #     """Test PUT request to update a user"""
    #     payload = {
    #         "name": "morpheus",
    #         "job": "zion resident"
    #     }
    #     response = requests.put(f"{self.BASE_URL}/users/2", json=payload)
    #     self.assertEqual(response.status_code, 200)
    #     data = response.json()
    #     self.assertEqual(data['job'], "zion resident")

    # def test_delete_user(self):
    #     """Test DELETE request to delete a user"""
    #     response = requests.delete(f"{self.BASE_URL}/users/2")
    #     self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()