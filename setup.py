from setuptools import setup

setup(
    name='WhatsAuto',
    version='0.1.0',
    description='WhatsApp driver',
    author='Habib Rohman',
    author_email="habibrohman@protonmail.com",
    url='https://github.com/hexatester/whatsauto',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["whatsauto"],
    install_requires=[
        'uiautomator2'
    ],
    entry_points={
        'console_scripts': [
            'whatsauto=whatsauto.__main__:main'
        ]
    }
)
