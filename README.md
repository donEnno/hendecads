### Sequence Analysis

**Goal** is to derive a "rule" which allows confident separation from true hendecads and other 11 repeats.

- [x] Visually, find hydrophobic regions

- [ ] Come up with a rule for Hendecadness
	--> Gly/Pro should be low/constant

- [ ] Blast on confirmed 11-repeats

- [ ] (Cluster Embeddings?)

------
### DeepCoil

**Goal** is to benchmark and develop DeepCoil further.

- [x] Rerun DC and visualize

Four approaches to be done:

- [ ] Train DeepCoil exactly the same way
- [ ] + latest data
- [ ] + latest data + PT5 - *updated DC*
- [ ] + latest data + PT5 + selected sequences from NPF - *new DC*

At some point try to reproduce your error: lower/uppercase predictions

Once we have confirmed Hendecads form the sequence analysis:
- [ ] Does DC capture them? 
	--> If yes, which groups?
	--> If yes, run AlphaFold on them

------
### Secondaty Structure Prediction

**Goal** is to implement a pipeline that handles data processing, modelling and analysis of results.

- [ ] More advanced

- [ ] How to generally visualize/assess the performance of my predictions?

- [ ] How to generally handle data?
	--> Try to find a way s.t. I later have to parse the data to fit my program, not my program fit the data!

- [ ] Filter NPF data by 11-repeats and try to separate sequences that actually represent hendecads
	--> they are often "buried" in a sequence of heptads
	--> Family specific coil-coiledness
