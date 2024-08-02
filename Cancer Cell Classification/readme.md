# Cancer Cell Classification as Benign or Malignant

This project demonstrates the use of **Support Vector Machines (SVM)** to classify human cell records as either benign or malignant. The dataset used is publicly available from the UCI Machine Learning Repository.

## Objectives

- To use scikit-learn to implement SVM for classification.
- To train and evaluate the model using human cell records.
- To compare different kernel functions to determine the best performance.

## Dataset

The dataset consists of several hundred human cell sample records, each containing values of various cell characteristics. The fields include:

- **ID**: Patient identifier
- **Clump**: Clump thickness
- **UnifSize**: Uniformity of cell size
- **UnifShape**: Uniformity of cell shape
- **MargAdh**: Marginal adhesion
- **SingEpiSize**: Single epithelial cell size
- **BareNuc**: Bare nuclei
- **BlandChrom**: Bland chromatin
- **NormNucl**: Normal nucleoli
- **Mit**: Mitoses
- **Class**: Diagnosis (benign = 2, malignant = 4)

## Evaluation Metrics

- Confusion Matrix
- F1-Score
- Jaccard Index

## License

This project is licensed under the MIT License.

