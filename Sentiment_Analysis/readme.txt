
# Sarcasm Detection Using Deep Learning

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
- [Sarcasm Dataset](https://storage.googleapis.com/tensorflow-1-public/course3/sarcasm.json)

### Sample Data Structure:
```json
{
  "headline": "Scientists to kill ducks to see why they are dying",
  "is_sarcastic": 1
}
