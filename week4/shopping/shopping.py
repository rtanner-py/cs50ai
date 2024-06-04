import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    for i in range(1,6):
        print(f"Training model with {i} neighbours")
        model = train_model(X_train, y_train, i)
        predictions = model.predict(X_test)
        sensitivity, specificity = evaluate(y_test, predictions)

        # Print results
        print(f"Correct: {(y_test == predictions).sum()}")
        print(f"Incorrect: {(y_test != predictions).sum()}")
        print(f"True Positive Rate: {100 * sensitivity:.2f}%")
        print(f"True Negative Rate: {100 * specificity:.2f}%")
        print("-----------------------------------------------")

def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []

    #get data and put into evidence/labels
    with open(filename) as csvfile:
        data = csv.reader(csvfile)
        headers = next(data)
        for row in data:
            evidence.append(row[0:17])
            labels.append(row[17])

    functions = [int, float, int, float, int, float, float, float, float, float, replaceMonth,int, int, int, int, replaceVisitorType, replaceWeekend]

    # ensure correct types in evidence
    evidence = [[func(val) for val, func in zip(line, functions)] for line in evidence.copy()]

    # ensure numeric values for labels
    labels = [0 if x == "FALSE" else 1 for x in labels.copy()]

    return tuple((evidence, labels))

# My functions

def replaceMonth(month: str) -> int:
    '''
    Takes in month name and returns integer value
    '''
    return {
        'jan': 0,
        'feb': 1,
        'mar': 2,
        'apr': 3,
        'may': 4,
        'june': 5,
        'jul': 6,
        'aug': 7,
        'sep': 8,
        'oct': 9,
        'nov': 10,
        'dec': 11
    }[month.lower()]

def replaceVisitorType(visitor: str) -> int:
    return 1 if visitor == "Returning_Visitor" else 0

def replaceWeekend(weekend: str) -> int:
    return 1 if weekend == "TRUE" else 0


def train_model(evidence, labels, neighbours):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=neighbours)

    X_training = [row for row in evidence]
    y_training = [row for row in labels]

    model.fit(X_training, y_training)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    total_positive = labels.count(1)
    total_negative = labels.count(0)
    true_positive = 0
    true_negative = 0

    for prediction, label in zip(predictions, labels):
        if prediction == label:
            if prediction == 1:
                true_positive += 1
            else:
                true_negative += 1

    sensitivity = float(true_positive / total_positive)
    specificity = float(true_negative / total_negative)

    return tuple((sensitivity, specificity))

    raise NotImplementedError


if __name__ == "__main__":
    main()
