from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xspass",
    version="0.3",
    author="XasdesNew",
    author_email="xasdesnew@gmail.com",
    description="Мощный и гибкий генератор паролей для Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XasdesNew/xspass",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    project_urls={
        "Source": "https://github.com/XasdesNew/xspass",
    },
) 