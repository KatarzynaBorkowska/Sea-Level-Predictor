import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot

    plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"])

    # Create first line of best fit

    line1 = linregress(data["Year"], data["CSIRO Adjusted Sea Level"])
    x1 = np.arange(data["Year"].min(), 2050, 1)
    y1 = x1*line1.slope + line1.intercept

    plt.plot(x1, y1)

    # Create second line of best fit

    data2 = data[data["Year"] >= 2000]

    line2 = linregress(data2["Year"], data2["CSIRO Adjusted Sea Level"])
    x2 = np.arange(data2["Year"].min(), 2050, 1)
    y2 = x2 * line2.slope + line2.intercept

    plt.plot(x2, y2)

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()