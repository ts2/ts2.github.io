
import SimpleHTTPServer
import json

from fabric.api import env, local, run, cd, sudo, warn_only


def run_www(port=8888):
	local( "python -m SimpleHTTPServer %s" % (port) )
