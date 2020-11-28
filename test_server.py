import unittest
from server import app
from model import connect_to_db


# class DatabaseTests(unittest.TestCase):
#     """Test database for snippet app."""

#     def setUp(self):
#         connect_to_db(app, "postgresql:///testdb")

#         db.drop_all()
#         db.create_all()

class FlaskTests(unittest.TestCase):
    """Test routes for snippet app."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage_response(self):
        """Test response from homepage."""

        response = self.client.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        """Test that homepage loads correctly."""

        response = self.client.get('/')
        self.assertIn(b'make an original Taylor Swift song snippet', response.data)


class FlaskTestsLoggedIn(unittest.TestCase):
    """Test routes for users that are logged in."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_albums(self):
        """Test that albums page loads correctly."""

        response = self.client.get('/albums')
        self.assertIn(b'Select an album to view more details', response.data)

    # def test_albums(self):
    #     """Test that albums page loads correctly."""

    #     response = self.client.get('/albums')
    #     self.assertIn(b'Select an album to view more details', response.data)

    # def test_correct_login(self):
    #     """Test login success with correct credentials."""

    #     response = self.client.post(
    #         '/login',
    #         data=dict(email="test@test.com", password="test",
    #         follows_redirect=True)
    #     )
    #     self.assertIn(b'Logged in!', response.data)
    
    # def incorrect_login(self): 

if __name__ == '__main__':
    unittest.main()