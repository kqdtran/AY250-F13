### Introduction
There are three problems in this repository. I solved the first two, and 
got somewhat halfway decent with the last one...   

Solutions to all three problems are stored in the hw3 IPython Notebook      

### Part I: Reproduce an old research paper's graph    
I don't have one, so I'm using the one Adam posted on Piazza. Data is 
under `q1_data`, and the reproduced plot is `q1.png`.   

### Part II: Reproduce the New York Temperature, Google, and Yahoo! graph   
Much like the first one, data is under `q2_data`, and the reproduced graph 
is `q2.png`.    

### Part III: Brushing
So far, I think I've been able to:    

* Plot the Iris dataset in a 4x4 grid
* Interactively draw rectangles in one of the subplots. There is, however, 
a strange bug at the moment, since I can only draw in the last grid (bottom 
right). I suppose this has something to do with calling plt, since it only 
remembers what's being drawn last, but I'm not sure of a way to fix it yet.   

There are still a few more steps to go, namely identifying the points in the 
rectangle, highlighting the same set of points in other subplots, and reducing 
the opacity of points that are not in the rectangle. But I'm not there yet :(    

### References
* [Mike Bostock's Brushing Plot](http://bl.ocks.org/mbostock/4063663)
* [A StackOverFlow post on how to create the interactive rectangle](http://stackoverflow.com/q/12052379/2465041)     
* Piazza!