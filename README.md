# Movie Recommendation System using content based filtering

## Objective: _To recommend movies which are similar to the movie searched by the user._

## Data Source: _[tmdb-movie-metadata](https://www.kaggle.com/tmdb/tmdb-movie-metadata)_

## Live Web App: _[recommendation-system-movies.herokuapp.com](https://recommendation-system-movies.herokuapp.com/)_

## Tools & Tech:
- Python 3.8
- scikit-learn
- streamlit
- requests
- tmdb movies API
- heroku cloud
## Similarity Score : 

How does it decide which item is most similar to the item searched by user? similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by <b>cosine-similarity</b>.

## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)
<br>
## Preview
1.<br>
![Home](https://github.com/ashok49473/movie-recommendation-system/blob/main/hhome.png)
<br>
2.<br>
![first](https://github.com/ashok49473/movie-recommendation-system/blob/main/first.png)
<br>
3.<br>
![second](https://github.com/ashok49473/movie-recommendation-system/blob/main/sec.png)
<br>
##### Thank you !

