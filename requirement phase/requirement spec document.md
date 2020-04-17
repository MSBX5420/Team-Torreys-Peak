Spec Document  
April, 17, 2020  
Team Torrey’s Peak  
Dylan Bernstein, Jennifer Dickson, Katie Greenfield, Madison Moye & Yongbo Shu  

## Glossary

- https://github.com/MSBX5420/Team-Torreys-Peak  
- https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26  

## Dataset

> “Has the news media been overreacting or under-reacting during the development of COVID-19? What are the media's main focuses? How is the news correlated to public reactions or policy changes? You might find many insights with more than 3,500 CBC news articles.”  

- This dataset retrieved from kaggle contains the authors, the title, the publish date, the description about the story, the main story and the url. Contains 3568 rows and 7 columns.  

## Functional Requirements

- Import dataset into AWS s3 bucket  
- Perform sentiment analysis including but not limited to “word count”, “Seriousness of COVID-19” and etc.  
- Visualize our observations with different graphs (treemap, barplot..)  

## Non-Functional Requirements

- Performance: Our project will be developed to be a parallel processing friendly and horizontally scaling program  

## Timeline

- April 12 - Spec Doc  
- April 13-17 - Cleaning dataset  
- April 20-24 - Building model  
- April 25 - Design, development & test
    - Use Agile development to have several iterations of design, development and test.  
    - Submit: Check in our design doc and code to Github repo.  
- April 28 - Deployment
    - Deploying our program to a larger cluster  
    - Presenting our work in class  
