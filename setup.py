from setuptools import setup, find_packages

# Load the README.md content.  This is a common practice.
def load_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""  # Or a default description

# Provide a default if you cannot access the file.
long_description = load_readme()

setup(
    name='polymarket_oracle_bot',
    version='0.1.0',
    description='A trading bot with CLI and GUI interfaces for Polymarket',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Layup',
    author_email='your.email@example.com',  # Add a valid email if you have one
    url='https://github.com/layup/Polymarket-Oracle-Bot',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
    ],
    keywords='polymarket oracle bot trading cryptocurrency defi',
    packages=find_packages(where='src'),  # Explicitly specify where packages are
    package_dir={'': 'src'},  # map the root package to src
    python_requires='>=3.9.10',
    install_requires=[
        'requests >= 2.20.0',
        'python-dotenv >= 1.0.0',  # Add version specifier
        'web3 >= 6.0.0', # add web3
        # Add other dependencies with version specifiers (e.g., 'argparse >= 1.4.0')
    ],
    entry_points={
        'console_scripts': [
            'tradebot_cli = cli.cli:main',
        ],
        'gui_scripts': [
            'tradebot_gui = gui.gui:run_gui',
        ],
    },
)
