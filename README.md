# LMS Web Scraper
This scraping module will display all the new assignments that have been uploaded and all the recent forum posts on lms.

In the initial execution, the code collects a list of all assignments that are already present.
Therefore it scrapes and displays all the content in the upcoming events block.

In subsequent executions, it compares its list of assignments with the assignments already scraped.
If a new assignment has been added, it displays the new assignment name.

It also checks for forum posts and displays all names of people who have made recent forum posts.

### INSTRUCTIONS:

- Make sure your system has BeautifulSoup module and lxml parser installed.
- Open the file "final_scraper.py" in any text editor.
  Assign values to the variables "USERNAME", "PASSWORD", "display_file_path", and "output_file_path"
- Open crontab and insert the following line:
  0 * * * * python /path/to/final_scraper.py
(Here /path/to/ is to be replaced by the path to the repository where final_scraper.py is stored on your system.)
 

Please note that while the forum post checking feature has been implemented in this script, its accuracy has not been ascertained due to the lack of new forum posts on lms.
