from setuptools import setup, find_packages

setup(name='cmsplugin_schedules_modal',
      version='0.1',
      description='CMS Plugin for display a scheduled modal on page',
      url='https://github.com/atiberghien/cmsplugin_schedules_modal',
      author='Alban Tiberghien',
      author_email='alban.tiberghien@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
           'Django<2.0',
      ],
      zip_safe=False)