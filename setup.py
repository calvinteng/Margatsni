from setuptools import setup, find_packages

setup(
    name='Margatsni',
    version='1.0',
    author='Solid State Group',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask', 'requests', 'instagram-scraper', 'tqdm', 'beautifulsoup4', 'Flask-APScheduler']
	)