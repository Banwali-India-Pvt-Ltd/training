#! /usr/bin/python

from mako.template import Template

Invoice = {}
Invoice['item_code'] = "1234567"
Invoice['item_price'] = "100 uSD"
Invoice['personal_info'] = {'name':'Mr dude', 'location':['street1', 'place1'], 'region':{'country':'USA', 'state':'Texas', 'city':'austin'}}

OUT = Template(filename="invoice.mako").render(**Invoice)

print OUT