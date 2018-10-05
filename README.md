# logs_analysis
Build an internal reporting tool [logs_analysis.py](https://github.com/HanaShamatah/logs_analysis/blob/master/logs_analysis.py) that will use information from PostgreSQL database to discover what kind of articles the site's readers like.
## Project Steps
 - Define multiple functions each for a specific statistics of the report using SQL queries to analyze the data:
   - Popular_articles: list the most popular three articles (with highest views).
   - Popular_authors: Sort authors according to their total articles views.
   - Requsts_error: List days with more than 1% requests error “404 NOT FOUND”.
 - Use the DB-API database library to query the PostgreSQL database.
 - Print the results in a good reporting format.
 - Write the results in a plain text file as in [results.txt](https://github.com/HanaShamatah/logs_analysis/blob/master/results.txt) results sample.
  
## Get Started
  - Install [Linux-based virtual machine (VM)](https://s3.amazonaws.com/video.udacity-data.com/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) that has the PostgreSQL database and support software needed for this project.
  - cd the terminal to vagrant directory, the bring the virtual machine  online (with vagrant up) andtThen log into it with vagrant ssh. Then, cd to /vagrant sub-directory to access the shared files in VM.
  - Download the date from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it, put it into the vagrant directory.
  - Use _psql -d news -f newsdata.sql_ in the terminal (git bash) to connect to the installed database server and execute the SQL commands in the downloaded file.
  - Fork this repository to create your own copy in GitHub. Then clone your repository to the vagrant directort to work on this project locally on your computer.

## How to Run
  - Run **python logs_analysis.py** in the terminal to get the results printed and saved in [results.txt](https://github.com/HanaShamatah/logs_analysis/blob/master/results.txt).

 ## Notes
- The codes are organized according to [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- The views used to run the code will be directly created or replaced (if they already exist) when [logs_analysis.py](https://github.com/HanaShamatah/logs_analysis/blob/master/logs_analysis.py) python code is running.

## License
The content of this repository is licensed under an [MIT](https://choosealicense.com/licenses/mit/).
