from setuptools import setup

setup(name="cwlgen",
        version='0.1.0',
        description='Generation of CWL programmatically. Avaible types: CommandLineTool and DockerRequirement',
        author='Kenzo-Hugo Hillion and Hervé Ménager',
        author_email='kehillio@pasteur.fr and hmenager@pasteur.fr',
        keywords = ['cwl'],
        install_requires=['six', 'ruamel.yaml==0.13.13'],
        packages=["cwlgen"],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Topic :: Scientific/Engineering :: Bio-Informatics',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'Environment :: Console',
            ],
        )
