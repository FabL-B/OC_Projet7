# Investment Optimization Project in Python

## Description:

This project focuses on creating algorithms to calculate the best combination of stocks to maximize the cost/profit ratio. Two types of algorithms are used:
1. A **bruteforce algorithm** that determines all possible combinations.
2. An **optimized algorithm** that uses dynamic programming to find the best combination.

## Features:
### Investment Optimization:

    - Explore all possible combinations of stocks with the **bruteforce** algorithm.
    - Use dynamic programming to optimize the stock selection process with the **optimized** algorithm.

### Dataset Management:

    - Customize the dataset by modifying the CSV file path in the scripts.
    - Supports CSV files formatted with columns: name, price, and profit.

### Example of Data:

    CSV files must be formatted as follows:

    ```csv
    name,price,profit
    Stock-1,20,5
    Stock-2,30,10
    Stock-3,50,15
    ```

## Installation:

1. Open the terminal.

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/FabL-B/OC_Projet7
    cd OC_Projet7
    ```

3. Create and activate the virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate (for Linux and Mac)
    env\Scripts\activate (for Windows)
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage:

1. To run the **bruteforce algorithm**:

    ```bash
    python brute_force.py
    ```

2. To run the **optimized algorithm**:

    ```bash
    python optimized.py
    ```

3. Change the dataset being used by modifying the `FILE_PATH` variable in the script files, for example:

    ```python
    FILE_PATH = "data/dataset2.csv"
    ```