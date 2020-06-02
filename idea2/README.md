# Idea #2 - Turi Create Image Similarity Model

While Googling around I stumbled upon the [_Turi Create_ library](https://apple.github.io/turicreate/docs/api/index.html) and their `ImageSimilarityModel`, which seemed to solve my problem for me.
All I had to do was load up all my images into their model by running one line of code: 
```
model = tc.image_similarity.create(imgs)
```
and _Turi Create_ would magically produce this super powerful object with unlimited power.
For example, I could query it for similar images:
```
model.query(some_img, k = 10) # Returns the 10 most similar images
```
It even had an option to create an entire weighted similarity graph out of every image:
```
model.similarity_graph()
```

At this point I was pretty amazed, so I followed their [guide](https://apple.github.io/turicreate/docs/userguide/image_similarity/) and chugged along in `similar_images_using_turicreate.ipynb`.
But then it hit me: "How do I go from similarity graph to grouping similar images together?"
The similarity graph is great at telling me relationships between images (a local property), but it's not quite so obvious how I obtain _clusters_ of images (a more global property).

There are, of course, ad-hoc things I can do.
For example, I could perform a BFS/DFS-like search from each image up until I reach a certain radius, at which point I drop the search.
Assuming the clusters of images are relatively spread apart from each other, this would work modulo having to play around with this radius parameter.

However, this seems somewhat convoluted.

_Where did it all go wrong?_

. . .

. . . 

I may just be looking at the problem through the wrong lens!

Indeed, as I alluded to earlier, instead of an _Image Similarity_ Model, I want something more along the lines of a _Clustering_ Model.

Unfortunate as it is, sometimes some ideas don't quite work, but 'tis alright, [the adventure continues](https://github.com/nicholaspun/similar-images-purger/tree/master/idea3)!

### Side Remark
I've lost the Stack Overflow/Github Issue (one of the two) where I ripped this from, but if one ever needs the feature vectors from this `ImageSimilarityModel`, the following code snippet does this:
```
features = similarity_model._extract_features(imgs, verbose=True, batch_size=64)
embeddings = features['__image_features__'].to_numpy()
```
Why I'm mentioning this:
I did actually try to go from this model to a clustering model, but ripping out these feature vectors and setting stuff up so I could use the `Turi Create` k-means model was too much ad-hoc, hacky coding for me.

(Okay, to be fair, I also completely lost information on the actual image.
The `_extract_features` function only returns feature vectors, but not metadata concerning the image.
I'd have to invent even _more_ ad-hoc stuff just to hack my way to retrieve that information.
Sooooo, yeah, time to call it quits.)