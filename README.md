# Exploratory-Data-Analysis-on-Electric-Vehicles
This project conducts an Exploratory Data Analysis (EDA) on electric vehicles, aiming to visualize key trends and performance metrics. Insights gathered are intended to inform stakeholders—manufacturers, consumers, and policymakers—about the electric vehicle market. The analysis is further enhanced with Tableau for interactive visual storytelling.

## Objectives
The primary objectives of this EDA project are as follows:

-[Data Understanding](#Data-undersatnding):
Gain an understanding of the dataset's structure, including its features and types.
Identify the relevance of different features in relation to electric vehicle performance.

-[Data Cleaning](#Data-Cleaning):
Detect and address any missing or null values within the dataset.
Remove irrelevant or redundant columns that do not contribute to the analysis.
Convert data types as needed to ensure proper analysis (e.g., date formats, categorical variables).

-[Statistical Summary](#Statistical-Summary):
Provide a statistical overview of the dataset using descriptive statistics (mean, median, mode, variance, etc.).
Identify outliers or anomalies that could skew analysis results.

-[Correlation Analysis](#correlation-Analysis):
Investigate relationships between numerical features using correlation matrices.
Use heatmaps to visualize these relationships, helping to understand potential influences among features.

-[Visual Exploratory Analysis](#Visual-Exploratory-Analysis):
Create a variety of visualizations to explore the dataset, including:
1. Pie Charts: To represent the distribution of features like seating capacity, drive types, and charge speeds.
2. Count Plots: To illustrate the number of vehicles produced by each manufacturer.
3. Box Plots: To compare distributions of electric ranges and top speeds across different manufacturers.
4. Scatter Plots: To examine relationships between acceleration time, total torque, electric range, and battery capacity.

-[Statistical Insights](#Statistical-Insights):
Analyze key performance indicators for electric vehicles, such as:
Best-performing vehicles based on top speed, electric range, battery capacity, and efficiency metrics.
Identify standout manufacturers in specific areas, such as range efficiency in various weather conditions.

-[Tableau Visualizations](#Tableau-visualizations):
Extend the findings from the EDA with Tableau to create interactive and advanced visualizations.
Develop dashboards that allow stakeholders to drill down into specific metrics and features.

## Dataset Description
The dataset used for this analysis is sourced from the GitHub EV Car Analysis Dataset.
It comprises several features of electric vehicles, including:
1. Manufacturer: The brand of the electric vehicle.
2. Model Number: Specific model identifiers.
3. Electric Range: Distance the vehicle can travel on a full charge.
4. Top Speed: Maximum speed the vehicle can achieve.
5. Acceleration Time: Time taken to accelerate from 0 to 60 mph.
6. Battery Capacity: Total energy storage capacity of the vehicle's battery.
7. Charge Speed: Rate at which the vehicle charges.
8. Seating Capacity: Number of passengers the vehicle can accommodate.
9. Drive Type: The type of drivetrain used (e.g., FWD, RWD, AWD).
10. Cargo Volume: Amount of storage space in the vehicle.

## Installation
To run this project, you will need the following Python libraries:
```
pip install pandas numpy matplotlib seaborn plotly
```
## Usage
1. Clone this repository:
```
git clone https://github.com/your-username/electric-vehicles-eda.git
```
2. Navigate to the project directory:
```
cd electric-vehicles-eda
```
3. Run the EDA script:
```
python eda_script.py
```


## Visualizations
The project includes various visualizations that effectively convey findings from the data analysis. Some examples include:
1. Distribution of Electric Range: A histogram showing the distribution of electric ranges across different models.
2. Manufacturer Performance: A bar chart ranking manufacturers by their average electric range.
3. Comparison of Acceleration Times: Box plots comparing acceleration times among various models to highlight performance differences.

###### To further enhance these insights, the project was later extended into a comprehensive Tableau dashboard, offering a more interactive and visually rich exploration of the data.
###### Explore the interactive visualizations and insights on electric vehicles through the extended analysis in Tableau [here](https://public.tableau.com/app/profile/shivani.pande2719/viz/CarAnalysisDashboard_17029103068390/Dashboard3).

## Conclusion.
This project provides a comprehensive analysis of electric vehicles through detailed exploratory data analysis and visualizations. The insights derived from this analysis can aid manufacturers in understanding market trends, consumers in making informed purchasing decisions, and policymakers in developing regulations or incentives related to electric vehicles.

## Future Work
Potential future work includes:
1. Integrating additional datasets (e.g., market trends, sales data) for more extensive analysis.
2. Applying machine learning techniques to predict electric vehicle performance based on features.
3. Conducting sentiment analysis on consumer reviews to gauge public perception of electric vehicles.

## Acknowledgements
1. Dataset Source: GitHub EV Car Analysis Dataset
2. Libraries Used: ```Pandas```, ```NumPy```, ```Matplotlib```, ```Seaborn```, ```Plotly```, ```Tableau```.

