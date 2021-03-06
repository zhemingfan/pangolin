from setuptools import setup, find_packages
import glob
import os
import pkg_resources
# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from pangolin import __version__, _program

setup(name='pangolin',
      version=__version__,
      packages=find_packages(),
      scripts=['pangolin/scripts/assign_query_file.smk',
                'pangolin/scripts/assign_query_lineage.smk',
                'pangolin/scripts/Snakefile',
                'pangolin/scripts/pangolearn.smk',
                'pangolin/scripts/pangolearn.py',
                'pangolin/scripts/assign_lineage.py',
                'pangolin/scripts/lineage_finder.py',
				# 'pangolin/scripts/codify_all_sites.py',
                'pangolin/scripts/utils.py',
                'pangolin/scripts/sam_2_snps.py',
                'pangolin/scripts/snp_based_classifier.py',
                'pangolin/scripts/snp_based_classify.smk',
                'pangolin/scripts/report_classes.py',
                'pangolin/scripts/report_results.py'
                ],
      package_data={"pangolin":["data/reference.fasta"]},
      install_requires=[
            "biopython>=1.70",
            "dendropy>=4.4.0",
            "pytools>=2020.1",
            'pandas>=1.0.1',
            "wheel>=0.34",
            'joblib>=0.11',
            'scikit-learn>=0.23.1',
            "PuLP>=2",
            'pysam>=0.15.4'
        ],
      description='hcov-2019 subtyping command line tool',
      url='https://github.com/cov-lineages/pangolin',
      author='Aine OToole, JT McCrone & Emily Scher',
      author_email='aine.otoole@ed.ac.uk',
      entry_points="""
      [console_scripts]
      {program} = pangolin.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)
