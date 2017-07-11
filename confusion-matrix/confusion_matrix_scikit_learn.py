from __future__ import division
from sklearn.metrics import confusion_matrix

y_actual = [1, 0, 0, 1, 1, 1, 1, 1, 1, 0]
y_predicted = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]

# if the labels are not given scikit learn rearranges. Also rows are actual values and columns are predictions
confusion_m = confusion_matrix(y_actual, y_predicted, labels=[1, 0])
print ("Confusion Matrix")
print(confusion_m)

tp = confusion_m[0][0]    # true positives
fn = confusion_m[0][1]    # false negatives
fp = confusion_m[1][0]    # false positive
tn = confusion_m[1][1]    # true negatives

print("\nTrue Positives  : " + str(tp))
print("False Negatives : " + str(fn))
print("False Positives : " + str(fp))
print("True Negatives  : " + str(tn) + "\n")

# pay attention to denominator being zero
accuracy = (tp+tn)/(tp+fn+fp+tn)
precision = tp/(tp+fp)
recall = tp/(tp+fn)
f1_score = 2*(precision*recall)/(precision+recall)

print("Accuracy  : " + str(accuracy))
print("Precision : " + str(precision))
print("Recall    : " + str(recall))
print("F1-score  : " + str(f1_score))
