from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="helmnet",
    version="0.1.0",
    author="Phanas N",
    author_email="phanas2524@gmail.com",
    description="Real-time safety helmet detection system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhanasN/helmnet",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "ultralytics>=8.0.0",
        "opencv-python>=4.8.0",
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
    ],
)
