# Machine Learning Journey

<p align="center">
  <strong>Learning machine learning by understanding concepts, implementing algorithms, and running experiments.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white" alt="Jupyter notebooks">
  <img src="https://img.shields.io/badge/Focus-Machine%20Learning-2E8B57" alt="Machine learning">
  <img src="https://img.shields.io/badge/Status-Actively%20Learning-blue" alt="Actively learning">
</p>

This repository documents my ongoing study of **Machine Learning** through Jupyter notebooks, exercises, visualisations, and experiments. The emphasis is on understanding why a method works, implementing it, evaluating its behaviour, and recording what I learn.

The repository is a work in progress. Topics and notebooks are added as I study them; a topic listed below does not imply that every planned experiment is complete.

## Explore the repository

| Area | Contents |
|---|---|
| [Foundations](./0foundations/) | Supporting Python and data-tool learning material |
| [Supervised Learning](./01_Supervised_learning/) | Regression, classification, evaluation, scaling, pipelines, and regularisation |
| [Regression](./01_Supervised_learning/Regression/) | Linear and multiple regression, cost functions, gradient descent, polynomial regression, and regularisation |
| [Classification](./01_Supervised_learning/Classification/) | Logistic regression, evaluation metrics, SVM, scaling, pipelines, and Naive Bayes |

## Concepts studied

### Regression
- Linear and multiple linear regression
- Cost functions and gradient descent
- Train/test split and model evaluation
- Polynomial regression
- Underfitting, overfitting, and the bias–variance trade-off
- L1 and L2 regularisation

### Classification
- Binary and multiclass logistic regression
- Confusion matrix, precision, recall, and F1 score
- Support Vector Machines
- Feature scaling and scikit-learn pipelines
- Naive Bayes and classification exercises

## Repository structure

```text
machine-learning/
├── 0foundations/
│   ├── Python/
│   ├── Numpy/
│   ├── Pandas/
│   ├── Matplotlib/
│   ├── SQL/
│   └── LLMs.ipynb
├── 01_Supervised_learning/
│   ├── Classification/
│   └── Regression/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── requirements.txt
├── CONTRIBUTING.md
└── README.md
```

Some existing directory names use legacy spellings. They are retained for now to avoid breaking notebook and dataset paths; any rename should update all affected references in the same change.

## Tools

- **Python** — primary language
- **Jupyter Notebook** — experiments and explanations
- **NumPy and Pandas** — numerical computing and data handling
- **Matplotlib and Seaborn** — visualisation
- **Scikit-learn** — models, preprocessing, and evaluation
- **Git and GitHub** — version control

## Notebook quality checklist

When adding or improving a notebook, aim to include:

1. A short introduction and learning objective.
2. Dataset/source information and relevant assumptions.
3. Clear, ordered steps with readable code.
4. Explanations of important outputs and metrics.
5. A short conclusion describing what the experiment demonstrates.
6. Reproducible execution and relative data paths where practical.

## Roadmap

- [x] Build initial regression and classification study material
- [x] Add exercises and supporting datasets
- [x] Create a foundations area for supporting tools
- [ ] Improve notebook explanations, naming, and reproducibility
- [ ] Complete additional supervised-learning algorithms
- [ ] Study unsupervised learning
- [ ] Build end-to-end machine-learning projects
- [ ] Explore model deployment

## Setup

Clone the repository and install the shared dependencies:

```bash
git clone https://github.com/utkarshxkansal/machine-learning.git
cd machine-learning
python -m venv .venv
```

Activate the virtual environment, then install:

```bash
pip install -r requirements.txt
jupyter notebook
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Contributing and feedback

This is primarily a personal learning repository, but corrections and constructive suggestions are welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidance.

---

<p align="center"><i>Understand the idea. Implement the method. Evaluate the result. Improve the work.</i></p>
