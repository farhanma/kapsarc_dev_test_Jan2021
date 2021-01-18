# KAPSARC Development Test

## Quickstart

```
# clean up the input data file (remove the first 4 lines)
sed -i -e 1,4d world_primary_15_65527066353070.csv
```

    * Note you need to install [SQLite](https://www.sqlite.org/index.html) database

```
# Create new SQLite database
sqlite3 jodidb.db
```

    * Once database is created:

```
-- Import csv data into a SQL table
.mode csv table0
.import world_primary_15_65527066353070_edited.csv table0
-- Do necessary tweaks to transpose columns into rows and order the output
-- Note: SQLite doesn't support pivot SQL command.
create table table2 as
    select * from (
        select Country as 'country', 'Aug2019' as 'month-year', Aug2019 as value from table0
        union all
        select Country as 'country', 'Sep2019' as 'month-year', Sep2019 as value from table0
        union all
        select Country as 'country', 'Oct2019' as 'month-year', Oct2019 as value from table0
        union all
        select Country as 'country', 'Nov2019' as 'month-year', Nov2019 as value from table0
        union all
        select Country as 'country', 'Dec2019' as 'month-year', Dec2019 as value from table0
        union all
        select Country as 'country', 'Jan2020' as 'month-year', Jan2020 as value from table0
        union all
        select Country as 'country', 'Feb2020' as 'month-year', Feb2020 as value from table0
        union all
        select Country as 'country', 'Mar2020' as 'month-year', Mar2020 as value from table0
        union all
        select Country as 'country', 'Apr2020' as 'month-year', Apr2020 as value from table0
        union all
        select Country as 'country', 'May2020' as 'month-year', May2020 as value from table0
        union all
        select Country as 'country', 'Jun2020' as 'month-year', Jun2020 as value from table0
        union all
        select Country as 'country', 'Jul2020' as 'month-year', Jul2020 as value from table0
        union all
        select Country as 'country', 'Aug2020' as 'month-year', Aug2020 as value from table0
        union all
        select Country as 'country', 'Sep2020' as 'month-year', Sep2020 as value from table0
        union all
        select Country as 'country', 'Oct2020' as 'month-year', Oct2020 as value from table0
    ) table1 order by country;

-- Output the query results into different format, csv, markdown, and html.

-- 1) CSV file
.mode csv
.headers on
.output query_results.csv
select * from table2;
.output stdout

-- 2) Markdown file
.mode markdown
.headers on
.output query_results.md
select * from table2;
.output stdout

-- 3) HTML file
.mode html
.headers on
.output query_results.html
select * from table2;
.output stdout
```

    * Finally, to get a nice output HTML results, use Python pandas to generate a new HTML table
```
# if you don't have Python pandas package, you can install it by:
pip3 install pandas
python3 query_results.py
```

## Contact
    * mohammed.farhan@kaust.edu.sa