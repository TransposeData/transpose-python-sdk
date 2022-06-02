from setuptools import find_packages, setup

with open("README.md", 'r') as f:
    long_description = f.read()
    
setup(
    name='transpose_data',
    
    # version compliant with PEP440
    # https://peps.python.org/pep-0440/
    version='0.1.2',
    
    # project meta
    

    
    long_description = long_description,
    long_description_content_type="text/markdown",


    include_package_data = True,
    description='Web3 Data Made Simple. Powerful APIs for accessing human-readable blockchain data at scale: from blocks and transactions to NFTs and tokens.',
    keywords=['web3', 'data', 'ethereum', 'web3 data', 'ethereum data'],
    license='MIT',
    
    # classifiers, not sure what these do but it's good to have
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Database',
        'Topic :: Utilities'
    ],

    # The project's main homepage.
    url='https://github.com/TransposeData/transpose-python-sdk',
    
    # Author details
    author='Michael Calvey (michaeljohncalvey), Alex Langshur (alangshur), Jonathan Becker (jon-becker)',
    author_email='michael@transpose.io, alex@transpose.io, jon@transpose.io',
    
    # Find all packages in the directory
    packages=find_packages(exclude=['tests', 'docs']),

    # required dependencies
    install_requires=[
        'requests',
    ],
)

