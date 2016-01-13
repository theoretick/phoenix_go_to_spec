# to run
# python resolver_test.py

import unittest
from resolver import *

class ResolverTest(unittest.TestCase):

	def test_is_test_returns_true(self):
		file = '/test/foo/something_test.exs'
		r = Resolver().is_test(file)
		self.assertEqual(r, True)

	def test_is_test_returns_true_for_eex_test(self):
		file = '/test/views/something.html.eex_test.exs'
		r = Resolver().is_test(file)
		self.assertEqual(r, True)

	def test_is_test_returns_false(self):
		file = '/web/foo/something.ex'
		r = Resolver().is_test(file)
		self.assertEqual(r, False)

	def test_is_test_returns_false_for_eex(self):
		file = '/test/views/something.html.eex.ex'
		r = Resolver().is_test(file)
		self.assertEqual(r, False)

	# get_source

	def test_finds_source(self):
		file = '/test/something/foo_test.exs'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/web/something/foo.ex')
		self.assertEqual(r[1], '/something/foo.ex')

	def test_finds_source_from_eex(self):
		file = '/test/views/namespace/users/_something.html.eex_test.exs'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/web/views/namespace/users/_something.html.eex')
		self.assertEqual(r[1], '/views/namespace/users/_something.html.eex')

	def test_finds_source_from_haml(self):
		file = '/test/views/documents/update.html.haml_test.exs'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/web/views/documents/update.html.haml')
		self.assertEqual(r[1], '/views/documents/update.html.haml')

	def test_finds_source_from_lib(self):
		file = '/test/lib/something/foo_test.exs'
		r = Resolver().get_source(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/lib/something/foo.ex')

	# get_test

	def test_finds_test(self):
		file = '/web/models/user.ex'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/models/user_test.exs')

	def test_finds_test_from_lib(self):
		file = '/lib/foo/utility.ex'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/lib/foo/utility_test.exs')

	def test_finds_test_from_eex(self):
		file = '/web/views/users/new.html.eex'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/views/users/new.html.eex_test.exs')

	def test_finds_test_from_haml(self):
		file = '/web/views/account/login.html.haml'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/views/account/login.html.haml_test.exs')

	def test_finds_test_from_other(self):
		file = '/foo/user.ex'
		r = Resolver().get_test(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/foo/user_test.exs')

	# run
	# returns either the source or test depending on the given file

	def test_run(self):
		file = '/web/decorators/namespace/user_decorator.ex'
		r = Resolver().run(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/decorators/namespace/user_decorator_test.exs')

	def test_run_from_lib(self):
		file = '/lib/utilities/namespace/foo.ex'
		r = Resolver().run(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/test/lib/utilities/namespace/foo_test.exs')

	def test_run_from_test(self):
		file = '/test/controllers/namespace/foo_controller_test.exs'
		r = Resolver().run(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/web/controllers/namespace/foo_controller.ex')
		self.assertEqual(r[1], '/controllers/namespace/foo_controller.ex')

	def test_run_from_test_lib(self):
		file = '/test/lib/namespace/foo_test.exs'
		r = Resolver().run(file)
		self.assertEqual(len(r), 1)
		self.assertEqual(r[0], '/lib/namespace/foo.ex')

	def test_run_for_eex_test(self):
		file = '/test/views/namespace/users/_new.html.eex_test.exs'
		r = Resolver().run(file)
		self.assertEqual(len(r), 2)
		self.assertEqual(r[0], '/web/views/namespace/users/_new.html.eex')
		self.assertEqual(r[1], '/views/namespace/users/_new.html.eex')

if __name__ == '__main__':
	unittest.main()
