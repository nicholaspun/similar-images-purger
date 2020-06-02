# Similar Images Purger

## Backstory
A while ago I went on a trip to Iceland with a couple friends.
Upon returning, we created a shared Google Photos album which quickly filled up with over 2000 images.
On one hand, we did make that many memories.
Buuuuut, on the other hand, there were many pairs of images that looked like the following:
<div style="text-align: center">
    <img src="similar_image_1.jpg" width="200"/>
    <img src="similar_image_2.jpg" width="200"/>
</div>

(If you look reaaally closely, the clouds are in _slightly_ different spots)

This is less than ideal.
Every time I wish to go through this photo album and bring back memories I'll have to flip through multiple duplicates.
As such, I went on a quest to purge similar looking images from the gigantic album. 

## Task
Create something (most likely a script) that can go through a directory containing the photos from this trip and isolate a subset of "unique" images.

## Idea #1 - Document Distance
We start simple.
We can cast our problem here as a "Document Distance" problem.
We create some metric _d_ that takes in two images and returns a some number that represents the "distance" between two images.
A larger distance means the two images are not alike and a smaller distance means the two images are similar.
As such, we can begin grouping similar images together and pick any representative image from each group to make up the subset of unique images.

There are definitely many issues with this, but hey, it's a start.
For more details, [follow me](https://github.com/nicholaspun/similar-images-purger/tree/master/idea1) 

## Idea #2 - Turi Create Image Similarity Model

We go down the deep learning route as we find that someone on the internet has already solved our problem for us (or have they?).
Specifically, _Turi Create_ is a python library that creates a model allowing us to identify similar images.

For more details, [follow me](https://github.com/nicholaspun/similar-images-purger/tree/master/idea2) 

## Idea #3 - K-means Clustering of Image Feature Vectors

We stay on the deep learning route, but roll our own models to solve our particular problem.

## Conclusion

### Miscellaneous Note (Converting HEIF files to JPEG)

The models I used didn't accept HEIF files (side note: I was annoyed to discover this after waiting for the `turicreate` model build over only ~1300 of my images instead of all 2000)
My initial idea was to create a Photoshop script to bulk convert them, but unfortunately PS doesn't support the HEIF file format (unless one is on a Mac), so that was a bust.
After a bit of googling, I found _Stuff Jason Does_'s [blog post](http://stuffjasondoes.com/2019/07/10/batch-convert-heic-to-jpg-in-linux/) which utilized  [libheif](https://github.com/strukturag/libheif) to convert HEIF to JPEG and life was good again.
All you have to do is follow these 4 easy steps:

```
# Installation 
sudo add-apt-repository ppa:strukturag/libheif
sudo apt-get install libheif-examples
sudo apt-get update

# Conversion
for f in *.heic; do heif-convert $f ${f%heic}jpg; done
```
Note 1: uhhhh ... 4 easy steps (_provided you're on a linux-based system_). :-)

Note 2: This only converts the `.heic` files ... so, just repeat with `.heif`, `.avif`, etc. for other file types.