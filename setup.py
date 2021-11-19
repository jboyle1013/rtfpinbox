from setuptools import setup

setup(
    name='rtfpinbox',
    version='1.5.0',
    packages=['inbox', 'headers', 'emails', 'demographics', 'content'],
    install_requires=[
        'mailbox~=0.4',
        'pytz~=2021.3',
        'nltk~=3.6.5',

    ],
    url='',
    license='',
    author='Jordan Boyle',
    author_email='jboyle1013@vt.edu',
    description='Data Structure For UAAPIL and RTFP Fellowship 2021'
)
