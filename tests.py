# pytest -q tests.py
import faker
import os
import re
import requests


# Utilities
F = faker.Faker()

def recursive_file(path=''):
	'''
	Example
	=======
		>>> for file in recursive_file('.'):
		... 	print(file)
	'''
	path = path or os.path.curdir
	for dirpath, dirnames, filenames in os.walk(path):
		for filename in filenames:
			yield os.path.join(dirpath, filename)

def ping_links(*links, seconds=3, **kwargs):
	'''
	Example
	=======
		>>> ping_links('...', '...', seconds=1)
	'''
	unavailable_links = list()

	for link in links:
		try:
			response = requests.head(link, timeout=seconds, **kwargs)
			is_available = response.status_code < 400
		except:
			is_available = False
		if not is_available:
			unavailable_links.append(link)
	assert not unavailable_links, \
		f'`{unavailable_links}` are unavailable'

def read_file(file_name, encode='utf-8'):
	'''
	Example
	=======
		>>> content = read_file('...')
	'''
	try:
		with open(file_name, 'r', encoding=encode) as f:
			return f.read()
	except Exception as e:
		print(e)
		return ''


# Tests
def test_link_available():
	available_ext = ('.md', )
	ref_pattern = re.compile(r'(?<=\()https[^\)]+(?=\))')
	headers = {'user-agent': F.user_agent()}

	for file in recursive_file():
		_, ext = os.path.splitext(file)
		if ext in available_ext:
			content = read_file(file)
			links = ref_pattern.findall(content)
			ping_links(*links, headers=headers)


# Main
if __name__ == '__main__':
	import typing

	_locals = locals()
	_locals_key = tuple(_locals.keys())
	is_test = lambda s: s.startswith('test')

	for func in filter(is_test, _locals_key):
		_func = _locals[func]
		if isinstance(_func, typing.Callable) and \
			_func.__code__.co_argcount==0:
			try:
				_func()
			except AssertionError as ae:
				print('AssertionError:', ae)
