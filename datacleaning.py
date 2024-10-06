import numpy as np
import pandas as pd
df= pd.read_csv("C:/Users/DELL/OneDrive/Desktop/SQL/smartphones - smartphones.csv")
df
pd.set_option('display.max_columns', None)
df.columns
#Data Assessing
#Quality Issues
df.sample(7)
# model: formatting issues (should be brand+ model name+generation)
#price : unnessary rupee unit
# rating : nan values
df['rating'].describe()
#sim : messy column(might convert to single or dual sim)
# processor: unnecessary info
# battery:unnecessary info(structure problem) incorrect values
# data shifting 
df.info()
# 19 missing values in camera
# datatype of price and rating is incorrect
df.describe()
df.duplicated().sum()
# data cleaning 
#price 
df1=df.copy()
df1
df1['price']=df1['price'].str.replace('₹','').str.replace(',','').astype('int')
df1
# from manual observation realised there are no of rows that have problems(try to specify it)
# we did union and intersection of rows 
# there are phones in data which are not smart
# we can filter upon the price <=3400 to filter data in someway
df1= df1.reset_index()
df1['index']= df1['index']+2
df1
processor_rows = set((642,647,649,659,667,701,750,759,819,859,883,884,919,927,929,932,1002))
ram_rows = set((441,485,534,553,584,610,613,642,647,649,659,667,701,750,759,819,859,884,919,927,929,932,990,1002))
battery_rows = set((113,151,309,365,378,441,450,553,584,610,613,630,642,647,649,659,667,701,750,756,759,764,819,855,859,884,915,916,927,929,932,990,1002))
display_rows = set((378,441,450,553,584,610,613,630,642,647,649,659,667,701,750,759,764,819,859,884,915,916,927,929,932,990,1002))
camera_rows = set((100,113,151,157,161,238,273,308,309,323,324,365,367,378,394,441,450,484,506,534,553,571,572,575,584,610,613,615,630,642,647,649,659,667,684,687,705,711,723,728,750,756,759,764,792,819,846,854,855,858,883,884,896,915,916,927,929,932,945,956,990,995,1002,1016 ))
# union of problematic rows
df1[df1['index'].isin(processor_rows| ram_rows | battery_rows|display_rows|camera_rows)]
# intersection of problematic rows
df1[df1['index'].isin(processor_rows & ram_rows&battery_rows&display_rows&camera_rows)]
# issue : data shifting and data mixing 
df1[df1['index'].isin(processor_rows & ram_rows&battery_rows&display_rows&camera_rows)]['price'].mean()
df1=df1[df1['price']>= 3400]
df1
# 3 rows left only
df1[df1['index'].isin(processor_rows & ram_rows&battery_rows&display_rows&camera_rows)]

# processor 
# 4 rows left 
df1[df1['index'].isin(processor_rows)]
df1
# Nokia 5710 XpressAudio , Nokia 3310 4G,Nokia 2760 Flip, LG Folder 2 not a smartphone, we need to remove
df1.drop([645,857,882,925],inplace=True)
# ram rows(3 rows)
df1[df1['index'].isin(ram_rows)]
# Nokia 8210 4G is a feature phone
df1.drop([582],inplace= True)

df1[df1['index'].isin(ram_rows)]
df1[df1['index'].isin(battery_rows)]

df1.drop([754,376],inplace=True)
temp_df = df1[df1['index'].isin(battery_rows)]
# bettery has display info and data shifted to right 
# using slicing and shift
x= temp_df.iloc[:,7:].shift(1,axis=1).values
x
x_index=temp_df.index
df1.loc[temp_df.index,temp_df.columns[7:]]=x

df1[df1['index'].isin(battery_rows)]
# display rows
df1[df1['index'].isin(display_rows)]
# camera rows
df1[df1['index'].isin(camera_rows)]
# problem : feature phone & some rows have shifted not all
df1.drop([155,271],inplace = True)
temp_df=df1[df1['index'].isin(camera_rows)]
# 
temp_df
#  (values exchange with card col)
temp_df=temp_df[~temp_df['camera'].str.contains('MP')]

df1.loc[temp_df.index,'camera']= temp_df['card'].values

df1[df1['index'].isin(camera_rows)]
# card
df1['card'].value_counts
temp_df= df1[df1['card'].str.contains('MP')]
df1.loc[temp_df.index,'card']='Memory Card Not Supported'


df1[df1['card'].str.contains('MP')]

# os and card

temp_df=df1[~df1['card'].str.contains('Memory Card')]
df1['card'].value_counts()
df1.loc[temp_df.index,'os']=temp_df['card'].values

df1.loc[temp_df.index,'card']='Memory Card Supported'

df1['card'].value_counts()

df1['os'].value_counts()

temp_df= df1[df1['os'].str.contains('Memory Card Not Supported')]

df1.loc[temp_df.index,'os']=np.nan

temp_df= df1[df1['os']=='Bluetooth']

df1.loc[temp_df.index,'os']=np.nan

df1['os'].value_counts()

temp_df= df1[df1['os']=='Memory Card Supported, upto 256 GB']

df1.loc[temp_df.index,'card']=temp_df['os'].values
df1['card'].value_counts()
df1['os'].value_counts()
df1['card']
temp_df= df1[df1['os']=='Memory Card Supported, upto 128 GB']


df1.loc[temp_df.index,'card']= 'Memory Card Supported, upto 128 GB'



temp_df= df1[df1['os']=='Memory Card Supported, upto 256 GB']
temp_df
df1.loc[temp_df.index,'os']=np.nan

temp_df= df1[df1['os']=='Memory Card Supported, upto 128 GB']
df1.loc[temp_df.index,'os']=np.nan

df1['display'].value_counts()
##Validity issue solved


## tidiness issue: every columnn has multiple issues
#'brand col'
brand_names= df1['model'].str.split(' ').str.get(0)
df1.insert(1,'Brand',brand_names)
df1.head(5)
df1['Brand']= df1['Brand'].str.lower()
has5G= df1['sim'].str.contains('5G')
NFC= df1['sim'].str.contains('NFC')
IR_Blaster= df1['sim'].str.contains('IR Blaster')
df1.insert(6,'5G',has5G)
df1.insert(7,'NFC',NFC)
df1.insert(8,'IR Blaster',IR_Blaster)


processor_name= df1['processor'].str.split(',').str.get(0)

df1.insert(10,'processor_name',processor_name)

num_cores=df1['processor'].str.split(',').str.get(1)
processor_speed= df1['processor'].str.split(',').str.get(2)
df1.insert(11,'num_cores',num_cores)
df1.insert(12,'processor_speed',processor_speed)

df1['processor_name'].str.strip()

temp_df= df1[df1['processor_name'].str.contains('Core')][['processor_name','num_cores','processor_speed']].shift(1,axis=1)
df1.loc[temp_df.index,['processor_name','num_cores','processor_speed']]=temp_df.values

df1['processor_name'].value_counts()

df1[df1['processor_name']=='(28 nm)']
df1.loc[856,['processor_name']]= 'Mediatek MT6739'


processor_brand =df1['processor_name'].str.split(' ').str.get(0).str.lower()

df1.insert(11,'processor_brand',processor_brand)

df1['num_cores']=df1['num_cores'].str.strip()


df1['num_cores'].value_counts()

df1['num_cores']=df1['num_cores'].str.replace('Octa Core Processor','Octa Core ').str.replace('Hexa Core Processor','Hexa Core').str.replace("Octa Core ",'Octa Core').value_counts()
df1['processor_speed']= df1['processor_speed'].str.strip().str.split(' ').str.get(0).str.replace('\u2009',' ').str.split(' ').str.get(0).astype('float')

df1.head(5)

df1['ram']
ram_capacity= df1['ram'].str.strip().str.split(',').str.get(0).str.findall(r'\b(\d+)\b').str.get(0)
# using regex
df1.insert(16,'ram_capacity',ram_capacity)


internal_memory=df1['ram'].str.strip().str.split(',').str.get(1).str.findall(r'\b(\d+)\b').str.get(0)
df1.insert(17,'internal_memory',internal_memory)
df1['ram_capacity']=df1['ram_capacity'].astype(float)
df1[df1['ram_capacity']>18]
df1.loc[[439,762],['ram_capacity','internal_memory']]=[[4,'64'],[4,'64']]

df1.loc[[439,762]]

df1.loc[[483],['ram_capacity','internal_memory']]=[12,'512']
df1.drop([486,627],inplace=True)
df1['internal_memory']= df1['internal_memory'].astype(float)


temp_df=df1[df1['internal_memory'] == 1]
df1.loc[temp_df.index,'internal_memory']=1024
df1['internal_memory'].value_counts()

battery_capacity= df1['battery'].str.strip().str.split('with').str.get(0).str.strip().str.findall(r'\b(\d+)\b').str.get(0).astype(float)
df1.insert(16,'battery_capacity',battery_capacity)
df1['battery_capacity'].value_counts()
df1['battery_capacity'].value_counts()

fast_charging= df1['battery'].str.strip().str.split('with').str.get(1).str.strip().str.findall(r'\d{2,3}').str.get(0)
df1.insert(17,'fast_charging',fast_charging)
def fast_charging_extractor(item):

  if type(item) == list:
    if len(item) == 1:
      return item[0]
    else:
      return 0
  else:
    return -1
df1['fast_charging'].value_counts()
df1.head(5)

screen_size= df1['display'].str.strip().str.split(',').str.get(0).str.strip().str.split(' ').str.get(0).astype(float)

df1.insert(21,'screen_size',screen_size)

resolution= df1['display'].str.strip().str.split(',').str.get(1).str.strip().str.split('px').str.get(0)

df1.insert(22,'resolution',resolution)

refresh_rate=df1['display'].str.strip().str.split(',').str.get(2).str.strip().str.findall(r'\d{2,3}').str.get(0).apply(lambda x: 60 if pd.isna(x) else x).astype(int)
df1.insert(23,'refresh_rate',refresh_rate)
df1['camera'].str.strip().str.split('&').str.get(0)
def camera_extractor(text):

  if 'Quad' in text:
    return '4'
  elif 'Triple' in text:
    return '3'
  elif 'Dual' in text:
    return '2'
  elif 'Missing' in text:
    return 'Missing'
  else:
    return '1'

num_rear_cameras= df1['camera'].str.strip().str.split('&').str.get(0).apply(camera_extractor)
df1.insert(25,'num_rear_cameras',num_rear_cameras)
df1.head()


num_front_cameras = df1['camera'].str.strip().str.split('&').str.get(1).str.strip().fillna('Missing').apply(camera_extractor)
df1.insert(26,'num_front_cameras',num_front_cameras)
df1[df1['num_front_cameras'] == 'Missing']
df1.loc[69,'camera'] == '50 MP'
temp_df = df1[df1['camera'] == 'Foldable Display, Dual Display']
df1.loc[temp_df.index, 'camera'] = '50 MP'
df1['primary_camera_rear'] = df1['camera'].str.split(' ').str.get(0).str.replace('\u2009',' ').str.split(' ').str.get(0)
df1['primary_camera_front'] = df1['camera'].str.split('&').str.get(1).str.strip().str.split(' ').str.get(0).str.replace('\u2009',' ').str.split(' ').str.get(0)


df1[df1['card'] == 'Memory Card (Hybrid)']
temp_df





























