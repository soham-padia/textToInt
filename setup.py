from setuptools import setup, find_packages

setup(
    name='text_to_number_soham_padia',
    version='0.1.0',
    author='Soham Padia',
    author_email='sohampadia10@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/soham-padia/text_to_number',
    license='LICENSE',
    description='A package to convert text numbers into integers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.6',
    extras_require={
        "test": ["pytest>=6.0", "tox>=3.21"],
    },
)
