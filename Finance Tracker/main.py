import pandas as pd
import csv
from datetime import datetime


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["DATE","AMOUNT","CATEGORY","DESCRIPTION"]
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls, date, amount, cat, desc):
        new_entry = {
            "DATE": date,
            "AMOUNT": amount,
            "CATEGORY": cat,
            "DESCRIPTION": desc
        }
        with open(CSV.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

        print("Entry Added")

CSV.initialize_csv()
CSV.add_entry("20-07-2024",1500,"Expense","Trial")
