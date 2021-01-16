from distutils.core import setup


def readme():
    with open("README.md", encoding="UTF8") as f:
        return f.read()


setup(
    name="pyreport",
    version="0.1",
    description="A python library for creating latex reports",
    long_description=readme(),
    author="schlerp",
    author_email="schlerpderpson@gmail.com",
    url="https://github.com/schlerp/pyreport",
    packages=["pyreport"],
    package_dir={"pyreport": "pyreport"},
    classifiers=[
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
    ],
)
