from __future__ import with_statement
from fabric.api import settings,local,env

def if_exists(path):
	env.colorize_errors = True
	print("Executing on %(host)s as %(user)s" % env)
	with settings(warn_only=True):
		return local('test -d %s' %path)
		print ("I am exists")
