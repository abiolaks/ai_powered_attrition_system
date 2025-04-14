# NOte on ML Metrics.

```
Azure (Preview)
To use the classification_report function from Scikit-learn in your code, you can follow these steps:

Import the Function: Ensure that you have imported classification_report from sklearn.metrics.

Generate Predictions: After training your model, generate predictions on your test dataset.

Use the Function: Call classification_report with your true labels and predicted labels to generate the report.

Here's how you can integrate it into your existing code:

This will output a detailed report showing precision, recall, F1-score, and support for each class, helping you evaluate your model's performance.

abiolaks
@azure What do the precision, recall, and F1-score metrics mean?

Azure (Preview)
Precision, recall, and F1-score are key metrics used to evaluate the performance of a classification model:

Precision: This metric measures the accuracy of positive predictions. It is the ratio of true positive predictions to the total number of positive predictions (true positives + false positives). High precision indicates a low false positive rate. Formula: Precision = True Positives / (True Positives + False Positives).

Recall: Also known as sensitivity, recall measures the model's ability to identify all relevant instances. It is the ratio of true positive predictions to the total number of actual positives (true positives + false negatives). High recall indicates a low false negative rate. Formula: Recall = True Positives / (True Positives + False Negatives).

F1 Score: This is the harmonic mean of precision and recall, providing a balance between the two. It is useful when you need a balance between precision and recall. Formula: F1 Score = 2 * (Precision * Recall) / (Precision + Recall).
```

