import re

class Resolver:

	def run(self, file):
		if self.is_test(file):
			return self.get_source(file)
		else:
			return self.get_test(file)

	def is_test(self, file):
		return file.find('_test.exs') != -1

	def get_source(self, file):
		# find erb, haml
		match = re.search(r'(.eex|.haml|.slim)_test.exs$', file)
		related = []

		if match:
			ext = match.group(0)
			regex = re.escape(ext)
			ext = re.sub(r'_test.exs', '', ext)
			file = re.sub(regex, ext, file)
		else:
			# simply sub .ex to _test.exs
			# e.g. foo.ex -> foo_test.exs
			file = re.sub(r'\_test.exs$', '.ex', file)

		if file.find('/test/lib/') > -1:
			# file in lib
			related.append(re.sub(r'/test/lib/', '/lib/', file))
		else:
			related.append(re.sub(r'/test/', '/web/', file, 1))
			related.append(re.sub(r'/test/', '/', file, 1))

		return related


	def get_test(self, file):
		# find eex, haml
		match = re.search(r'eex$|haml$|slim$', file)
		related = []

		if match:
			ext = match.group(0)
			regex = re.escape(ext) + "$"
			file = re.sub(regex, ext + '_test.exs', file)
		else:
			file = re.sub(r'\.ex$', '_test.exs', file)

		if file.find('/lib/') > -1:
			related.append(re.sub(r'/lib/', '/test/lib/', file))
		elif file.find('/web/') > -1:
			related.append(re.sub(r'/web/', '/test/', file, 1))
		else:
			related.append('/test' + file)

		return related
