# Mission-to-Mars



## Results

Using Python code, a script to collect recent posts on the website https://redplanetscience.com which contained recent news about Mars was collected along with the most recent images from the website https://spaceimages-mars.com.  This data was combined with facts about Mars that was collected from the website https://galaxyfacts-mars.com along with images of the hemispheres of Mars that were made available on the website https://marshemispheres.com/.  This data was collected by scraping the webpages for the relevent links and text that was stored in a MongoDB database.  This data collected was stored in a Mongo database as the information, however relevent, was not structured and would be difficult to access using an SQL style database.  The data stored in the Mongo database accessed through a flask app that created a local server webpage that was populated by the data collected in the webscraping script and stored in the database.  The webpage also allow the user to rescrape the webpages to update the database and present the update data on the webpage. 

#

## Summary

From this project it is possible to see the power of using Python to automate webscrapping to collect relevent data for users.  This process can access data from a number of sources and store it in an unstructured database that can be accessed by user through a webpage.  This provides an effective and efficent manner of data collection, storage and accessibility that can provide data for users without them having to access a number of websites. 
