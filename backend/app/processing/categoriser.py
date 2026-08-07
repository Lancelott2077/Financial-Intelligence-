"""
processing/categoriser.py — Transaction spending category classifier.

Assigns a spending category to each transaction using deterministic keyword rules.
Transactions that cannot be confidently categorised are assigned to 'other'.
"""

from __future__ import annotations

import pandas as pd
import re
from app.schemas.common import SpendingCategory

# Keyword rules for each spending category.
# Order in the dictionary determines priority (first match wins).
KEYWORD_RULES: dict[SpendingCategory, list[str]] = {
    SpendingCategory.FOOD_AND_DINING: ["restaurant", "cafe", "coffee", "swiggy", "zomato", "starbucks", "mcdonalds", "kfc", "dominos", "pizza", "dining", "eats"],
    SpendingCategory.GROCERIES: ["supermarket", "grocery", "mart", "bazaar", "reliance fresh", "d-mart", "bigbasket", "blinkit", "zepto", "instamart", "dairy"],
    SpendingCategory.TRANSPORT: ["uber", "ola", "rapido", "petrol", "fuel", "hpcl", "bpcl", "indian oil", "metro", "railway", "irctc", "flight", "taxi", "toll", "fastag"],
    SpendingCategory.ENTERTAINMENT: ["netflix", "amazon prime", "spotify", "cinema", "pvr", "inox", "bookmyshow", "hotstar", "gaming", "steam"],
    SpendingCategory.UTILITIES: ["electricity", "water", "gas", "bill", "recharge", "jio", "airtel", "vi", "bsnl", "broadband", "wifi", "telecom", "bescom"],
    SpendingCategory.HEALTHCARE: ["hospital", "pharmacy", "clinic", "apollo", "medplus", "netmeds", "pharma", "health", "doctor"],
    SpendingCategory.SHOPPING: ["amazon", "flipkart", "myntra", "ajio", "zara", "h&m", "mall", "store", "shopping", "apparel"],
    SpendingCategory.EDUCATION: ["school", "college", "university", "tuition", "course", "udemy", "coursera", "fee", "institute"],
    SpendingCategory.TRAVEL: ["hotel", "makemytrip", "goibibo", "yatra", "agoda", "airbnb", "resort", "booking.com"],
    SpendingCategory.INCOME: ["salary", "payroll", "dividend", "interest", "refund", "deposit", "cashback", "reward"],
    SpendingCategory.TRANSFER: ["upi", "transfer", "neft", "imps", "rtgs", "atm", "cash withdrawal", "paytm", "phonepe", "gpay", "bharatpe"]
}

# Precompile regex patterns globally to avoid rebuilding them on every categorise() call
COMPILED_PATTERNS: dict[SpendingCategory, re.Pattern] = {}
for category, keywords in KEYWORD_RULES.items():
    if keywords:
        # Clean keywords identically to ensure matching (e.g. "d-mart" -> "d mart")
        clean_keywords = [re.sub(r'[^a-z0-9]', ' ', kw.lower()) for kw in keywords]
        # Create regex pattern for word boundary matches
        pattern_str = r'\b(?:' + '|'.join(map(re.escape, clean_keywords)) + r')\b'
        COMPILED_PATTERNS[category] = re.compile(pattern_str)


class Categoriser:
    """Classifies transactions into spending categories."""

    def categorise(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Add a 'category' column to the normalised DataFrame.

        Args:
            df: Normalised DataFrame (must have 'description' column).

        Returns:
            DataFrame with 'category' column populated.
        """
        df_cat = df.copy()
        
        # Default all transactions to the repository's default fallback category
        df_cat["category"] = SpendingCategory.OTHER.value
        
        # Early exit if no description column
        if "description" not in df_cat.columns:
            return df_cat
            
        # Clean descriptions for matching: replace non-alphanumeric with spaces.
        # This allows accurate word-boundary (\b) regex matching even in messy bank strings like "UPI/PAYTM/123".
        desc_clean = df_cat["description"].fillna("").astype(str).str.lower()
        desc_clean = desc_clean.str.replace(r'[^a-z0-9]', ' ', regex=True)
        
        # Apply precompiled regex patterns
        for category, compiled_pattern in COMPILED_PATTERNS.items():
            # Find matching rows robustly
            mask = desc_clean.str.contains(compiled_pattern, regex=True, na=False)
            
            # Only update rows that are still 'other' (first match wins to prevent conflicts)
            update_mask = mask & (df_cat["category"] == SpendingCategory.OTHER.value)
            df_cat.loc[update_mask, "category"] = category.value
            
        return df_cat
