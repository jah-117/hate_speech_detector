# setup.py
from setuptools import setup, find_packages

setup(
    name="hate_speech_detector",
    version="0.1.1", 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # or whichever packages you used
        "nltk",
        "regex",
        "os",
        "joblib",
    ],
    author="Jahfar Muhammed",
    author_email="jahfarbinmuhammed117@gmail.com",
    description="A simple hate speech detection model using machine learning.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/hate_speech_detector",   Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    python_requires=">=3.7",
)
