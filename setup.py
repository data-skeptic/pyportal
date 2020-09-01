import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyportal",
    version="0.0.1",
    author="Kyle Polich",
    author_email="kyle@dataskeptic.com",
    description="A python interface to Data Skeptic Portal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/data-skeptic/pyportal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)