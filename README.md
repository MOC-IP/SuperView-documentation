# SuperView
This project will attempt to combine population statistics with data about
businesses to derive meaningful relations such as why a business succeeds, who
are its competitors and where can it expand. The main actors will be the business
owners.

## Members
Coordonator: Mihaela Elena Breaban   pmihaela@info.uaic.ro 
- Anda Buinoschi   anda.buinoschi@outlook.com
- Vasile Groza   vasilegroza3@gmail.com
- Andrei-Constantin Iacob   andreiacob37@gmail.com
- Dorin Andrei Miron   adorin.miron@gmail.com

## TODOs

### Week 1
Requirements
1. Creating team
2. Study themes from previous years
3. Find theme
4. Find coordinator

### Week 2
Requirements: [State of the art](https://github.com/AndreiIacob/SuperView/tree/master/documents/state_of_the_art.md)

- [x] Andrei - search about teams who win "yelp challenge"
- [x] Anda   - seach about other studies on yelp dataset
- [x] Dorin  - search about another datasets
- [x] Vasile - search about available tools/apis that we can use

### Week3
1. Configure github page
2. Configure board with issues and assignments
3. Make requirements analysis
4. Create UML diagrams

- Anda 	
    - [x] Create final file with state of the art.
	- [ ] Make 2 diagrams:
		+ [x] "collaborationdiagram"
		+ ... (package diagram) ##!! not finished !!##

- Andrei  
    - [x] configure github page
	- [x] configure board with issues and assignments
	- [x] Make 4 diagrams:  
		+ [x] "Request Competitors" (use case)
		+ [x] "Request Own Business" (use case)
		+ [x] "Generate Sugesstions" (use case)
		+ [x] "Classifier Class Diagram"

- Vasile  
    - [x] create requirements analysis
	- [x] make 2 diagrams:
		+ [x] "DeployDiagram0"
		+ [x] "DeploymentDiagram1"

- Dorin 	
    - [x] create requirements analysis
	- [x] make 2 diagrams:
		+ [x] "ClassDiagram"
		+ [x] "SequenceDiagram"

### Week4
- [X] Anda 	
    - research about LDA

- Andrei
    - give ideas about algorithms and methods that we nedd to use.
 	- generate statistics (can be found in /documents/statistics)

- Vasile
    - research about ways to join dataset from tripAdvisor and Yelp
	- create an API that can return location of business.

- Dorin
	- analyze dataset from tripAdvisor
	- create an approach for generate (for group words in) strengths and weaknesses (can be found in /documents/topics_extraction) 

<!-- ### Week 5 -->
<!-- Anda 	- se uita peste abordarea celor de la netflix
Andrei 	- incearca sa extraga eticheteze cu label-uri valide acele grupuri de cuvinte create.
Vasile 	- se uita peste sentimentAnalyzez
Dorin 	- Fac join intre acele date si ma folosesc de api-ul lui vasile -->

### Week 5
- Anda
	- research about The Netflix Prize and search for an approach that we can use
- Andrei
	- try to label with valid labels those groups of created words (in other words, to extract significant digrams and trigrams)
- Vasile
	- research about Sentiment Analysis
- Dorin
	- join the data and use Vasile's api

### Week 6
- Dorin & Vasile
	- created an instance on EC2 for MongoDB

### Week 7
- populate the database

### Week 8
- All of us
	- Aspect Oriented Programming (AOP) and Test Driven Development (TDD) for some functions used

### Week 9
- Andrei 
	- evaluation of the sentiment classifiers on the reviews' scores
	- clustering based on arrays of words (word2vec and GloVe)
	- Topic Coherence
	- Interface through Flash and PyMongo
- Vasile & Dorin
	- user interface (ui), backend, processor components (modules)
- Anda
	- confussion matrix

### Week 10
- Andrei
	- filtered the reviews that are not in English
- Anda
	- comparison between Clustering and Topic Modelling
- Dorin & Vasile
	- database for Python

### Week 11
- Andrei
	- evaluation of the sentiment classifiers on bias extracted from the reviews
	- wordcloud on the clusters