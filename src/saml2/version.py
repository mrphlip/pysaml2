import pkg_resources as _pkg_resources


def _parse_version():
    value = _pkg_resources.parse_version("4.9.0.post1+xswbackport")
    return value


version = _parse_version()
