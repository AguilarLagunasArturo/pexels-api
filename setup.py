import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pexels-api-custom-voltaic",
    version="1.0.2",
    author="Voltaic314",
    author_email="lmaupin@arizona.edu",
    description="Use Pexels API v1 with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Voltaic314/pexels-api-custom-voltaic",
    keywords='pexels api images photos',
    install_requires=['requests'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
