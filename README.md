
# Cyber Security ANN

This project applies machine learning algorithms, including isolation forests and neural networks, to cybersecurity datasets for anomaly detection and predictive analysis. The project includes a variety of models with detailed comparisons and insights.

## Project Structure

- `isolation_forest.ipynb`: Implements the Isolation Forest algorithm for anomaly detection, focusing on identifying outliers in the dataset.
- `NN.ipynb`: Builds a basic neural network model for predictive analysis on the cybersecurity datasets.
- `wrefined_NN.ipynb`: Refines the neural network model by incorporating techniques such as **SMOTE** to oversample minority classes and improve model performance on imbalanced datasets.
- `unify_datasets.py`: Preprocesses and unifies multiple datasets, ensuring consistency and readiness for model training.
- `datasets/`: A directory to store the datasets used in the project (you need to create this manually in the main directory).

## Model Comparisons

1. **Isolation Forest**:
   - Purpose: Anomaly detection by identifying outliers.
   - Strength: Works well for unsupervised learning scenarios.
   - Limitation: May not perform as well with heavily imbalanced datasets.

2. **Neural Network (NN.ipynb)**:
   - Purpose: Predictive modeling with a basic feedforward neural network.
   - Strength: Provides a baseline for neural network performance.
   - Limitation: Performance may degrade with imbalanced datasets.

3. **Refined Neural Network (wrefined_NN.ipynb)**:
   - Purpose: Improves upon the basic neural network by addressing imbalances using **SMOTE** (Synthetic Minority Oversampling Technique).
   - Strength: Handles imbalanced datasets effectively, improving recall for minority classes.
   - Limitation: Synthetic data generation may introduce noise if not carefully handled.

## Installation

To set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/egoistas/cyber_securityANN.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd cyber_securityANN
   ```
3. **Create the `datasets/` Directory**:
   Create a directory named `datasets` in the main project folder to store your datasets:
   ```bash
   mkdir datasets
   ```
4. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
5. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scriptsctivate
     ```
   - On Unix or macOS:
     ```bash
     source venv/bin/activate
     ```
6. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preparation**:
   - Place your datasets in the `datasets/` directory.
   - Run `unify_datasets.py` to preprocess and unify the datasets.

2. **Model Training and Evaluation**:
   - Open and run the Jupyter notebooks (`.ipynb` files) to train and evaluate the models.

3. **Results Analysis**:
   - Compare the outputs of different models to determine the best approach for your data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## Acknowledgements

Special thanks to all contributors and supporters of this project.
