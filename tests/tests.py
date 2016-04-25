from webtest import TestApp
import unittest
import manage
from corpuslinguistics.models.base import Base
from corpuslinguistics.models.Auxiliar import Auxiliar
from os import listdir
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

# ----- Test DB
class test_db(unittest.TestCase):
    def test_insert(self):
        base = Base()

        nome = 'test'
        email = 'test@test.com'
        senha = 'test'
        base.inserir_dados(nome, email, senha)

        bd_return = base.login('test','test')

        self.assertEqual(bd_return[0][1], 'test')

    def test_select(self):
        base = Base()

        self.assertIsNot(base.busca(), [])

# ----- Test Auxiliar functions
class test_auxiliar(unittest.TestCase):
    def test_cria_pasta(self):
        aux = Auxiliar()

        palavra = 'teste'
        aux.cria_pasta(palavra)

        self.assertIn(palavra, listdir('/tmp'))
