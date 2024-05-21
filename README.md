### Directory Structure

- 0 means it belongs directly to the parent directory
- 1, ... are different projects within the thesis

So for example
```
1_SubProject
---|> 0_data  		
---|> 0_plots
---|> doStuff.ipynb
---|> doStuff.py
---|> 1_ExtendedAnalysis	
------|> 0_data
------|> DoElaborateStuff.ipynb 	
------|> 1_EvenFurtherExtendedAnalysis
----------|> 0_data
----------|> 0_plots
----------|> ThisWillMaybeEndUpInTheThesisStuff.ipynb
---|> 2_OtherExtendedAnalysis
2_NextSubProject
```
