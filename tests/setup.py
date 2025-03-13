from setuptools import setup, find_packages

setup(
    name="veenayaraddi",  # Name of your Python package
    version="0.1.0",  # Initial version of your package
    packages=find_packages(where="src"),  # Automatically find packages under 'src'
    package_dir={"": "src"},  # Tell setuptools that the source code is under the 'src' directory
    install_requires=[  # External dependencies your project needs
        "pytest>=6.0",  # For running tests
    ],
    extras_require={  # Optional dependencies (e.g., for development)
        "dev": [
            "flake8",  # For linting
            "black",   # For automatic code formatting
            "pytest-cov",  # For test coverage
        ]
    },
    test_suite="tests",  # Location of your test suite
    tests_require=["pytest"],  # Dependencies for running tests
    author="Your Name",  # Replace with your name or organization
    author_email="your.email@example.com",  # Replace with your email
    description="A brief description of your Python project",  # Description of your project
    long_description=open("README.md").read(),  # Long description from the README file
    long_description_content_type="text/markdown",  # The format of the README
    url="https://github.com/veenayaraddi/python-project",  # URL to your project or repo
    classifiers=[  # Metadata about your project
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",  # Adjust to your Python version
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # Supported OS
    ],
    python_requires=">=3.6",  # Minimum Python version required for the project
)
