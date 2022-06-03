import pkg_resources as _pkg_resources


def _parse_version():
    value = _pkg_resources.parse_version("4.9.0.post2+backport")
    return value


version = _parse_version()
