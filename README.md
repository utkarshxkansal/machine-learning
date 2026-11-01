# Machine Learning Journey

<p align="center">
  <strong>A hands-on repository of machine learning notes, notebooks, exercises, and experiments.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white" alt="Jupyter notebooks">
  <img src="https://img.shields.io/badge/Focus-Machine%20Learning-2E8B57" alt="Machine learning">
  <img src="https://img.shields.io/badge/Status-Actively%20Learning-blue" alt="Actively learning">
</p>

This repository documents my ongoing learning in **Machine Learning**. It contains practical Jupyter notebooks, supporting datasets, visualizations, and exercises as I work through concepts and implement them in Python.

The goal is to understand the ideas behind each technique, experiment with implementations, and gradually build a collection of reproducible ML work. This is a learning repository, so the content and structure will evolve over time.

## Contents

| Area | What you'll find |
|---|---|
| [Supervised Learning](./01_Supervised_learning/) | Regression, classification, model evaluation, feature scaling, pipelines, and regularization |
| [Regression](./01_Supervised_learning/Regression/) | Linear and multiple linear regression, cost function, gradient descent, train/test split, evaluation, polynomial regression, and L1/L2 regularization |
| [Classification](./01_Supervised_learning/Classification/) | Logistic regression, model evaluation, support vector machines, scaling, scikit-learn pipelines, Naive Bayes, and practice exercises |

## Topics covered

### Regression
- Linear regression with one and multiple features
- Cost function and gradient descent
- Training and testing data
- Model evaluation and the (R^2) score
- Polynomial regression
- Underfitting, overfitting, and bias–variance concepts
- L1 and L2 regularization

### Classification
- Binary and multiclass logistic regression
- Confusion matrix and F1 score
- Support Vector Machines (SVM)
- Feature scaling
- Scikit-learn pipelines
- Naive Bayes (SMS spam dataset)
- Classification practice exercises

> The topic lists describe material currently represented in the repository; individual notebooks may be works in progress.

## Repository structure

```text
machine-learning/
├── 01_Supervised_learning/
│   ├── Classification/
│   │   ├── Logistic Regression/
│   │   ├── Model Evaluation/
│   │   ├── Support Vector Machine/
│   │   ├── Scaling/
│   │   ├── Scikit-learn Pipeline/
│   │   ├── Naive Bayes/
│   │   └── Exercises/
│   └── Regression/
│       ├── Linear Regression/
│       ├── Multiple Linear Regression/
│       ├── Cost Function/
│       ├── Gradient Descent/
│       ├── Train-Test Split/
│       ├── Model Evaluation/
│       ├── Polynomial Regression/
│       ├── Underfitting & Overfitting/
│       ├── L1 & L2 Regularization/
│       └── Exercises/
├── requirements.txt
├── CONTRIBUTING.md
└── README.md
```

*Folder names above are descriptive; existing directory names are retained so current notebook and dataset links remain unchanged.*

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/utkarshxkansal/machine-learning.git
cd machine-learning
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch Jupyter

```bash
jupyter notebook
```

Open a notebook from the relevant topic folder. You can also preview notebooks directly on GitHub.

## Tools

- **Python** — primary programming language
- **Jupyter Notebook** — interactive experimentation
- **NumPy & Pandas** — numerical computing and data handling
- **Matplotlib & Seaborn** — visualization
- **Scikit-learn** — machine learning algorithms and workflows
- **Git & GitHub** — version control

## Working with notebooks

- Run notebook cells in order when possible.
- Check that dataset paths are relative to the notebook or repository.
- Keep outputs useful; clear very large or irrelevant outputs before committing.
- Give notebooks descriptive names instead of leaving them as `Untitled.ipynb`.
- Add a short Markdown introduction explaining the objective, dataset, and key concepts.

## Roadmap

- [x] Add initial regression and classification study material
- [x] Include practice exercises and supporting datasets
- [ ] Continue improving notebook explanations and naming
- [ ] Add NumPy, Pandas, and data visualization study notes
- [ ] Add unsupervised learning
- [ ] Build end-to-end machine learning projects
- [ ] Explore model deployment

## Contributions

Suggestions and corrections are welcome. If you spot an issue or want to suggest an improvement, please open an issue or submit a pull request. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the workflow.

---

<p align="center">
  <i>Learning by understanding, implementing, experimenting, and improving.</i>
</p>
