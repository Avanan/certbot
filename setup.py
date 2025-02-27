from setuptools import setup, find_packages
setup(
    name='certbot',
    version='3.3.0',  # Match the version of the original certbot
    description='ACME client',
    long_description_content_type='text/markdown',
    url='https://github.com/Avanan/certbot',
    author='Certbot Project',
    author_email='certbot-dev@eff.org',
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        'certbot-dns-cloudflare',
        'certbot-dns-cloudxns',
        'certbot-dns-digitalocean',
        'certbot-dns-dnsimple',
        'certbot-dns-dnsmadeeasy',
        'certbot-dns-gehirn',
        'certbot-dns-google',
        'certbot-dns-linode',
        'certbot-dns-luadns',
        'certbot-dns-nsone',
        'certbot-dns-ovh',
        'certbot-dns-rfc2136',
        'certbot-dns-sakuracloud',
        # Add any other DNS plugins you want to exclude
    ]),
    install_requires=[
        'acme',
        'ConfigArgParse',
        'configobj',
        'cryptography',
        'distro',
        'josepy',
        'parsedatetime',
        'pyrfc3339',
        'pytz'
    ],
    entry_points={
        'console_scripts': [
            'certbot=certbot.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.11',
)

