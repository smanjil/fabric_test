
from fabric.api import local

def hello(name='Fabric!'):
    print 'Hello {0}' .format(name)

def test():
    local('./manage.py test fabapp')

def commit():
    local('git add -p && git commit')

def push():
    print 'Deploying.....'
    local('git push')

def prepare_deploy():
    test()
    commit()
    push()
