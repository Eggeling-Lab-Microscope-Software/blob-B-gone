from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='blobBgone',
    version='0.2.1',
    description='A lightweight tool to remove blob artifacts from 2D/3D point cloud data as produced by MINFLUX ',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='BSD License',
    readme = readme,
    packages=find_packages(include=['blobBgone']),
    author='Bela Tristan Leander Vogler',
    author_email='bela.vogler@uni-jena.de',
    keywords=['MINFLUX', 'clustering', 'Point Clouds', 'geometry', 
              'Artifact Removal (AR)', 'artifact removal (AR)', 
              'algorithm', 'Single particle tracking (SPT)', 'Blobs Detection'],
    classifiers=[
    "Development Status :: 4 - Beta",

    "Intended Audience :: Science/Research",
    "Topic :: Scientific/Engineering :: Bio-Informatics",

    "License :: OSI Approved :: BSD License",

    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ],
    install_requires=['numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-learn', 'seaborn', 'tqdm'],
    python_requires='>=3',
    url='https://github.com/Eggeling-Lab-Microscope-Software/blob-B-gone'
)