from setuptools import setup, find_packages

setup(
    name="dircat",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "dircat": ["templates/*.json"],  # 🔥 THIS IS THE FIX
    },
    install_requires=[
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "dircat=dircat.cli:main",
        ],
    },
)