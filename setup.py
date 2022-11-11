import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youdao-dict",
    version="1.0.5",
    author="Xin Wang",
    author_email="wangxin19930411@163.com",
    description="Query Youdao Dictionary in Command Line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WangXin93/youdao_dict",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'youdao = youdao_dict.youdao:main'
        ],
    },
    install_requires=[
        'requests>=2.19.1',
        'lxml>=4.1.0',
        'python-vlc>=3.0.101',
        'pyttsx3>=2.9.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
