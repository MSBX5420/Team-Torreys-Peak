<p align="left">
  <img width="250" height="100" src="https://github.com/MSBX5420/Team-Torreys-Peak/blob/master/design%20doc/images/Boulder%20one%20line%20copy.jpg">
</p>

# MSBX 5420 - Spring 2020
# Unstructured and Distributed Data Modeling and Analysis

Leeds School of Business, University of Colorado Boulder


## Project Description

COVID-19 has a strong impact on human lives. Our mission is to analyze how COVID-19 affects the newspaper industry.

### Prerequisites
- AWS cluster with pyspark (python 3) environment
- pandas & pyspark & numpy for data processing
- tmtoolkit & nltk for text mining and topic modeling
- matplotlib & wordcloud & seaborn for data visualization

### Installing
```console
pip install --user pandas pyspark tmtoolkit nltk numpy wordcloud matplotlib seaborn
```

### Deployment
- For local environment:
  - All files except [word_count_pyspark.ipynb](https://github.com/MSBX5420/Team-Torreys-Peak/blob/master/word%20count/word_count_pyspark.ipynb) can be executed on your local machine. Be sure to adjust the path for reading [news.csv](https://www.kaggle.com/ryanxjhan/cbc-news-coronavirus-articles-march-26).
- For cluster platform:
    - All files can be executed on any cloud service. We will give an example on running files on AWS cluster.
    - Tuning path for reading files is a pain, we totally understand that. So if you want to run our code on AWS, we strongly recommend save news.csv at the same folder as all other .ipynb files. In that way, all you need to do is change path to :
    <p align="center">
      <img width="500" height="100" src="https://github.com/MSBX5420/Team-Torreys-Peak/blob/master/design%20doc/images/Jietu20200428-234300%402x.jpg">
    </p>

    - You can use aws cluster jupyter notebook interface to interact with our code;
    - You can also use spark-submit to submit our work to your personal cluster and check results with provided hadoop link
    ```console
    spark-submit --master yarn --deploy-mode cluster --num-executors 2 --executor-memory 1G --executor-cores 1 --driver-memory 1G /aws_cluster_hadoop_path/files_you_want_to_execute.py(ipynb)
    ```

### Documents

- [Requirement Spec Document](https://github.com/MSBX5420/Team-Torreys-Peak/blob/master/requirement%20phase/requirement%20spec%20document.md)
- [Design Document](https://github.com/MSBX5420/Team-Torreys-Peak/blob/master/design%20doc/design%20doc.md)
- [Presentation Slide](https://drive.google.com/file/d/1Qlrb08yvZkpX_sjBkwRaUdeK4vhppyEM/view?usp=sharing)

## Contact Information

**Author:**  
- Yongbo Shu (Yongbo.Shu@colorado.edu)
- Katie Greenfield (Kathryn.Greenfield@colorado.edu)
- Madison Moye (Madison.Moye@colorado.edu)
- Dylan Bernstein (Dylan.Bernstein@colorado.edu)
- Jennifer Dickson (Jennifer.Dickson@colorado.edu)  

**Instructor:**
- Peigang Zhang (Peigang.Zhang@colorado.edu)
