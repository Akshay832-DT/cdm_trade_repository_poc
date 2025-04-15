from setuptools import setup, find_packages

setup(
    name="cdm_trade_repository",
    version="0.61",
    packages=find_packages(),
    install_requires=[
        "pydantic>=2.0",
        "simplefix",
        "python-dateutil",
    ],
    python_requires=">=3.8",
) 