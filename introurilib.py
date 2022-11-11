import urllib
print(dir(urllib))

#urlib holds modules to do work
from urllib import request
print(dir(request))
resp = request.urlopen("https://www.wikipedia.org/")
print(resp.code)
print(resp.length)
print(resp.peek())#not a string it is bytes object
create a repository using Github API