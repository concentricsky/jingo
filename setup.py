from setuptools import setup
import os


from jingo import VERSION

setup(
    name='jingo',
    version="0.4.6",
    description='An adapter for using Jinja2 templates with Django.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Jeff Balogh',
    author_email='jbalogh@mozilla.com',
    url='http://github.com/jbalogh/jingo',
    license='BSD',
    packages=['jingo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['jinja2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        # I don't know what exactly this means, but why not?
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
