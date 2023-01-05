# Project
##### Proteomes, Interactomes and Biological Networks 2022/2023
<img width="1014" height="360" src="https://user-images.githubusercontent.com/106587485/209847519-83c43328-4d87-426f-8e9f-1c7d46d1e4d1.jpg">

## Specification
The project aims to study ***cagA***, an _Helicobacter pylori_ virulence factor, as a risk factor of gastric cancer. </br>
We have focused our attention onto:
1. Analysis of _H. pylori_'s proteome;
2. Focus on _cagA_'s structure;
3. Interaction between _cagA_ and ***SHP2*** and its pro-oncogenic action.

## Results
We have listed here the files regarding the results of our analysis:
* _[CagA.cxs](https://github.com/samustora/PIBN/blob/main/CagA.cxs)_ file chimera file representing _cagA_ protein;
* _[UP000000429_85962.fasta](https://github.com/samustora/PIBN/blob/main/UP000000429_85962.fasta)_ is a _FASTA_ file representing a reference proteome of H. pylori (strain ATCC 700392 / 26695);
* _[cagA_P55980.png](https://github.com/samustora/PIBN/blob/main/cagA_P55980.png)_
* _[cagA_P80200.png](https://github.com/samustora/PIBN/blob/main/cagA_P80200.png)_
* _[cagA_hp.png](https://github.com/samustora/PIBN/blob/main/cagA_hp.png)_
* _[caga_hs.png](https://github.com/samustora/PIBN/blob/main/caga_hs.png)_
* _[colored_relative_abundance.png](https://github.com/samustora/PIBN/blob/main/colored_relative_abundance.png)_ file represents the relative abundances of the 703729 amino acids in _H. pylori_:
  * Gray color symbolizes non-polar amino acids;
  * Yellow color symbolizes aromatic amino acids;
  * Blue color symbolizes polar amino acids;
  * Orange color represents charged amoni acids.
* _[helicobacter_pylori.py](https://github.com/samustora/PIBN/blob/main/helicobacter_pylori.py)_ is a _.py_ file that:
  * Analyzes sequence frequency;
  * Defines the residues;
  * Gets the residues relative abundances.
* _[map05120.png](https://github.com/samustora/PIBN/blob/main/map05120.png)_ file shows a KEGG pathway representing interactions between genes as _cagPAI_ and _cagA_;
* _[multi_SHP2.fasta.txt](https://github.com/samustora/PIBN/blob/main/multi_SHP2.fasta.txt)_ file
* _[sh2_EPIYA_D.cxs](https://github.com/samustora/PIBN/blob/main/sh2_EPIYA_D.cxs)_ chimera file representing _SHP2_ protein;
* _[tree_SHP2.pdf](https://github.com/samustora/PIBN/blob/main/tree_SHP2.pdf)_ file representing a phylogenetic tree based on the _SHP2_ protein order to see its evolutionary pattern across different animals.

## Linux
We wanted to show, using Linux, how many interactions there are between _cagA_ and _SHP2_ (also known as _PTPN11_). </br>
On UniProt, the proteins we are dealing with have the following identification codes:
* _CagA_ in H. Pylori is identified through the UniProt ID P80200;
* _PTPN11_ in H. Sapiens is identified through the UniProt ID Q06124;

The interaction between cagA and PTPN11 can be seen by dealing with the IntAct database that contains the interactome, through bash commands.
```
wget ftp://ftp.ebi.ac.uk/pub/databases/intact/current/psimitab/intact.zip 
unzip intact.zip
cat intact.txt | grep 'uniprotkb:P80200'|grep 'uniprotkb:Q06124'| wc -l
> 8
```
...
```
cat intact.txt | grep 'uniprotkb:cagA' | grep 'uniprotkb:MARK2' | wc -l # same as we write P55980
> 4
```

## Authors
***Corona** Gaia, **Storari** Samuele, **Verdesca** Laura Claudia.*
