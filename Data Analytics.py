import pandas as pd
df = pd.read_csv('loans.csv')


#df['Gender'].replace({'Female':'F','Male':'M','0':'F','1':'M','H':'F','N':'M'},inplace=True) 
#df=df[df.Gender != 'D']
df['Years at address'].replace({560:56,410:41,300:30,250:25},inplace=True)
df['Income'].replace({180000:18000,220000:22000},inplace=True)
df=df.set_index('Customer ID')
df['CCJs'].replace({100:1,10:1},inplace=True)

df.to_csv('New_loans.csv')

