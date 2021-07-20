MRPYTHON_VERSION_MAJOR = 4
MRPYTHON_VERSION_MINOR = 9
MRPYTHON_VERSION_PATCH = 1
MRPYTHON_VERSION_TAG = "alpha"


def version_string():
    return "{}.{}.{}{}".format(MRPYTHON_VERSION_MAJOR,
                               MRPYTHON_VERSION_MINOR,
                               MRPYTHON_VERSION_PATCH,
                               "" if MRPYTHON_VERSION_TAG == "" else ("-" + MRPYTHON_VERSION_TAG))
