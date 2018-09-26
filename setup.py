from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(
    name='harmonicintervalprofile',
    version='0.1',
    description='Features for computational harmony related tasks',
    author='Hendrik Vincent Koops',
    author_email='hvkoops@gmail.com',
    url='https://github.com/hvkoops/harmonicintervalprofile',
    packages=['harmonicintervalprofile'],
    long_description=long_description,
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Programming Language :: Python :: 3",
    ],
    keywords='harmony music mir dsp',
    license='LGPLv3',
    install_requires=[
        'numpy >= 1.7.0',
        'scipy >= 1.0.0',
        're'
    ],
)
