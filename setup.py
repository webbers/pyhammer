from distutils.core import setup

setup(
    name='pyhammer',
    version='0.1',
    license='MIT',
    description='Build automation library',
    author='Afonso Franca',
    author_email='afonso.franca@gmail.com',
    url='https://github.com/afonsof/pyhammer',
    packages=['pyhammer', 'pyhammer.filters', 'pyhammer.reporters', 'pyhammer.steps'],
    platforms = ['Any'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Topic :: Software Development :: Build Tools',
        ], requires=['pyhammer']
)