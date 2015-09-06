from fabric.api import local,env

env.hosts = ['localhost','127.0.0.1']

def task1():
    local("uptime")

def task2():
    local("whoami")

def run_all():
    task1()
    task2()
