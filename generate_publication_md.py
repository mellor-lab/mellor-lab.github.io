import pandas as pd

# on pubmed search for author and then export all publications as a csv
# Open the CSV file and read it into a Pandas dataframe
df = pd.read_csv('csv-MellorJR-set.csv')

prev_year = ""
# Open the Markdown file for writing
with open('book\contents\publications.md', 'w') as file:
    file.write('## Publications\n\n')
    file.write('&nbsp; \n')
    # Loop through each row in the dataframe
    for index, row in df.iterrows():
        # Extract the title and author from the current row
        title = row['Title']
        author = row['Authors']
        journal = row['Journal/Book']
        year = row['Publication Year']
        DOI = row['DOI']
        
        curr_year = year
         
        # pubmed gets some old papers that are not Jacks
        if year >= 1990:
            if not curr_year == prev_year:
                file.write('&nbsp;\n\n  **{}**\n\n---\n'.format(year))
                            
            # Print a formatted string containing the title and author
            file.write('_{}_<br>\n{}<br>\n{}, **`{}`** ([article](https://doi.org/{}))<br>\n\n'.format(title, author, journal, year,DOI))
        
        prev_year = year