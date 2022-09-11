from setuptools import setup, find_packages

setup(
    name="myproject",
    version='1.1',
    description='Pythonのディレクトリ構成のテスト用',
    author='test',
    author_email='test@gmail.com',
    url='https://github.com/test/test.git',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      myproject = myproject.cli:execute
    """,
)