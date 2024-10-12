import unittest
import requests

# This class provides the test cases to assess the API automation using pytest
class TestReqResAPI(unittest.TestCase):
    BASE_URL = "https://reqres.in"


    # This Function test the GET request of a single user from the database,
    # ensures a correct response code then asserts to ensure data is equal to the expected outcome
    def test_get_single_user(self):
        response = requests.get(f"{self.BASE_URL}/api/users/2")                 # Send GET Request To API
        self.assertEqual(response.status_code, 200)                             # Conduct Response Code Assertion
        data = response.json()                                                  # Retrieve JSON Response
        self.assertEqual(data['data']['id'], 2)                                 # Conduct Data Assertions
        self.assertEqual(data['data']['email'], "janet.weaver@reqres.in")


    # This Function tests the POST request of a single user into the database,
    # providing necessary details of name and job and asserting proper response code and data
    def test_create_user(self):
        payload = {                                                             # Create Data
            "name": "morpheus",
            "job": "leader"
        }
        response = requests.post(f"{self.BASE_URL}/api/users", json=payload)    # Send POST Request To API
        self.assertEqual(response.status_code, 201)                             # Conduct Response Code Assertion
        data = response.json()                                                  # Retrieve JSON Response
        self.assertEqual(data['name'], "morpheus")                              # Conduct Data Assertions
        self.assertEqual(data['job'], "leader")


    # This Function tests the PUT request of a current user,
    # providing necessary details of updated data and asserting proper response code and data
    def test_update_user_put(self):
        payload = {                                                             # Create Updated Data
            "name": "morpheus",
            "job": "zion resident"
        }
        response = requests.put(f"{self.BASE_URL}/api/users/2", json=payload)   # Send PUT Request To API
        self.assertEqual(response.status_code, 200)                             # Conduct Response Code Assertion
        data = response.json()                                                  # Retrieve JSOn Response
        self.assertEqual(data['job'], "zion resident")                          # Conduct Data Assertions


    # This Function tests the PATCH request of a current user,
    # providing necessary details of updated data and asserting proper response code and data
    def test_update_user_patch(self):
        payload = {                                                             # Create Updated Data
            "name": "morpheus",
            "job": "zion resident"
        }
        response = requests.patch(f"{self.BASE_URL}/api/users/2", json=payload)   # Send PATCH Request To API
        self.assertEqual(response.status_code, 200)                             # Conduct Response Code Assertion
        data = response.json()                                                  # Retrieve JSOn Response
        self.assertEqual(data['job'], "zion resident")                          # Conduct Data Assertions


    # This Function tests the DELETE request of a current user
    def test_delete_user(self):
        response = requests.delete(f"{self.BASE_URL}/api/users/2")              # Send DELETE Request to API
        self.assertEqual(response.status_code, 204)                             # Conduct Response Code Assertion


    # This Function tests the POST request for a Successful Login
    def test_post_login_success(self):
        payload = {                                                             # Create Data
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = requests.post(f"{self.BASE_URL}/api/login", json=payload)    # Send POST LOGIN Request To API
        self.assertEqual(response.status_code, 200)                             # Conduct Response Code Assertion
        data = response.json()                                                  # Retrieve JSON Response
        self.assertEqual(data['token'], "QpwL5tke4Pnpja7X4")                    # Conduct Data Assertions


    # This Function tests the POST request for an Unsuccessful Login
    def test_post_login_unsuccessful(self):
        payload = {                                                             # Create Data
            "email":"peter@klaven"
        }
        response = requests.post(f"{self.BASE_URL}/api/login", json=payload)    # Send POST LOGIN Request To API
        self.assertEqual(response.status_code, 400)                             # Conduct Response Code Assertion
        data = response.json()                                                  # Retrieve JSON Response
        self.assertEqual(data['error'], "Missing password")                     # Conduct Data Assertions


# Main Function
if __name__ == "__main__":
    unittest.main()