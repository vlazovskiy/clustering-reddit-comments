**Project**: Attempting to Partition Reddit Comments into a Small Number of Compact Clusters

*Presentation* can be found [here](https://github.com/vlazovskiy/sf18_ds9/blob/master/student_submissions/projects/fletcher/lazovskiy_vladimir/Clustering%20Reddit%20Comments.pdf). 

*Data*: I used the data from https://files.pushshift.io/reddit/comments/, which contains Reddit comments from September 2016 to January 2018. There are over 91 million comments, and for my project pipeline I used samples of 100k and 1m in size. I also attempted to look only at the comments from r/gaming.

*Pre-processing*: After picking comments with only 300 characters, I removed hyperlinks using regex and converted html elements into humanly readable characters. I also stripped text of punctuation. In the end, I settled for TFIDF vectorizer because many comments quoted other comments and used colloquial language, and it was important to get rid of these repeating elements. I added 2-grams and tried adding 3-grams in some tests to get additional signal.

*Analysis*: First, I tried CountVectorizer with LDA, but my topics were repetitive and featured the same most frequently encountered words over and over. To have more control over term frequency, I decided to go with TFIDF and LSI. After tokenizing with TFIDF, I ran the result through TruncatedSVD model to find the optimal number of topics to use for LSI. Unfortunately, results from TruncatedSVD could never explain more than 50% of the variance. Using LSI to further cut down the number of principal components, I normalized the result and used it in my k-means clustering algorithm.

*Result*: The results were inconclusive. My silhouette plots showed that with small k's the clusters were very spread out with very few data points near their respective centroids. When I picked a smaller sample and tried to run my model with the number of clusters up to 400, I kept getting better silhoette scores, but my elbow plot had no clear breaking points, so I could not decide on which k to choose. Besides, having that many custers makes them uninterpretable, so I abandoned the idea.
