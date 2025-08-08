from typing import List
from setuptools import find_packages, setup

# Constant representing editable install flag, e.g., '-e .'
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements file and returns a list of dependencies,
    excluding the editable install flag ('-e .') if present.

    Args:
        file_path (str): Path to the requirements.txt file.

    Returns:
        List[str]: A list of cleaned requirement strings.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Package configuration using setuptools
setup(
    name="credit-card-detection-system",
    version="1.0",
    description="A machine learning project for detecting credit card fraud using " \
    "sampling techniques, multiple classifiers, and best practices for imbalanced datasets.",
    author="Vipin Kumar",
    author_email="krvipin15@tutamail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
