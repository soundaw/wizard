
import pandas as pd



data_frame1 = pd.read_csv("SYS_ALL_CUSTOMER_ONLY_RSYS_3.csv",usecols=[0,3], header=0,low_memory=False)
data_frame2 = pd.read_csv("SYS_ALL_CUSTOMER_WITHOUT_RSYS_3.csv",usecols=[3], header=0,low_memory=False)
df2 = data_frame1[~data_frame1['ExternalUUID'].isin(list(data_frame2['ExternalUUID']))]
df2.to_csv('RSYS_DF_DUPLICATE_3.zip', index=False)

# "MasterCustomer_ID","SourceMasterCustomerID","Email","Phone","MobilePhone"
# Customer_ID,ExternalUUID


#df2 = pd.read_csv("RSYS_DF_DUPLICATE_3.csv",usecols=[0,1], header=0,low_memory=False)
#df1 = pd.read_csv("RSYS_MC_UNIQUE_3.csv",usecols=[0,1], header=0,low_memory=False)

#df3 = df1[~df1['MasterCustomer_ID'].isin(list(df2['Customer_ID']))]
#df3.to_csv('RSYS_RESULT_A_2.zip', index=False)

#df4 = df2[~df2['Customer_ID'].isin(list(df1['MasterCustomer_ID']))]
#df4.to_csv('RSYS_RESULT_B_2.zip', index=False)