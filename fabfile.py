
import SimpleHTTPServer
import json

from fabric.api import env, local, run, cd, sudo, warn_only


def run_www(port=8888):
	"""Runs a local http server to view `website` """
	local( "python -m SimpleHTTPServer %s" % (port) )

def publish():
	"""Commits local branch and send to github.io and publish stuff"""
	local( "git commit -a -m " )
	local( "git push origin master " )
	
	