from setuptools import setup, find_packages

setup(name='cmsplugin_scheduled_modal',
      version='0.3',
      description='CMS Plugin for display a scheduled modal on page',
      url='https://github.com/atiberghien/cmsplugin_scheduled_modal',
      author='Alban Tiberghien',
      author_email='alban.tiberghien@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
           'Django<2.0',
      ],
      zip_safe=False)