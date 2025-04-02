# Housing Price Prediction - MLOps Project

## Overview
This repository demonstrates a complete MLOps setup for a housing price prediction model. It integrates MLflow for experiment tracking and model registry, alongside MinIO for artifact storage.

## Project Structure
```
📂 housing-mlops/
├── 📂 data/               # Dataset files (not included in repo)
├── 📂 notebooks/          # Jupyter notebooks for analysis and model training
│   ├── 📄 01_eda.ipynb    # Exploratory Data Analysis (EDA)
│   └── 📄 02_model_training.ipynb # Model training with MLflow tracking
├── 📂 scripts/            # Utility scripts
│   └── 📄 s3_utils.py     # MinIO/S3 utilities for data and model storage
├── 📄 .gitignore          # Ignore unnecessary files in version control
├── 📄 docker-compose.yml  # Docker configuration for MLflow, MinIO, Jupyter
└── 📄 requirements.txt     # Project dependencies
```

## Technology Stack
- **Python 3.11** - Core programming language
- **Scikit-learn** - Machine learning library for model development
- **MLflow** - Experiment tracking, model versioning, and registry
- **MinIO** - S3-compatible object storage for models and artifacts
- **Docker** - Containerization for reproducibility
- **Jupyter** - Interactive development and visualization

## MLOps Implementation
This project follows MLOps best practices with:
- **Data Versioning**: Housing data is stored in MinIO with version control.
- **Experiment Tracking**: MLflow logs all model training runs.
- **Model Registry**: Trained models are stored and versioned in MLflow.
- **Reproducible Environment**: Docker ensures a consistent setup for development and deployment.

## Getting Started
### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Services with Docker
```bash
docker-compose up -d
```

### 3. Access Services
- **MLflow UI**: `http://localhost:5000`
- **MinIO Console**: `http://localhost:9001`
- **Jupyter Notebook**: `http://localhost:8888`

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

## License
This project is licensed under the Apache License 2.0 License.


