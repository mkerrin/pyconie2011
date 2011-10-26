from setuptools import find_packages, setup

setup(
    name = "pyie2011",
    version = "0.1",

    install_requires = [
        "setuptools",
        "WebOb",
        "Paste",
        "PasteScript",
        "Jinja2",
        "WebTest",
        "wsgi_lite",
        ],

    include_package_data = True,
    zip_safe = False,
    )
