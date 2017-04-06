BScWSD (UNDER CONSTRUCTION)
=====

A collection of different Python algorithms of Word Sense Disambiguation Systems(WSD):

* **Lesk algorithms**
  * Original Lesk (Michael E.Lesk 1986, 1986)
  * Simple Lesk (with definition, example(s) and lemmas)

  

This package is based on many other implemented packages.
Author:Abdelrahman Khaled Hussun
Supervised by:Dr.Mohamed el Mahdy

This package includes:
=====================
```
wsd semeval_2015_task_13_(multilingual)  README.md  
``` 

Installation 
============

```
using Windows:
1)Install python shell lastest version from https://www.python.org/downloads/windows/
2)Open cmd and type these commands in the following order:
pip install nltk
python -m nltk.downloader 'averaged_perceptron_tagger'
pip install BScWSD

using Unix:
Just open the terminal and write these commands.
``` 

***
Usage
=====

```

$ python
>>> from wsd.Lesk_Algorithms import simple_lesk
>>> sent = 'I went to the bank to deposit my money'
>>> ambiguous = 'bank'
>>> answer = simple_lesk(sent, ambiguous)
>>> print answer
Synset('depository_financial_institution.n.01')
>>> print answer.definition()
a financial institution that accepts deposits and channels the money into lending activities

```

***
Cite
====

To cite `BScWSD`:

Abdelrahman Khaled. 2017. BScWSD: A collection of different Python algorithms of Word Sense Disambiguation Systems(WSD) [software].supervisor:Dr. Mohamed el Mahdy Retrieved from  https://github.com/AbdelrahmanKhaled95/BScWSD

In `bibtex`:

```
@misc{BScWSD,
author =   {Abdelrahman Khaled},
supervisor= {Dr. Mohamed el Mahdy}
title =    {BScWSD: A collection of different Python algorithms of Word Sense Disambiguation Systems(WSD) [software]},
published = {https://github.com/AbdelrahmanKhaled95/BScWSD}},
year = {2017}
}
```

***
License
=========

Copyright (c) 2017 Abdelrahman Khaled

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


***
References
=========

* Michael Lesk. 1986. Automatic sense disambiguation using machine readable dictionaries: how to tell a pine cone from an ice cream cone. In Proceedings of the 5th annual international conference on Systems documentation (SIGDOC '86), Virginia DeBuys (Ed.). ACM, New York, NY, USA, 24-26. DOI=10.1145/318723.318728 http://doi.acm.org/10.1145/318723.318728

* Satanjeev Banerjee and Ted Pedersen. 2002. An Adapted Lesk Algorithm for Word Sense Disambiguation Using WordNet. In Proceedings of the Third International Conference on Computational Linguistics and Intelligent Text Processing (CICLing '02), Alexander F. Gelbukh (Ed.). Springer-Verlag, London, UK, UK, 136-145.

* Satanjeev Banerjee and Ted Pedersen. 2003. Extended gloss overlaps as a measure of semantic relatedness. In Proceedings of the Eighteenth International
Joint Conference on Artificial Intelligence, pages 805–810, Acapulco.

* Jay J. Jiang and David W. Conrath. 1997. Semantic similarity based on corpus statistics and lexical taxonomy. In Proceedings of International Conference on Research in Computational Linguistics, Taiwan.

* Claudia Leacock and Martin Chodorow. 1998. Combining local context and WordNet similarity for word sense identification. In Fellbaum 1998, pp. 265–283.

* Lee, Yoong Keok, Hwee Tou Ng, and Tee Kiah Chia. "Supervised word sense disambiguation with support vector machines and multiple knowledge sources." Senseval-3: Third International Workshop on the Evaluation of Systems for the Semantic Analysis of Text. 2004.

* Dekang Lin. 1998. An information-theoretic definition of similarity. In Proceedings of the 15th International Conference on Machine Learning, Madison, WI.

* Linlin Li, Benjamin Roth and Caroline Sporleder. 2010. Topic Models for Word Sense Disambiguation and Token-based Idiom Detection. The 48th Annual Meeting of the Association for Computational Linguistics (ACL). Uppsala, Sweden.

* Andrea Moro, Roberto Navigli, Francesco Maria Tucci and Rebecca J. Passonneau. 2014. Annotating the MASC Corpus with BabelNet. In Proceedings of the Ninth International Conference on Language Resources and Evaluation (LREC'14). Reykjavik, Iceland.

* Zhi Zhong and Hwee Tou Ng. 2010. It makes sense: a wide-coverage word sense disambiguation system for free text. In Proceedings of the ACL 2010 System Demonstrations (ACLDemos '10). Association for Computational Linguistics, Stroudsburg, PA, USA, 78-83.

* Steven Bird, Ewan Klein, and Edward Loper. 2009. Natural Language Processing with Python (1st ed.). O'Reilly Media, Inc..

* Eneko Agirre and Aitor Soroa. 2009. Personalizing PageRank for Word Sense Disambiguation. Proceedings of the 12th conference of the European chapter of the Association for Computational Linguistics (EACL-2009). Athens, Greece. 

* Liling Tan. 2014. Pywsd: Python Implementations of Word Sense Disambiguation (WSD) Technologies [software]. Retrieved from  https://github.com/alvations/pywsd

