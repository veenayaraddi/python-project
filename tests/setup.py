from setuptools import setup, find_packages

setup(
    name="python-project",  # Name of your project
    version="0.1.0",  # Initial version of your package
    packages=find_packages(where="src"),  # Automatically find packages in the 'src' directory
    package_dir={"": "src"},  # Tells setuptools to look for packages inside the 'src' directory
    install_requires=[  # External dependencies
        "pytest>=6.0",  # Example: pytest for testing
    ],
    extras_require={  # Optional dependencies for extra features
        "dev": [
            "flake8",  # Linter for development
            "black",   # Code formatter
            "pytest-cov",  # For test coverage reporting
        ]
    },
    test_suite="tests",  # Location of your tests (optional)
    tests_require=["pytest"],  # Test dependencies, e.g., pytest
    author="Your Name",  # Your name or organization
    author_email="your.email@example.com",  # Your email
    description="A brief description of your Python project",  # Short description of the project
    long_description=open("README.md").read(),  # Detailed description from README file
    long_description_content_type="text/markdown",  # Format of README (markdown)
    url="https://github.com/yourusername/python-project",  # URL to your project's homepage or repository
    classifiers=[  # Metadata for the project
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",  # You can list specific Python versions
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # Supported operating systems
    ],
    python_requires=">=3.6",  # Minimum Python version required
)
