import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xplore",
    packages = ['xplore'],
    version="0.0.1",
    author="Jerry Buaba",
    author_email="buabajerry@gmail.com",
    description="A python package built with pandas for data scientist/analysts, AI/ML engineers for exploring features of a dataset in minimal number of lines of code for quick analysis before data wrangling and feature extraction.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/buabaj/xplore",
    download_url='https://github.com/buabaj/xplore/archive/v0.0.1.tar.gz',
    keywords = ['Data-Science', 'Machine-Learning', 'python'],
    install_requires=[            
          'pandas',
          'pandas_profiling',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)