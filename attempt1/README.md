# Attempt 1 - Document Distance

## Various approaches

1. Using histograms

    One approach to document distance is to create a vector of word frequencies for each document and then find the angular distance between the two vectors.
    Analogously, we can compute the angular distance between the histograms of two images.
    This approach is used in `histogram_approach.py`.

2. Treating the image as one big vector

    Another approach is treating the image as one big vector and then computing the angular distance much like with the histograms.
    This appraoch is used in `one_big_vector_approach.py`.

3. Average distance of all pixels

    We compute the distance between each pixel (of the two images) separately, then compute an average.
    This appraoch is used in `average_distance_approach.py`

## Results and Discussion
We use the following images (and call them `image#`, where `#` is its order of appearance, from left-to-right):
<div style="text-align: center">
    <img src="images/image1.jpg" width="100"/>
    <img src="images/image2.jpg" width="100"/>
    <img src="images/image3.jpg" width="100"/>
    <img src="images/image4.jpg" width="100"/>
</div>

The raw output for each approach can be found in `out_hist`, `out_big` and `out_hist`.
A number close to 0 means "similar".

**To summarize the raw output**: The histogram approach and averaged distance approach both seem to be useful.

I would say that the histogram approach is the most natural.
It is analogous to the word frequency approach for document distance and we find good results---`image3` and `image4` have small angular distance, but the remaining pairs have larger angular distance.

I realized after coding up the 2nd approach that I really shouldn't expect much from it.
We don't quite capture the right type of information and hence don't quite obtain any useful aggregate information.
The vector contains perfect information on each pixel, but as a result, a small perturbation in a single pixel doesn't have much affect on the overall result.
This results in crazy small numbers, _but_ we do perserve the relative information---that is, `image3` and `image4` still have relatively smaller angular distance.

The averaged distance approach also seems intuitively sane.
Similar images will differ very little pixel-by-pixel, and indeed this approach beats the histogram approach with respects to recognizing that `image3` and `image4` are similar.
I'll note that there was a bug I couldn't figure out where I was getting `Nan`s in my norms calculation.
I ended up using `numpy.nanmean` over `numpy.average` instead of figuring it out.
(i.e. This approach may not be perfect)