# ds-intro-basics
A beginner-friendly Python project covering the core Data Science workflow: loading a CSV dataset, cleaning missing values, performing exploratory data analysis (EDA), and visualizing results with charts. Great for anyone starting to learn Data Science fundamentals.
# Data Science Basics 📊

A beginner-friendly Python project demonstrating the **core workflow of Data Science**: loading data, cleaning it, exploring it, and visualizing it — all in one simple script.

This project is a great starting point for anyone learning the fundamentals of Data Science, covering the topics typically taught in an "Introduction to Data Science" course:

- Data loading (CSV)
- Data cleaning (handling missing values)
- Exploratory Data Analysis (EDA)
- Data visualization (charts)

## 📁 Project Structure

```
ds-intro-basics/
├── main.py              # Main script — runs the full workflow
├── students_data.csv    # Sample dataset (with intentional missing values)
├── requirements.txt     # Python dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ds-intro-basics.git
   cd ds-intro-basics
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the main script:

```bash
python main.py
```

## 🧠 What This Project Demonstrates

| Step | What Happens |
|------|--------------|
| **1. Load Data** | Reads `students_data.csv` into a Pandas DataFrame |
| **2. Clean Data** | Fills missing numeric values with the column mean, and missing categorical values with `"Unknown"` |
| **3. Explore Data** | Prints summary statistics and average score grouped by city |
| **4. Visualize Data** | Generates two charts: a bar chart of student scores and a scatter plot of study hours vs. score |

## 📈 Output

After running the script, you'll see:
- Console output showing raw data, cleaned data, and statistics
- Two image files saved in the project folder:
  - `scores_chart.png` — Bar chart of student scores
  - `study_vs_score.png` — Scatter plot of study hours vs. score

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/) — data manipulation
- [Matplotlib](https://matplotlib.org/) — data visualization

## 📚 Concepts Covered

This project maps directly to core Data Science fundamentals:
- Structured data handling
- Missing value treatment
- Descriptive statistics
- Basic data visualization

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this repo and submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
