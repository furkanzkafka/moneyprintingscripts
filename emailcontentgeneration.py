import pandas as pd

# Define the email template
EMAIL_TEMPLATE = """
Hi {Name},

{Institution} would be an ideal partner

Sincerely,
"""

def generate_emails(input_csv, output_csv):
    # Read the input CSV
    data = pd.read_csv(input_csv)

    # Check if necessary columns are present
    required_columns = ['Name', 'Institution', 'Email']
    if not all(col in data.columns for col in required_columns):
        raise ValueError(f"Input CSV must contain the following columns: {', '.join(required_columns)}")

    # Generate personalized emails
    data['Generated Email Content'] = data.apply(
        lambda row: EMAIL_TEMPLATE.format(Name=row['Name'], Institution=row['Institution']),
        axis=1
    )

    # Save the output to a new CSV
    data.to_csv(output_csv, index=False)
    print(f"Generated emails saved to {output_csv}")


# Example usage
input_file = "CleanColdEmailList.csv"  # Input file path
output_file = "generated_emails.csv"  # Output file path
generate_emails(input_file, output_file)
