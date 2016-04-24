from webtest import TestApp
import unittest
import manage

routes = []

# ----- Test ALL PAGES
class test_pages(unittest.TestCase):

    def test_routes(self):
        for route in manage.app.wrap_app.routes:
            route = str(route).split()

            if 'POST' not in route[0] and 'assets' not in route[1]:
                route = route[1].replace('\'','')
                routes.append(route)

        self.assertIsNot(route,[])

    def test_basic_all_get_pages(self):
        app = TestApp(manage.app)
        for route in routes:
            resp = app.get(route)

            self.assertEqual(resp.status_int, 200)
            self.assertEqual(resp.charset,'UTF-8')
            self.assertEqual(resp.status,'200 OK')
