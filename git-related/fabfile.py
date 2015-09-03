from __future__ import with_statement
from fabric.api import local,lcd,run

def update_my_fork():
     code_dir = '/Users/Dileep/repo-location/'
     with lcd(code_dir):
     	local("git checkout master")
     	local("git pull origin master")
     	local("git push upstream master")