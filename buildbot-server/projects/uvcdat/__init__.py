import projects
from projects.common import options

__all__ = [
    'NAME',

    'DEFAULTS',

    'OPTIONS',
    'OPTIONORDER',

    'FEATURES',
]

NAME = 'uvcdat'

DEFAULTS = {
    'configure_options:project': {
        'BUILD_EXAMPLES:BOOL': 'ON',
        'BUILD_TESTING:BOOL': 'ON',
    },
    'cdash_url': 'https://open.cdash.org',
    'cdash_project': 'UV-CDAT',
    'supports_parallel_testing:project': False,
    'github_owner': 'UV-CDAT',
    'github_repo': 'uvcdat',
}


OPTIONS = {
    'os': options.os,
    'buildtype': options.buildtypes,
}
OPTIONORDER = ('os', 'buildtype',)

FEATURES = {
    '_noexamples': ({}, {
        'configure_options:feature': {
            'BUILD_EXAMPLES:BOOL': 'OFF',
        },
    }),
    'gui': projects.make_feature_cmake_options({
        'CDAT_BUILD_GUI:BOOL': ('OFF', 'ON')
    }),
    'graphics': projects.make_feature_cmake_options({
        'CDAT_BUILD_GRAPHICS:BOOL': ('OFF', 'ON')
    }),
    'parallel': projects.make_feature_cmake_options({
        'CDAT_BUILD_PARALLEL:BOOL': ('OFF', 'ON')
    }),
    'esmf': projects.make_feature_cmake_options({
        'CDAT_BUILD_ESMF_ESMP:BOOL': ('OFF', 'ON')
    }),
    'mesa': projects.make_feature_cmake_options({
        'CDAT_BUILD_OFFSCREEN:BOOL': ('OFF', 'ON')
    }),
    'mode': ({
      'configure_options:feature': {
        'CDAT_BUILD_MODE:STRING': 'LEAN',
        },
      },{
      'configure_options:feature': {
        'CDAT_BUILD_MODE:STRING': 'DEFAULT',
        },
      },{
      'configure_options:feature': {
        'CDAT_BUILD_MODE:STRING': 'ALL',
        },
      }),
}
