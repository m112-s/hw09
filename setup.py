from setuptools import setup, find_packages

setup(
    name="booklover",  
    version="1",
    author="Manav Sheth", 
    author_email="gfw8hq@virginia.edu",
    description="HW9", 
    long_description=open("readme.md").read(), 
    long_description_content_type="text/markdown",
    url="https://github.com/m112-s/hw09/tree/main/booklover", 
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
)