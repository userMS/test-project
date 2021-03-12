import setuptools

setuptools.setup(
    name="test-project",
    version="0.1.0",
    url="https://github.com/userMS/test-project",
    author="userMS",
    author_email="marcosae@hotmail.it",
    description="Testing github package",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
