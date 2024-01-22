from setuptools import setup, find_packages

setup(
    name='binvox_rw',
    version='0.0',
    author='wangqiang9',
    author_email='wanqqiang@bupt.edu.cn',
    description='Read and Visualiz binvox data',
    packages=["binvox_rw"],
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
