from setuptools import setup


setup(
    name="python-ocapi-sdk",
    version="0.1.0",
    description="Python SDK for Sales Force Commerce Cloud Open Commerce API",
    author="Erik Marty",
    author_email="erik.marty@accenture.com",
    url="https://github.com",
    packages=["ocapi", "ocapi.lib"],
    install_requires=[
        "requests",
        "requests-oauthlib>=1.3.0"
    ],
    license="Apache-2.0",
    keywords="ocapi",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development",
    ],
)