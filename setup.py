from distutils.core import setup
setup(
    name = 'SimpleParameters',
    packages = ['simple_parameters'],
    version = '1.1',
    description = 'Simple parsing of parameters supplied on the command line',
    author='Saurabh Gupta',
    author_email = 'upscprep48@gmail.com',
    url = 'https://github.com/crazybusy/SimpleParameters',
    long_description= 'Allows to create json file with details of the parameters available on the command line for any application. It then handles the user parsing of these parameters by setting the required flags which you can directly consume in your application',
    classifiers = [
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: Free for non-commercial use",
        "Topic :: Software Development :: Libraries"
        "Topic :: Utilities",
        "Topic :: Text Processing"
        ]
)
