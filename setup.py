from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ovnis",
    version="0.0.1",
    author="Eduardo Vitor",
    author_email="eduardovitor730@gmail.com",
    description="Exploring information about aliens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eduardovitor/primeiro-pacote-python-dio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
