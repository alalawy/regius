import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regius", 
    version="0.0.2",
    author="M Nasrul Alawy",
    author_email="alawy.nasrul@gmail.com",
    description="regius - Python Handsome Web Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alalawy/regius",
    packages=setuptools.find_packages(),
    install_requires=['webob','parse','jinja2','whitenoise','gunicorn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)