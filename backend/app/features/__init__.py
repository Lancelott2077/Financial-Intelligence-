"""
features package — Feature extraction from normalised transactions.

Transforms raw transaction data into numerical and categorical features
suitable for behavioural bias detection.

Modules:
    temporal_features       Time-based features (day-of-week, weekend, payday).
    spending_features       Amount-based features (z-score, rolling averages).
    merchant_features       Merchant recurrence and loyalty metrics.
    category_features       Category share and drift metrics.
    feature_matrix          Assembles all features into a unified matrix.
"""
