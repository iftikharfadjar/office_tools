import argparse
from getBacklog import * 

def main():
    parser = argparse.ArgumentParser(
        description="Extract, map, reorder, and rename columns from Excel."
    )
    
    parser.add_argument("input", help="Path to input Excel file")
    parser.add_argument("-o", "--output", help="Path to output CSV file")
    parser.add_argument("-s", "--sheet", help="Specific sheet name")
    parser.add_argument("-k", "--keyword", default="Backlog", help="Header keyword (default: 'Backlog')")
    parser.add_argument("-c", "--columns", help="Exact column titles to extract and order (e.g. 'Backlog,Description')")
    
    # NEW ARGUMENT FOR RENAMING
    parser.add_argument("-r", "--rename", help="Rename columns using OldName=NewName format (e.g. 'Backlog=Ticket ID, Description=Details')")

    args = parser.parse_args()

    process_excel(args.input, args.output, args.sheet, args.keyword, args.columns, args.rename)

if __name__ == "__main__":
    main()