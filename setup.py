import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xchain",  # Replace with your own username
    version="0.0.1",
    author="kobibarhanin",
    author_email="",
    description="A generic blockchain library",
    long_description='',
    long_description_content_type="text/markdown",
    url="https://github.com/kobibarhanin/xchain",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["attrs==19.3.0", "bleach==3.1.5", "certifi==2020.6.20", "chardet==3.0.4", "colorama==0.4.3",
                      "docutils==0.16", "idna==2.10", "importlib-metadata==1.7.0", "keyring==21.2.1",
                      "more-itertools==8.4.0", "packaging==20.4", "pkginfo==1.5.0.1", "pluggy==0.13.1", "py==1.9.0",
                      "pycrypto==2.6.1", "Pygments==2.6.1", "pyparsing==2.4.7", "pytest==5.4.3",
                      "readme-renderer==26.0", "requests==2.24.0", "requests-toolbelt==0.9.1", "rfc3986==1.4.0",
                      "six==1.15.0", "tqdm==4.47.0", "twine==3.2.0", "urllib3==1.25.9", "wcwidth==0.2.5",
                      "webencodings==0.5.1", "zipp==3.1.0"],
    python_requires='>=3.7',
)
