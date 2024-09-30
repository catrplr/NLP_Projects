
## Sarcasm Detection Using Deep Learning

This project implements a sarcasm detection model using a dataset of news headlines. The model uses a deep learning approach, specifically a neural network built with TensorFlow and Keras, to classify whether a given headline is sarcastic or not.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [How to Run the Project](#how-to-run-the-project)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The objective of this project is to create a machine learning model that can accurately classify headlines as sarcastic or non-sarcastic. The project leverages deep learning techniques, including tokenization, embedding layers, and dense neural networks.

## Dataset
The dataset used for this project consists of news headlines labeled as sarcastic or non-sarcastic. It can be accessed through the following link:
- [Sarcasm Dataset](https://www.kaggle.com/datasets/rmisra/news-headlines-dataset-for-sarcasm-detection/data)

### Sample Data Structure:
```json

{"is_sarcastic": 1, "headline": "thirtysomething scientists unveil doomsday clock of hair loss", "article_link": "https://www.theonion.com/thirtysomething-scientists-unveil-doomsday-clock-of-hai-1819586205"}

{"is_sarcastic": 0, "headline": "dem rep. totally nails why congress is falling short on gender, racial equality", "article_link": "https://www.huffingtonpost.com/entry/donna-edwards-inequality_us_57455f7fe4b055bb1170b207"}

