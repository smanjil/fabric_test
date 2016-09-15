
from fabric.api import local

def hello(name='Fabric!'):
    print 'Hello {0}' .format(name)

def prepare_deploy():
    local('./manage.py test fabapp')
    local('git add -p && git commit')
    local('git push')
