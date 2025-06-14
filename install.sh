mamba install -y -c conda-forge --file requirements.non_src 
mamba install -y -c conda-forge --file requirements.doc
mamba install -y -c conda-forge --file requirements.test
pip install -e .
