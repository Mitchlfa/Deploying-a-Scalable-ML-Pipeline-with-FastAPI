# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a RandomForestClassifier with 100 estimators. It was trained to predict whether an individual's salary is greater than $50K based on demographic features in the census dataset.

## Intended Use
The model is intended for predicting income levels (<=50K or >50K) based on census data, such as age, education level, occupation, and more. It is suitable for applications that require income classification.

## Training Data
The training data consists of 32,561 entries from the UCI Adult Income dataset. The data includes features such as age, education, occupation, and marital status. Categorical features were one-hot encoded, and missing values were filled with the most frequent value for each categorical column.

## Evaluation Data
The model was evaluated using a test set that was 20% of the original dataset. The test set contains 6,512 entries, and the model was evaluated based on its ability to correctly predict salary classification.

## Metrics
Precision: 0.7466
Recall: 0.6378
F1: 0.6880
These metrics were calculated using the precision, recall, and F1 score, which evaluate the model's ability to make correct predictions for both classes.

## Ethical Considerations
This model is trained on census data, which may contain biases related to age, gender, race, and other factors. Care should be taken to ensure that the model does not reinforce or amplify these biases when deployed in real-world applications.

## Caveats and Recommendations
The model's performance on rare categories or small sample sizes may not be as reliable.

The model might be biased based on the demographic characteristics present in the training data. Additional steps should be taken to assess fairness and reduce bias.
