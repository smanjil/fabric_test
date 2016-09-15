
from fabric.api import local

def hello(name='Fabric!'):
    print 'Hello {0}' .format(name)

def test():
    print 'App Testing....'
    local('./manage.py test fabapp')

def commit():
    print 'Committing the changes....'
    local('git add -p && git commit')

def push():
    print 'Deploying the app.....'
    local('git push')

def prepare_deploy():
    test()
    commit()
    push()
