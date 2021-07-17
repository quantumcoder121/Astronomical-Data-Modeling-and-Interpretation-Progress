There will be two files in this folder, a Python Script and a Jupyter Notebook which have the required code. The binapprox algorithm is implemented in the code.
# Stacking
In Image Processing, stacking is a process in which multiple images are combined in order to minimize the random errors in the measurement and also to make an enhanced image. 
This can be of two types, Mean and Median Stacking which use mean and median respectively of the values of each pixel in the multiple images as the value of pixel in the final combined image. 
Mean stacking is very sensitive to errors as the mean directly depends on individual values. 
As the median does not depend directly on individual values, Median Stacking is preferred over Mean Stacking.
# Bin Approximation Algorithm
If we try to actually find out median stack of a large number of images, it will consume a lot of data and time. 
This is because while findng out the median, all images are loaded at once in the memory. 
So, we use an algorithm which will find the approximate median called as binapprox. 
In this Algorithm, we divide the range (m - s, m + s) into B bins and find out how many values lie in each bin. 
We are actually assuming that Median will lie in this range and hence, the middle bin will have the median value. 
We approximate the value of median as the average of extreme values of this bin.
# Welford's Method
Here's a reference : https://jonisalonen.com/2013/deriving-welfords-method-for-computing-variance/
