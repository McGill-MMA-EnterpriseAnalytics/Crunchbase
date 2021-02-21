
# from google.colab import drive
# drive.mount("/content/drive")

# %cd 'drive/My Drive/bulk_export/'
import pickle
import pandas as pd
import numpy as np


def load_data(nrows=10000):
    """ Get 10000 data points, where we have already dummified the categories removing nas """
    pickle_res = pickle.load( open( "filtered_orgs.p", "rb" ) )
    orgs,dummycolumns = pickle_res['data'],pickle_res['dummies']
    #Filter data
    orgs = pd.read_csv("filtered_orgs.csv",nrows=nrows)
    orgs=orgs[orgs['category_groups_list'].isna()==False]
    orgs=orgs.reset_index(drop=True)
    return(orgs,dummycolumns)


def add_features(orgs,nrows=None):
    """ Add new features such as degree and event participation within the first year """
    if(nrows==None):
        founders=pd.read_csv("people.csv")
        degrees=pd.read_csv("degrees.csv")
        events=pd.read_csv("event_appearances.csv")
    else:
        founders=pd.read_csv("people.csv",nrows=nrows)
        degrees=pd.read_csv("degrees.csv",nrows=nrows)
        events=pd.read_csv("event_appearances.csv",nrows=nrows)

    ivyleague = ['Harvard','UCLA','Stanford','MIT','Yale','Princeton','Columbia','Brown','Dartmouth','Pennsylvania','Cornell']
    ivyleagers=degrees[degrees['institution_name'].str.contains("|".join(ivyleague))]
    ivyleagers=founders[founders['uuid'].isin(ivyleagers['person_uuid'])]
    ivyleagers=orgs[orgs['uuid'].isin(ivyleagers['featured_job_organization_uuid'])]
    orgs['ivy_league']= 0
    orgs['ivy_league']= [1 if i in ivyleagers.index else 0 for i in orgs.index]
    
    events["created_at"]=  pd.to_datetime(events["created_at"], format='%Y-%m-%d')
    events["created_at_year"] = pd.DatetimeIndex(events["created_at"]).year
    events["created_at_month"] = pd.DatetimeIndex(events["created_at"]).month
    events["created_at_day"] = pd.DatetimeIndex(events["created_at"]).day
    org_attended=orgs[orgs['uuid'].isin(events['participant_uuid'])]
    org_attended=pd.merge(org_attended,events[['participant_uuid','created_at_year']],left_on="uuid",right_on="participant_uuid")
    org_attended_year=org_attended[(org_attended['created_at_year']-org_attended['founded_on_year']>0)&(org_attended['created_at_year']-org_attended['founded_on_year']< 2)]
    
    participated=orgs[orgs['uuid'].isin(org_attended_year['participant_uuid'])]
    orgs['particapated_event_first_year']= 0 
    orgs['particapated_event_first_year']= [1 if i in participated.index else 0 for i in orgs.index]
    return(events,founders,degrees,orgs)