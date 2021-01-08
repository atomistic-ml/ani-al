### ANI-Al
This repository will contain companion data and model to the paper _Automated discovery of a robust interatomic potential for aluminum_, by J. S. Smith et al. [[arxiv:2003.04934](https://arxiv.org/abs/2003.04934)], pending LANL approval. In particular, we plan to release the final ANI-Al potential and the DFT calculations that comprise its training dataset.

### Required software
Python3.5 or better
Numpy
H5PY

### Included extraction software
pyanitools.py
	-Contains a class called 
	 "anidataloader" for loading
	 and parsing the ANI-1 data set.

example_data_sampler.py
	-Example of how to sample data
	from the anidataloader class.

### Installation instructions

1) export ANI-1_release/readers/lib/ to PYTHONPATH.

2) Run: example_data_sampler.py to test


### ANI-Al Model
The model (located here within this repository: ani-al/model/model-Al-75/) can be used with the NeuroChem Binaries at one of the following locations:
https://github.com/isayev/ASE_ANI
https://github.com/atomistic-ml/neurochem
