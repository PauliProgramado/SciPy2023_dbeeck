import os
import pandas as pd
import make_interface


def main():
    """Start programm"""

    #check if 'combined.csv' exists, if not create it
    if not (os.path.exists('combined.csv')):
        empty_df = pd.DataFrame(list())
        empty_df.to_csv('combined.csv')

    df = pd.DataFrame(data={'Type': [], 'Correct': [], 'Time' : []})
    make_interface.start_page(df)

if __name__ == "__main__":
    main()