# Weather Prediction

```bash
https://weather-prediction-ketnqhcothesbccadc3omp.streamlit.app/
```
Welcome to the Weather Prediction project! This project aims to predict weather conditions using historical data and a Linear Regression model from sklearn.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview
This project is a basic implementation of a weather prediction model. It uses historical weather data to predict future weather conditions for the next 7 days. The primary goal of this project is to increase knowledge and understanding of machine learning concepts and their application in weather prediction.

## Installation
To get started with this project, follow these steps:

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/Weather-Prediction.git
    cd Weather-Prediction
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Prepare the dataset**
    - Ensure you have the dataset in the `Dataset` directory.
    - The dataset should include `Weather.csv` and `Weather_mod_dataset.csv`.

2. **Run the application**
    ```bash
    streamlit run app.py
    ```

3. **Navigate the application**
    - **Home**: View original and modified data, and visualize data with daily, monthly, and yearly plots.
    - **Prediction**: Predict weather for the next 7 days and get specific predictions by date.
    - **Contribution**: Add new weather data to the dataset.

## Contributing
Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information on how to contribute to this project.
