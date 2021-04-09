from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
      name='light-async-scheduler',
      version='0.0.1',
      description='A function based scheduler based on the async event loop.',
      long_description_content_type="text/markdown",
      long_description=README,
      author='Ellis Lunnon',
      author_email='ellislunnon@gmail.com',
      license='MIT',
      packages=['async_scheduler'],
      zip_safe=False

)
