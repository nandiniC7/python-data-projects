"""
Stock Market Data Analyzer

This module provides a basic structure for loading,
preprocessing, analyzing, and visualizing stock market data.
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Load stock market data from a CSV file.

    Parameters:
        file_path (str): Path to CSV file

    Returns:
        pandas.DataFrame: Loaded dataset
    """
    return pd.read_csv(file_path)


def preprocess_data(data):
    """
    Clean and preprocess the dataset.

    - Removes missing values
    - Ensures proper data format

    Parameters:
        data (pandas.DataFrame): Raw dataset

    Returns:
        pandas.DataFrame: Cleaned dataset
    """
    data = data.dropna()
    return data


def calculate_indicators(data):
    """
    Calculate basic technical indicators.

    Currently implemented:
    - Simple Moving Average (SMA)

    Parameters:
        data (pandas.DataFrame): Cleaned dataset

    Returns:
        pandas.DataFrame: Dataset with indicators
    """
    data["SMA_20"] = data["Close"].rolling(window=20).mean()
    return data


def visualize_data(data):
    """
    Visualize stock price and moving average.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data["Close"], label="Close Price")
    plt.plot(data["SMA_20"], label="20-Day SMA")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("Stock Price Analysis")
    plt.legend()
    plt.show()


def analyze_data(data):
    """
    Perform basic statistical analysis.
    """
    return data.describe()


if __name__ == "__main__":
    print("Stock Market Data Analyzer module loaded successfully.")
