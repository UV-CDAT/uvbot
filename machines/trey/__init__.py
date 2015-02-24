r'''
    Machine: trey.kitwarein.com
    Owner: ben.boeckel@kitware.com
'''

from . import slave
from . import paraview

BUILDERS = {
    'ParaView': paraview.BUILDERS,
}

def get_buildslave():
    return slave.SLAVE

def get_builders(project='ParaView'):
    return BUILDERS[project]
