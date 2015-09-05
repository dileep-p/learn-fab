from fabric.api import *


env.roledefs = {
    'webserver' : ['web01','web02'],
    'dbservers' : ['db01','db02'],
}

@task
def mem_usage():
    run('free -m')

@task
def sudo_test():
    sudo('touch /tmp/abcd')
    sudo('ls -la /tmp/abcd')

@task
def put_file():
    put('/tmp/abcd','/tmp/abcd')

@task
def get_file():
    get('/tmp/abcd','/tmp/123')


