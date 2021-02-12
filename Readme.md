# Data:
The data contains startups from crunchbase. The data is greatly unbalanced. Considering most startups fail, this is not represented in the data. Startups have information such as amount raised, whether or not they are still operating, acquired as well as descriptions, categories.

The folder also contains employee and investor data. 


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

We can also use Casual ML to find causal relationships between success.

TPOT can also be used to create a baseline model.


Startup Name, Acquired by Large Corp, Acquired, Cybersecurity, Unicorn (raised a lot) 
