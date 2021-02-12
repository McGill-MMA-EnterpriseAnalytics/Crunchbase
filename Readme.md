# Data:
The data contains startups from crunchbase. The data is greatly unbalanced. Considering most startups fail, this is not represented in the data. Startups have information such as amount raised, whether or not they are still operating, acquired as well as descriptions, categories.

The folder also contains employee and investor data. 

The objective is to see if we can determine which startups will fail, which will be acquired/succeed and in what area of expertise they are in. These areas of expertise usually change over time. Ie. recently the verticals "Regtech" and "Digital ID" are becoming more and more popular. Given that there is no existing labels for these startups we can use semi-supervised algoirthms to label them ourselves. The purpose of crunchbase is for investors to get a glimpse at the most up to date startup data. Investors soemtimes have different definitions on trends, therefore this may serve useful in bboth predicting a companies relevance to their vertical as well as potential success. 

# Preprocessing:
Startups need to be companies.
 In addition we will need to find the acquired companies for companies with status “acquired” for multi-label classification.
In addition we should see if removing the date has any effect. 
Also we need to ensure that company size must not be included as this may indicate that they will be acquired. 
We must find a test dataset that is small companies that just got acquired. Red labels are the target labels.
We must also create features such as potential competition stats.
Look at employee data stats/diversity.

# Prediction: 

We can do labelling on our own at first for the super verticals (ie. cybersecurity) -> we need to 
identify these from the groups_list we can do clustered semi-supervised ml for this.

We can also use Casual ML to find causal relationships between failure.

TPOT can also be used to create a baseline model.


What we want to perdict is: Acquired by Large Corp, Acquired, Super Vertical (ie. Cybersecurity), Unicorn (raised a lot) 
