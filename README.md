A similarity matching model for parents living in the Phoenix metropolitan region has be created by our team. Parents will be able to determine which five schools in their city are most comparable to the reference school of their choice by using this process. By examining a range of school characteristics, including academic achievement, extracurricular activities, facilities, and other pertinent criteria, the method will identify schools that closely align with each parent's preferences and objectives. Similarity matching is the goal of data mining related to this topic; data attributes referring to the traits and performance of schools will be collected, cleaned, and analyzed to construct an effective matching model.

Data Collection and Preprocessing:
Compile information on the schools in the metropolis of Phoenix. Metrics measuring academic achievement, the availability of extracurricular activities, facilities, student demographics, etc., may be included. Deal with outliers, inconsistent data, and missing numbers to clean up the data.
Scale or normalize numerical features; properly encode categorical variables.


Model Building & Evaluation:
•	Data Loading: The dataset providing details about schools in the Phoenix metropolitan area must be loaded first. Numerous aspects of schools, such as academic standing, extracurricular activities, facilities, etc., should be included in this dataset. A school is represented by each row, and a feature is represented by each column.

•	Reference School Selection: Under this technique, parents choose a reference school to use as a guide when looking for other schools that are comparable. The similarity scores between this school and the other schools in the dataset are computed using this reference school.

•	Feature Extraction: We extract the features from the target variable (school names) after the data has been loaded. The features of every other school in the dataset are regarded as possible matches, while the features of the reference school are retrieved as the benchmark.

•	Calculating MSE and RMSE of various Similarity matching models: The following Similarity matching models were used.

o	Cosine Similarity: Cosine similarity measures the cosine of the angle between two non-zero feature vectors in an inner product space. In our scenario, cosine similarity is calculated between the feature vectors of the reference school and each other school. Higher cosine similarity scores indicate greater similarity between schools.

o	Euclidean Distance: Euclidean distance is a measure of the straight-line distance between two points in a Euclidean space. In our context, it quantifies the dissimilarity between the feature vectors of the reference school and each other school. Lower Euclidean distance values imply higher similarity between schools.

o	Jaccard Similarity: Jaccard similarity measures the similarity between two sets by comparing their intersection to their union. In our case, Jaccard similarity is computed based on the presence or absence of certain features in the feature vectors of the reference school and each other school. Higher Jaccard similarity scores suggest greater similarity between schools.

o	Pearson Correlation Coefficient: Pearson correlation coefficient measures the linear correlation between two variables. Here, it quantifies the strength and direction of the linear relationship between the feature vectors of the reference school and each other school. Higher absolute values of the Pearson correlation coefficient indicate stronger linear relationships, implying higher similarity between schools.

•	Model Evaluation: We rank the schools according to how similar they are to the reference school by adding up the scores obtained from the similarity calculations for each fold. The schools that are deemed most comparable to the reference institution are the top five with the highest similarity scores.
