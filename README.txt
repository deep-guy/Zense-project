This scraping module will display all the new assignments that have been uploaded and all the recent forum posts on lms.

In the initial execution, the code collects a list of all assignments that are already present.
Therefore it scrapes and displays all the content in the upcoming events block.

In subsequent executions, it compares its list of assignments with the assignments already scraped.
If a new assignment has been added, it displays the new assignment name.

It also checks for forum posts and displays all names of people who have made recent forum posts.

INSTRUCTIONS:

1)Make sure your system has BeautifulSoup module and lxml parser installed.
2)Open the file "final_scraper.py" in any text editor.
  Assign values to the variables "USERNAME", "PASSWORD", "display_file_path", and "output_file_path"
3)Open crontab and insert the following line:
    
