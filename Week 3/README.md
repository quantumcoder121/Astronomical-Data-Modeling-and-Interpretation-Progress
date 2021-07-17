# Cross-matching
When we make observations, we often need to match the object we found to an object listed in a known catalogue. 
Though this process looks simple, it becomes quiet complex when we have thousands or even millions of objects. 
This process is called as Cross-matching. 
It basically involves comparing the RA and Dec values of the found object and the listed object. 
This is done by finding out if the distance between these 2 positions on a sphere is greater then a fixed value "max_radius" provided by us.
# Optimized Cross-matching Algorithm
If we try a simple cross-matching algorithm we need to micro-optimize it. 
Here, we first try to find a range of values of dec in which th target object is expected to be found. 
This will be (dec - max_radius, dec + max_value) where dec is the declination of the target object. 
Then we use a binary search apporoach to find if there is a position that matches the target object. 
See the Python Script and Jupyter Notebook for implementation.
# k-d trees
See the Python Script and Jupyter Notebook for implementation.
