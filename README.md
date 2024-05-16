### Directory Structure

- 0 means it belongs directly to the parent directory
- 1, ... are different projects within the thesis

So for example

1_RegEx		_the subproject_
 |- 0_data  _the data generated in RegEx_
 |- 0_plots _the plots created in RegEx_
 |- 1_TMP	_RegEx extended (or reduced) to TMPs only_
	 |- 0_data 	_data from TMPs only_
	 |-1_3R	_TMP reduced to 3R only_
	...
