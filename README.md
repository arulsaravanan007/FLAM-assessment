# FLAM-assessment
1) First, the CSV file xy_data.csv was loaded. It contained only two columns that are x and y.
2) The total number of data points in the file are 1500, and the given condition for t was 6 < t < 60. Therefore, a "t vector" of 1500 points was created, which were equally spaced from 6 to 60.
3) A parametric equation was given, so i formulated the parametric equations given into a python function using the following expressions,
         $$x(t) = (t \cdot \cos(\theta) - e^{M|t|} \cdot \sin(0.3t) \sin(\theta) + X)$$ (in LaTex format).
         $$y(t) = (42 + t \cdot \sin(\theta) + e^{M|t|} \cdot \sin(0.3t) \cos(\theta))$$ (given in LaTex format).
4) A loss function was made to gauge the error. The loss function figures out the L1 distance which is the Mean Absolute Error between the (x,y) points derived from the CSV and the (x.y) points predicted by our model.
5) From the Python's scipy library, I used scipy.optimize.minimize which is a very advanced optimization tool. I passed it the following arguments,
   * The error function to minimize 
   * The constraint bounds of theta being between 0 and 50, i.e., 0 < theta < 50
   * The constraint bounds of M being between -0.05 and 0.05, i.e., -0.05 < M < 0.05
   * The constraint bounds of X being between 0 and 100, i.e., 0 < X < 100
   * An initial guess was also provided
6) The optimizer was run and the values obtained for the parameters theta, M and X were those that gave the least possible error which are
   * theta = 28.12 degrees
   * M = 0.0214
   * X = 54.898
7) The final L1 distance obtained for this fit is 25.24 .
