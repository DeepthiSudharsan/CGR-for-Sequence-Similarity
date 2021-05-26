## CHAOS GAME REPRESENTATION FOR SEQUENCE SIMILARITY ANALYSIS

#### There are two main parts to the project - Analysis of sequences using Frequency CGR (FCGR) and Coordinate CGR.

## Methods implemented

![image](https://user-images.githubusercontent.com/59824729/119332381-1f42da00-bca6-11eb-8b7f-ab4fed1c3947.png)

###### Note: While plotting, the y-axis is inverted to follow the usual convention.

### Frequency CGR

In the frequency CGR method, we divide a grid into a 2D array of size (√(4<sup>k</sup> ), √(4<sup>k</sup>))
![image](https://user-images.githubusercontent.com/59824729/119365199-52e52a80-bccd-11eb-9c6b-bd8aafe2287b.png)

##### For each nucleotide in a kmer, the image is subdivided into 4 quadrants:
- A in the top left
- G in the top right 
- C in the bottom left 
- T in the bottom right

Each quadrant is split according to the same principle for the next nucleotide in the kmer, recursively. 

![image](https://user-images.githubusercontent.com/59824729/119365969-1cf47600-bcce-11eb-991c-2c5c49650fbe.png)

#### CGR Probabiltiy Distance

Calculating Euclidean distance between 2 chaos probability matrices

![image](https://user-images.githubusercontent.com/59824729/119366485-a5731680-bcce-11eb-805f-b50bb4960299.png)

### Coordinate CGR

In this method we use the coordinates calculated using the following steps to analyse the sequences

* Start from the center of the grid

* 1st coordinate - plotted halfway between the center of the square and the vertex representing this nucleotide (A)

* Successive coordinates - plotted halfway between the previous point and the vertex representing the current nucleotide

![image](https://user-images.githubusercontent.com/59824729/119368475-b02eab00-bcd0-11eb-9e4e-cdf48bb59db6.png)

#### CGR Coordinate Distance

Calculating Euclidean distance between 2 chaos vectors obtained

![image](https://user-images.githubusercontent.com/59824729/119368812-187d8c80-bcd1-11eb-91d9-663356991f2a.png)

Annotated code of our project has been provided.  We also used streamlit open-source app framework for creating a custom web-app for our project. A folder with the source code for the app, snips of the expected output and directions for running it have also been provided. 

## Data

The data has been gathered from NCBI (https://www.ncbi.nlm.nih.gov/) and GISAID (https://www.gisaid.org/). We tried for two categories of data - hCov-19 and BetaCov-19 sequences (DNA_SEQUENCES folder) and also for human and various animal genome sequences (ANIMAL_GENOME folder). 

## Observations

* Frequency Chaos Game Representation

![image](https://user-images.githubusercontent.com/59824729/119442272-24a33180-bd45-11eb-9aa3-a2286c4e8c9c.png)

* Coordinate Chaos Game Representation

![image](https://user-images.githubusercontent.com/59824729/119442281-2a007c00-bd45-11eb-8680-79b3438ad062.png)

## References

1. https://towardsdatascience.com/chaos-game-representation-of-a-genetic-sequence-4681f1a67e14
2. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7497811/
3. https://www.hindawi.com/journals/aaa/2013/926519/

## Additional Note

In the code, the CGR of the sequences being analyzed are exported as png files in the same folder as the data. So in the same folders as the data, we have uploaded the images for a sample execution as well.
