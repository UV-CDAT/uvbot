from buildbot.config import BuilderConfig

from kwextensions import factory


__all__ = [
    'build_config',
    'make_builders',
]


def build_config(project, defconfig={}, features=(), *args, **kwargs):
    avail_options = set(project.OPTIONS.keys())
    avail_features = set(project.FEATURES.keys())

    options = set(kwargs.keys())
    missing_options = avail_options.difference(options)
    if missing_options:
        raise RuntimeError('unknown missing options: %s' % ', '.join(missing_options))

    unknown_options = options.difference(avail_options)
    if unknown_options:
        print('ignoring unknown options: %s' % ', '.join(unknown_options))

    featureset = set(features)
    unknown_features = featureset.difference(avail_features)
    if unknown_features:
        raise RuntimeError('unknown features: %s' % ', '.join(unknown_features))

    config = defconfig.copy()

    for optname, optvalues in project.OPTIONS.items():
        if kwargs[optname] not in optvalues:
            raise RuntimeError('unknown value for option %s: %s' % (optname, kwargs[optname]))

        config.update(optvalues[kwargs[optname]])

    nameparts = []
    for option in project.OPTIONORDER:
        nameparts.append(kwargs[option])
    name = '-'.join(nameparts)

    for feature in sorted(avail_features):
        use_feature = 0
        if feature in featureset:
            name += '+%s' % feature
            use_feature = 1
        for k, v in project.FEATURES[feature].items():
            config[k] = v[use_feature]

    return (name, config)


def make_builders(project, buildsets, defprops={}, defconfig={}, **kwargs):
    configs = {}
    for buildset in buildsets:
        name, conf = build_config(project, defconfig=defconfig, **buildset)
        configs[name] = conf

    builders = []
    for name, config in configs.items():
        props = defprops.copy()
        props['configure_options:builderconfig'] = config

        builders.append(BuilderConfig(
            name=name,
            factory=factory.get_ctest_buildfactory(),
            properties=props,
            **kwargs
        ))

    return builders
