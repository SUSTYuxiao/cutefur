from django.test import TestCase

# Create your tests here.
from views import post_test

import demjson

file = open('test.json', 'r')
json = demjson.decode(file, 'utf-8')
file.close()


print json