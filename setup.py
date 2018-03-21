import os
from setuptools import find_packages, setup, Command
import sys

__author__ = 'taufik'


class RunTests(Command):
    description = 'Run the django test suite from the tests dir.'
    user_options = []
    extra_env = {}
    extra_args = []

    def run(self):
        for env_name, env_value in self.extra_env.items():
            os.environ[env_name] = str(env_value)

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


setup(name='django-gruveo',
      version='0.0.1',
      description='A django app for Gruveo Token Signer',
      author='Taufik Hidayat',
      author_email='taufik.hidayat.official@gmail.com',
      url='https://github.com/senseobservationsystems/django-gruveo',
      keywords=['django', 'gruveo', 'token', 'signer'],
      packages=find_packages(),
      license="LGPLv3",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Telecommunications Industry',
          'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
          'Topic :: Software Development :: Libraries :: Application Frameworks',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=[
          'django',
          'mock'],
      cmdclass={"test": RunTests}
)