# DYNASTY

A random family tree generator. It generates a GEDCOM file that can be imported in GENOPRO.

The script begins with a randomly generated male, and runs in yearly intervals producing descendants until it reaches the maximum (500) or everybody is dead.

Each individual has these information attached:

* A **name**, chosen from a list of predefined names. The script can also randomly decide to create a composed name.

* A **surname**, inherited from the father. They are randomly generated from a list of predefined surnames.

* **Birth** and **death** dates. The birth of new individuals is determined by a formula that takes into account the ages of both parents and the empirical distribution of the ages at which the European royalty had their children. The death age is determined from the empirical distribution of the ages at death from the same dataset.

* **Personality**, determined by three traits. One is inherited from the father, one from the mother, and the third one is randomly chosen from the list of possible psychological traits.

* **Physical appearance**, determined by three traits. One is inherited from the father, one from the mother, and the third one is randomly chosen from the list of possible physical traits.

* A pair of chromosomes that determine other physical characters: **blood type**, **height**, **weight** and **hair color**.

  * The blood type is determined by one gene with three possible alleles: A, B, and i. One allele is inherited from the father, and the other from the mother. The phenotype is determined by their combinations: A (AA, Ai, iA), B (BB, Bi, iB), AB (AB, BA) or 0 (ii).
  
  * The height is determined by ten genes. Each of these genes has two possible alleles: T or S. The base height is 1.78 m. The script takes all the 20 alleles (10 from the father, 10 from the mother), then increases the heigh by 0.03 m for each T and reduces the heigh by 0.04 m for each S.
  
  * The weight is determined by ten genes. Each of these genes has two possible alleles: W or L. The base weight is 76 kg. The script takes all the 20 alleles (10 from the father, 10 from the mother), then increases the weight by 1 kg for each W and reduces the weight by 1.5 kg for each L.
  
  * The hair color is determined by four genes, each of them independently inherited. Gene 1 has two possible alleles, N or M. Gene 2 has two possible alleles, N or R. Gene 3 has two possible alleles, N (common) or A (rare). Gene 4 has two possible alleles, N (common) or P (rare). If the individual is homozygotic NN for the gene 2, his/her hair color is randomly chosen from brown to black. Else, if he/she is homozygotic MM for gene 1, he/she has a red (homozygotic PP for gene 4) or light brown (other combination for gene 4) hair. Else, if he/she is homozygotic AA for gene 3, he/she is an albino. Else, if he/she is homozygotic PP for gene 4, his/her hair is red. Any other combination results in blonde hair.

* The **list of aristochractic titles** that this person possesses. This is determined by a complex set of inheritance rules that is triggered every time that a person dies. Special rules are applied for illegitimate children. The script determines the list of heirs and divides his/her titles among them. If a person accumulates more than 4 titles, only the highest ranked ones are exported to the output file.

## List of auxiliary files

persos.txt:
List of possible personalities, first in masculine,
then a tabulator, then the personality in
feminine. If the language used does not distinguish
between genders, just repeat the same adjective.

fisicos.txt:
Idem with physical characters.

namesm.txt:
List of male names, one in each line.

namesf.txt:
Idem with feminine names.

paises.txt:
List of countries, in caps, with syllabes
separated by tabulators.

apellidos.txt:
Idem with surnames.
