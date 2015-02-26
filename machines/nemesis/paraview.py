import projects
from projects import paraview

__all__ = [
    'BUILDERS',
]

defprops = {
    'test_include_labels:builderconfig': [
        'PARAVIEW',
    ],
    'test_excludes:builderconfig': [
        'SurfaceLIC-ShuttleAll', # seems the streamlines aren't thick enough?
        'NonlinearSubdivisionDisplay', # missing mesh edges?
    ],
}

defconfig = {
    'BUILD_EXAMPLES:BOOL': 'ON',
    'VTK_DEBUG_LEAKS:BOOL': 'ON',
    'VTK_LEGACY_REMOVE:BOOL': 'ON',

    'PARAVIEW_DATA_STORE:PATH': 'C:/Users/kitware/dashboards',
}

base_features = (
    'gui',
    'python',
    'mpi',
)
buildsets = [
    {
        'os': 'windows',
        'libtype': 'shared',
        'buildtype': 'release',
        'features': base_features,
    },
    {
        'os': 'windows',
        'libtype': 'static',
        'buildtype': 'release',
        'features': base_features + (
            'kits',
        ),
    },
    {
        'os': 'windows',
        'libtype': 'shared',
        'buildtype': 'release',
        'features': base_features,
    },
    {
        'os': 'windows',
        'libtype': 'static',
        'buildtype': 'release',
        'features': base_features + (
            'kits',
        ),
    },
]

BUILDERS = projects.make_builders(paraview, buildsets,
    defprops=defprops,
    defconfig=defconfig,
    slavenames=['megas']
)
