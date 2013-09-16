### Introduction
This is an awesome calculator written in Python 2.7.5. 
It can evaluate simple arithmetic expressions. For 
questions that are beyond arithmetic, it queries Wolfram
Alpha using their API to look for answers

### Installation
First, make sure that you have Beautiful Soup 4
and Nose install. The former is for XML parsing, while 
the latter is needed for testing purposes.  
```bash
pip install BeautifulSoup4     
pip install nose
```    

Then install this module with   
```python
python setup.py install
```

### Versions
0.1 (09/16/2013)

### Usage
```python
python CalCalc.py -s 'YOUR_STRING_HERE'
```   
  
For example:    
```python
python CalCalc.py -s '30*20*    
python CalCalc.py -s 'mass of the earth in kg'
```    

### Implementation
Simple arithmetic expressions are evaluated using Python's 
evil `eval`. We call `eval` on a separate namespace in an 
attempt to prevent injection.   

Complex queries are posted to the Wolfram Alpha API. Results 
are sent back as XML, and BeautifulSoup 4 is used to parse 
the XML and retrieve the final result

### Testing
```python
nosetests testCalc.py
```   

There are currently five tests, each queries for a different 
kind of question. More tests can be added to the file 
`testCalc.py`    

### Related Resources
* [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)   
* [Wolfram Alpha API](http://products.wolframalpha.com/api/explorer.html)
