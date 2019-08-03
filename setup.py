import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pexels-api",
    version="0.0.1",
    author="a.a.l",
    author_email="aguilar.lagunas.arturo@gmail.com",
    description="Use Pexels API v1 with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AguilarLagunasArturo/pexels-api",
    keywords='pexels api images',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
