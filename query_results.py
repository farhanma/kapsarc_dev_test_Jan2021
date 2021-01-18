import pandas
data_frame = pandas.read_csv('query_results.csv')
with open('index.html', 'w') as f:
    print(data_frame.to_html(), file=f)