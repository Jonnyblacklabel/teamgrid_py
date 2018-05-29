import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teamgrid_py",
    version="0.0.1",
    author="Jonnyblacklabel",
    author_email="mail@jonnyblacklabel.de",
    description="Package for calling to teamgrid API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonnyblacklabel/teamgrid_py",
    packages=setuptools.find_packages(),
    install_requires=['requests','jsonpickle'],
    python_requires='>=3.6',
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)