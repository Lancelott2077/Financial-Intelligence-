# Datasets Directory

This directory stores sample bank statement CSV files for development and testing.

**These files are NOT committed to source control** (excluded by `.gitignore`).

## Expected CSV Format

The platform supports most major Indian and international bank export formats.
At minimum, a CSV should contain:

| Column type   | Examples                                          |
|---------------|---------------------------------------------------|
| Date          | Date, Transaction Date, Value Date                |
| Description   | Description, Narration, Details, Particulars      |
| Amount        | Amount, Debit, Credit (separate or combined)      |

## Sample Files to Create

| Filename                    | Description                         |
|-----------------------------|-------------------------------------|
| `sample_hdfc.csv`           | HDFC Bank export format             |
| `sample_icici.csv`          | ICICI Bank export format            |
| `sample_sbi.csv`            | SBI Bank export format              |
| `sample_generic.csv`        | Generic format for testing          |

*TODO: Add sample CSV files before Sprint 1 testing.*
