import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Got this from the tox web site
class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex

        args = self.tox_args

        if args:
            args = shlex.split(self.tox_args)

        errno = tox.cmdline(args=args)
        sys.exit(errno)

setup(
    name='django-juno-testrunner',
    version='0.4.1',
    description='A more useful (and slightly more glamorous) test runner for Django 1.6+ from the folks at YunoJuno',
    long_description=README,
    author='Steve Jalim, Hugo Rodger-Brown',
    author_email='steve@somefantastic.co.uk, hugo@yunojuno.com',
    url='https://github.com/yunojuno/django-juno-testrunner.git',
    license='MIT',
    packages=['junorunner'],
    install_requires=['colorama'],
    extras_require={'junorunner': ['colorama', ]},
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ]
)
