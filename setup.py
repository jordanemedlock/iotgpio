import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iotgpio", # Replace with your own username
    version="0.0.1",
    author="Jordan Medlock",
    author_email="jordanemedlock@gmail.com",
    description="A small library of IOT GPIO classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jordanemedlock/iotgpio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)