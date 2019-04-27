from setuptools import find_packages, setup

setup(
    name='Fai',
    version='0.1',
    maintainer_email='mrcn@vp.pl',
    description='Fakturownia.pl & apaczka.pl client/integrator',
    long_description='Fakturownia.pl & apaczka.pl client/integrator',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
