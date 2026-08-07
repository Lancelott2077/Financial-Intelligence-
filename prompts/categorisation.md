# Transaction Categorisation Prompt Template

> TODO: Write the full categorisation prompt.

You are a financial transaction classifier.

Classify each of the following bank transaction descriptions into exactly one of these categories:

**Categories:**
food_and_dining, groceries, transport, entertainment, utilities, healthcare,
shopping, education, travel, income, transfer, other

**Transactions to classify:**
{transaction_descriptions_json}

**Rules:**
- Return a JSON array of strings — one category per transaction, in the same order.
- Use only the category names listed above.
- If uncertain, use "other".

**Output format:**
```json
["category1", "category2", ...]
```
