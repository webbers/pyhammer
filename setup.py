from distutils.core import setup

setup(
    name='pyhammer',
    version='0.3.8',
    license='MIT',
    description='Build automation library',
    author='Afonso Franca',
    author_email='afonso.franca@gmail.com',
    url='https://github.com/afonsof/pyhammer',
    packages=['pyhammer', 'pyhammer.filters', 'pyhammer.reporters', 'pyhammer.tasks', 'pyhammer.tasks.helpers',
              'pyhammer.tasks.io', 'pyhammer.tasks.git', 'pyhammer.tasks.svn', 'pyhammer.tasks.text'],
    platforms = ['Any'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Build Tools',
        ], requires=['pyhammer']
)