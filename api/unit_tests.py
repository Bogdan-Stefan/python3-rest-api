import requests
import unittest


class TestRestApi(unittest.TestCase):
    address = "http://127.0.0.1:8081"

    def make_request(self, method, resource):
        if method == "GET":
            return requests.get(self.address + resource)
        return None

    # Testing GET
    def test_GET1(self):
        """successful GET"""
        r = requests.get(self.address + "/cars")
        self.assertEqual(r.status_code, 200)

    def test_GET2(self):
        """successful GET"""
        r = requests.get(self.address + "/car/2")
        self.assertEqual(r.status_code, 200)

    def test_GET3(self):
        """bad syntax - incorrect path"""
        r = requests.get(self.address)
        self.assertEqual(r.status_code, 400)

    def test_GET4(self):
        """bad syntax - incorrect path"""
        r = requests.get(self.address + "/carcar/23")
        self.assertEqual(r.status_code, 400)

    def test_GET5(self):
        """bad syntax - incorrect path"""
        r = requests.get(self.address + "/carca")
        self.assertEqual(r.status_code, 400)

    def test_GET6(self):
        """non-existant car"""
        r = requests.get(self.address + "/car/45")
        self.assertEqual(r.status_code, 404)

    # Testing POST
    def test_POST1(self):
        """successful POST"""
        payload = {
            "id": "24",
            "make": "BMW",
            "model": "Z4",
            "year": 2005,
            "price": 9300
        }
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 202)

    def test_POST2(self):
        """bad syntax - incorrect path"""
        payload = {
            "id": "222",
            "make": "Wolkswagen",
            "model": "Golf",
            "year": 2011,
            "price": 8600
        }
        r = requests.post(self.address, json=payload)
        self.assertEqual(r.status_code, 400)

    def test_POST3(self):
        """bad syntax - incorrect path"""
        payload = {
            "id": "222",
            "make": "Wolkswagen",
            "model": "Golf",
            "year": 2011,
            "price": 8600
        }
        r = requests.post(self.address + "/car", json=payload)
        self.assertEqual(r.status_code, 400)

    def test_POST4(self):
        """JSON missing values"""
        payload = {
            "id": "25",
            "make": "Audi",
            "model": "A4",
            "price": 7900
        }
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 422)

    def test_POST5(self):
        """duplicate ids, car is already present in database"""
        payload = {
            "id": "114",
            "make": "Mercedes",
            "model": "CLA",
            "year": 2014,
            "price": 34000
        }
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 202)
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 409)

    def test_POST6(self):
        """missing body"""
        r = requests.post(self.address + "/cars")
        self.assertEqual(r.status_code, 400)

    # Testing PUT
    def test_PUT1(self):
        """successful PUT"""
        payload = {
            "make": "Nissan",
            "model": "Skyline",
            "year": 1999,
            "price": 2200
        }
        r = requests.put(self.address + "/car/1", json=payload)
        self.assertEqual(r.status_code, 202)

    def test_PUT2(self):
        """non-existant car"""
        payload = {
            "make": "Nissan",
            "model": "Skyline",
            "year": 1999,
            "price": 2200
        }
        r = requests.put(self.address + "/car/9001", json=payload)
        self.assertEqual(r.status_code, 404)

    def test_PUT3(self):
        """missing body"""
        r = requests.put(self.address + "/car/1")
        self.assertEqual(r.status_code, 400)

    def test_PUT4(self):
        """bad syntax - invalid path"""
        payload = {
            "make": "Nissan",
            "model": "Skyline",
            "year": 1999,
            "price": 2200
        }
        r = requests.put(self.address + "/loremipsum/42", json=payload)
        self.assertEqual(r.status_code, 400)

    # Testing DELETE
    def test_DELETE1(self):
        """successful delete"""
        r = requests.delete(self.address + "/car/3")
        self.assertEqual(r.status_code, 202)

    def test_DELETE2(self):
        """non-existant car"""
        r = requests.delete(self.address + "/car/9002")
        self.assertEqual(r.status_code, 404)

    def test_DELETE3(self):
        """bad syntax - invalid path"""
        r = requests.delete(self.address + "/cars/42")
        self.assertEqual(r.status_code, 400)

    def test_DELETE4(self):
        """bad syntax - invalid path"""
        r = requests.delete(self.address + "/car/")
        self.assertEqual(r.status_code, 400)


if __name__ == '__main__':
    unittest.main()
