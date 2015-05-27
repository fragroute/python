#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

formatter = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("我是中文.","That you could type up right.","But it didn't sing.","So I said goodnight.")
