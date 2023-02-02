from django.contrib.auth import get_user_model
from django.test import Client, TestCase


class TestCreateUser(TestCase):
    def test_create_user(self):
        c = Client()
        res = c.post(
            "/accounts/users/create/",
            {"username": "test", "password": "test", "email": "asd@asd.asd"},
        )

        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()["username"], "test")

        user = get_user_model().objects.get(username="test")
        self.assertTrue(user.check_password("test"))

        res = c.post(
            "/accounts/users/create/",
            {"username": "test", "password": "test", "email": "asd@asd.asd"},
        )
        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            res.json()["username"][0], "A user with that username already exists."
        )


class TestToken(TestCase):
    def test_token(self):
        c = Client()
        res = c.post(
            "/accounts/users/create/",
            {"username": "test", "password": "test", "email": "asd@asd.asd"},
        )

        self.assertEqual(res.status_code, 201)

        res = c.post("/accounts/token/", {"username": "test", "password": "test"})

        self.assertEqual(res.status_code, 200)
        self.assertTrue("token" in res.json())

        token = res.json()["token"]
        u = get_user_model().objects.get(username="test")
        self.assertTrue(u.auth_token.key == token)
