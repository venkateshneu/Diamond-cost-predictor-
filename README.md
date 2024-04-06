# Diamond-cost-predictor-

Overview
🔍 This project aims to predict the price of diamonds using machine learning techniques. The dataset used contains various attributes of diamonds such as carat, cut, color, clarity, depth, table, dimensions, and price. The main objective is to build a regression model that accurately predicts the price of diamonds based on their characteristics.

Key Findings
🔍 Exploratory Data Analysis (EDA): Conducted thorough EDA to understand the distribution and relationships between different attributes. Explored the distribution of the target variable (diamond prices) using visualizations such as histograms, box plots, and correlation matrices.

📈 Linear Regression Model:

Utilized linear regression to model the relationship between diamond attributes and prices.
Cross-validated the model using R-squared scores, achieving an average R-squared score of approximately 0.932 across multiple folds.
Predicted diamond prices for new data points, achieving reasonable accuracy.
🌳 Decision Tree Regressor:

Employed a decision tree regressor to capture non-linear relationships between features and prices.
Achieved an R-squared score of approximately 0.932.
👜 Bagging Regression Techniques:

Implemented bagging regressors with base estimators including Linear Regression, Decision Tree Regressor, and Support Vector Regressor (SVR).
Achieved the highest R-squared score of approximately 0.971 using bagging with KNeighborsRegressor.
Further improved performance using bagging with KNeighborsRegressor in a random subspace setting, obtaining an R-squared score of approximately 0.938.
🔄 Log Transformation of Target Variable:

Observed that the target variable (diamond prices) was right-skewed.
Applied log transformation to the target variable to make its distribution more normal.
Significantly improved the R-squared score of the bagging regressor with KNeighborsRegressor to approximately 0.984.
🔢 Ordinal Encoding:

Based on the EDA performed, ordinal encoding was used for the categorical columns 'cut', 'clarity', and 'color'.
The decision to use ordinal encoding was influenced by insights such as:
Ideal cut diamonds were sold more, indicating that they might be purchased more due to their lower price.
The descending order of clarity and color with respect to price was analyzed to determine the encoding order.
Conclusion
🎉 The project successfully developed regression models to predict diamond prices based on their attributes. Bagging techniques, particularly with KNeighborsRegressor, yielded the highest predictive performance, especially after applying log transformation to the target variable. The findings suggest that ensemble methods such as bagging can effectively handle complex relationships in the data and improve predictive performance.

🚀 Future work may involve exploring other ensemble techniques, feature engineering, or incorporating domain knowledge to further enhance model performance. Additionally, a Flask web application was created to demonstrate the deployment of the trained model, and the code for this application can be found in the GitHub repository along with the model development code.

Tools and Libraries Used
🛠️ Python, Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Statsmodels, Flask





