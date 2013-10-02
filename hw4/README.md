### Introduction
This is the repository for HW4: Homebrew Computer Vision. 
Solutions to all of the problems are stored in the hw4 IPython Notebook.     

Since my classifier ends up being around 600Mb, I've decided not to include 
it here, but to have instructions on how to recreate it instead.     

### Features Extraction    
* Image array size
* Average of each of the RGB channel
* Cross-correlation between each of the RGB channel
* Harris corner detection
* PCA (I only select 5 components)
* Proportion of pixels that are part of the image's edges, using `vsobel` and `hsobel`
* Image segmentation using the Felzenszwalb algorithm

### Cross-validation   
* Cross-validation 10 times with mean 0.28 and variance 0.02    
* It performs 14 times better than random guessing, since there are fifty categories, 
we would expect a mean of 0.02 only
* Most important features: the first, eight, and nineteenth of my twenty features. This 
translates to the image's array size (???), Harris corner detection, and the proportion 
of pixels along the vertical edge.

### Recreating the Classifier    
Run    

```python
combined_result = pickle.load(open('combined_result.p', 'r'))
```    

to get the combined_result after extracting features via the pickle file. 
Then, run 

```python
target = np.asarray([c[-1] for c in combined_result])      
data = np.asarray([c[:-2] for c in combined_result])
```   

to get the data and target for traning the Random Forest Classifier.    

Finally, executing the block   

```python
from sklearn.cross_validation import cross_val_score    
from sklearn.ensemble import RandomForestClassifier     
clf = RandomForestClassifier(n_estimators=100, n_jobs=4, compute_importances=True)    
clf.fit(data, target)     
pickle.dump(clf, open('trained_classifier.p','w'))
```    

will generate the classifier and save its as a pickle file. On my machine, the 
size of the pickle file varies from 300 to 600 Mb.
