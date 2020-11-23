# Mean for hypergeometric random variable

You now know how to generate yet another kind of random variable.  If you want you could, therefore, calculate the histogram by sampling.  We are not going to do all that we are instead going to write a function to calculate the mean.  We also want to be able to quote a 90% confidence limit around this mean.  We will use the central limit theorem to extract this confidence limit so you will also need to calculate the sample variance in your function using:

![](https://render.githubusercontent.com/render/math?math=S^2=\frac{n}{n-1}\left[\left(\frac{1}{n}\sum_{i=1}^nX_i^2\right)-\left(\frac{1}{n}\sum_{i=1}^nX_i\right)^2\right])

where the ![](https://render.githubusercontent.com/render/math?math=X_i) are the ![](https://render.githubusercontent.com/render/math?math=n) random variables.  The ![](https://render.githubusercontent.com/render/math?math=p\times100)% confidence limit can then be computed as:

![](https://render.githubusercontent.com/render/math?math=\epsilon=\sqrt{\frac{S^2}{n}}\Phi^{-1}\left(\frac{p+1}{2}\right))

where ![](https://render.githubusercontent.com/render/math?math=\Phi^{-1}) is the inverse of the normal distribution.  You can compute the value of this function at ![](https://render.githubusercontent.com/render/math?math=p) in python using:

````
bar = scipy.stats.norm.ppf(p)
````

The function you need to complete is called `hypergeom_mean`.  This function takes four arguments:

1. `nsamples` - the number of samples from the distribution from which the mean will be computed.
2. `M` - the number of balls that are to be drawn from the urn
3. `R` - the number of green balls that are in the urn (recall that our random variable counts how many of the balls drawn are green)
4. `N` - the total number of balls in the urn (recall that the balls in the urn are either green or red).
 
The function should return two quantities:

1. `mean` - the mean calculated by sampling nsamples random variables.
2. `confidence_limit` - the 90% confidence limit, which you should compute using the formulas on this page.
