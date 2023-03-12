## Visualization Script
This script loads maintenance data from a CSV file using pandas library and calculates the duration of each maintenance request based on the difference between the request date and completion date. It then visualizes the maintenance request counts over time using a histogram and the maintenance request durations over time using a boxplot.
## Requirements
Python 3.6 or higher
pandas library
matplotlib library
## Installation
Download the script files from the GitHub repository.
Install the required libraries using pip: pip install pandas matplotlib
## Usage
Place the maintenance data CSV file in the same directory as the script files.
Open the question3.py file and customize the plot title, x-axis label, y-axis label, histogram bins, and boxplot figure size as needed.
Run the script: python question3.py
The script will output two visualizations - a histogram of maintenance request counts over time and a boxplot of maintenance request durations over time.
## Customization
You can customize the plot title, x-axis label, y-axis label, histogram bins, and boxplot figure size by modifying the following variables in the question3.py file:
PLOT_TITLE: plot title
X_LABEL: x-axis label
Y_LABEL: y-axis label
HIST_BINS: number of bins for the histogram
FIG_SIZE: figure size for the boxplot
You can also modify the code in the script to add additional visualizations or modify the existing visualizations.
