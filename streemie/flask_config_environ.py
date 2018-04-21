from os import environ as env


def envvar(*args, **kwargs):
    cfg = {}

    convert = kwargs.get('convert', lambda x: x)
    default = kwargs.get('default')
    key = kwargs.get('key')

    for arg in args:
        if default is not None:
            val = convert(env.get(arg, default))
        else:
            try:
                val = env[arg]
            except KeyError as e:
                raise KeyError(
                    f'Missing flask config env variable {arg}') from e
        cfg[key or arg] = val

    return cfg


def mergeall(*dicts):
    cfg = {}
    for dict_ in dicts:
        cfg.update(dict_)
    return cfg


def to_bool(s):
    if isinstance(s, bool):
        return s
    if not isinstance(s, str):
        raise RuntimeError(f'Value is not of type str ({type(s)})')
    if s.startswith('y'):
        return True
    if s.startswith('n'):
        return False
    return s in ['1', 'on']
