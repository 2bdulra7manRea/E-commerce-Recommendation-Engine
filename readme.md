# E-commerce Recommendation Engine

## Overview

This project implements a products recommendation engine for an e-commerce platform, combining collaborative filtering, content-based filtering, and cosine similarity. The system is designed to provide personalized products recommendations based on user behavior and products features.

## Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Collaborative filtering
- Content-based filtering
- Cosine similarity for recommendation
- Scalable design for handling growing user base and product catalog

## Requirements

- Python 3.x
- Pandas
- Scikit-learn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/2bdulra7manRea/E-commerce-Recommendation-Engine.git
    ```

2. Navigate to the project directory:

    ```bash
    cd E-commerce-Recommendation-Engine
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the required dataset (`dataset.csv`) in the project directory.
2. Update the dataset if needed.
3. Run the recommendation engine:

    ```bash
    python main.py
    ```

4. Adjust parameters in the `perform` function for different recommendations.

## Project Structure

- `recommendation_engine.py`: Contains functions for data processing, similarity calculation, and recommendation.
- `dataset.csv`: Sample dataset.


## Development Status

This project is currently under development. Expect changes and updates.


## License

This project is licensed under the [MIT License](LICENSE).