import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gif2tx",
    version="0.1.0",
    author="tantanGH",
    author_email="tantanGH@github",
    license='MIT',
    description="Animated GIF to Tx/Tp converter for xmkmcs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tantanGH/gif2tx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'gif2tx=gif2tx.gif2tx:main'
        ]
    },
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    setup_requires=["setuptools"],
    install_requires=["Pillow"],
)
