#imported packages
import os
import json
import pandas as pd
import psycopg2 
import git

import json
import streamlit as st
import pandas as pd
import requests
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
st.set_page_config(layout= "wide")

#aggre_transaction
path1="C:/Users/ELCOT/Desktop/phonepe/pulse/data/aggregated/transaction/country/india/state/"
agg_tran_list= os.listdir(path1)

columns1={"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for state in agg_tran_list:
    cur_states=path1+state+"/"
    agg_year_list=os.listdir(cur_states)
   
    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            A=json.load(data)


            for i in A["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)
                columns1["States"].append(state)
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))
                
aggre_transaction=pd.DataFrame(columns1)


#aggre_user
path2="C:/Users/ELCOT/Desktop/phonepe/pulse/data/aggregated/user/country/india/state/"
agg_user_list= os.listdir(path2)

columns2={"States":[],"Years":[],"Quarter":[],"Brands":[],"Transaction_count":[],"Percentage":[]}

for state in agg_user_list:
    cur_states=path2+state+"/"
    agg_year_list=os.listdir(cur_states)
   
    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            B=json.load(data)

            try:
                for i in B["data"]["usersByDevice"]:
                    brand=i["brand"]
                    count=i["count"]
                    percentage=i["percentage"]
                    columns2["Brands"].append(brand)
                    columns2["Transaction_count"].append(count)
                    columns2["Percentage"].append(percentage)
                    columns2["States"].append(state)
                    columns2["Years"].append(year)
                    columns2["Quarter"].append(int(file.strip(".json")))

            except:
                pass
            
aggre_user=pd.DataFrame(columns2)
            

#map_transaction
path3="C:/Users/ELCOT/Desktop/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_tran_list= os.listdir(path3)

columns3={"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_tran_list:
    cur_states=path3+state+"/"
    agg_year_list=os.listdir(cur_states)
   
    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            C=json.load(data)
           
            for i in C["data"]["hoverDataList"]:
                    name=i["name"]
                    count=i["metric"][0]["count"]
                    amount=i["metric"][0]["amount"]
                    columns3["Districts"].append(name)
                    columns3["Transaction_count"].append(count)
                    columns3["Transaction_amount"].append(amount)
                    columns3["States"].append(state)
                    columns3["Years"].append(year)
                    columns3["Quarter"].append(int(file.strip(".json")))
                    
map_tran = pd.DataFrame(columns3)
                    

#map_user

path4="C:/Users/ELCOT/Desktop/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list= os.listdir(path4)

columns4={"States":[],"Years":[],"Quarter":[],"Districts":[],"RegisteredUsers":[],"AppOpens":[]}

for state in map_user_list:
    cur_states=path4+state+"/"
    agg_year_list=os.listdir(cur_states)
   
    for year in agg_year_list:
        cur_year=cur_states+year+"/"
        agg_file_list=os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file=cur_year+file
            data=open(cur_file,"r")

            D=json.load(data)

            for i in D["data"]["hoverData"].items():
                district=i[0]
                registeredUsers=i[1]["registeredUsers"]
                appOpens=i[1]["appOpens"]
                columns4["Districts"].append( district)
                columns4["RegisteredUsers"].append( registeredUsers)
                columns4["AppOpens"].append(appOpens)
                columns4["States"].append(state)
                columns4["Years"].append(year)
                columns4["Quarter"].append(int(file.strip(".json")))
                
map_user=pd.DataFrame(columns4)


#top_transaction

path5="C:/Users/ELCOT/Desktop/phonepe/pulse/data/top/transaction/country/india/state/"
top_tran_list = os.listdir(path5)

columns5 ={"States": [], "Years": [], "Quarter": [], "Pincodes": [], "Transaction_count": [], "Transaction_amount": []}


for state in top_tran_list:
    cur_states = path5+state+"/"
    top_year_list = os.listdir(cur_states)
    
    for year in top_year_list:
        cur_years = cur_states+year+"/"
        top_file_list = os.listdir(cur_years)
    
        for file in top_file_list:
            cur_files = cur_years+file
            data = open(cur_files,"r")

            E = json.load(data)
    
            for i in E["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                columns5["Pincodes"].append(entityName)
                columns5["Transaction_count"].append(count)
                columns5["Transaction_amount"].append(amount)
                columns5["States"].append(state)
                columns5["Years"].append(year)
                columns5["Quarter"].append(int(file.strip(".json")))
                
top_transaction=pd.DataFrame(columns5)


#top_user

path6="C:/Users/ELCOT/Desktop/phonepe/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(path6)

columns6={"States": [], "Years": [], "Quarter": [], "Pincodes": [], "RegisteredUser": []}

for state in top_user_list:
    cur_states=path6+state+"/"
    top_year_list=os.listdir(cur_states)

    for year in top_year_list:
        cur_years=cur_states+year+"/"
        top_file_list=os.listdir(cur_years)

        for file in top_file_list:
            cur_files=cur_years+file
            data=open(cur_files,"r")

            F=json.load(data)

            for i in F["data"]["pincodes"]:
                name = i["name"]
                registeredusers = i["registeredUsers"]
                columns6["Pincodes"].append(name)
                columns6["RegisteredUser"].append(registeredusers)
                columns6["States"].append(state)
                columns6["Years"].append(year)
                columns6["Quarter"].append(int(file.strip(".json")))
                
top_user = pd.DataFrame(columns6)

#Table_creation
#pgsql_connection
mydb=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="atchayaA@10_02",
                      database="phonepe_data",
                      port="5432")
cursor=mydb.cursor()

#aggregated transaction table
create_query1 = '''CREATE TABLE if not exists aggregated_transaction (States varchar(50),
                                                                      Years int,
                                                                      Quarter int,
                                                                      Transaction_type varchar(50),
                                                                      Transaction_count bigint,
                                                                      Transaction_amount bigint
                                                                      )'''
cursor.execute(create_query1)
mydb.commit()

for index,row in aggre_transaction.iterrows():
    insert_query1 = '''INSERT INTO aggregated_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                           values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Transaction_type"],
              row["Transaction_count"],
              row["Transaction_amount"]
              )
    cursor.execute(insert_query1,values)
    mydb.commit()

#aggregated user table
create_query2 = '''CREATE TABLE if not exists aggregated_user (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                Brands varchar(50),
                                                                Transaction_count bigint,
                                                                Percentage float)'''
cursor.execute(create_query2)
mydb.commit()

for index,row in aggre_user.iterrows():
    insert_query2 = '''INSERT INTO aggregated_user (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Brands"],
              row["Transaction_count"],
              row["Percentage"])
    cursor.execute(insert_query2,values)
    mydb.commit()

# Create DataFrame for map_transaction_table
#converting map_tran to csv file
map_transaction = pd.DataFrame(data) 

#map_transaction_table
# Assuming a DataFrame named map_tran
map_tran.to_csv('map_tran.csv')

#SQL table creation and insertion code
create_query3 = '''CREATE TABLE if not exists map_transaction (
                    States varchar(50),
                    Years int,
                    Quarter int,
                    districts varchar(50),
                    Transaction_count bigint,
                    Transaction_amount float
                )'''
mydb.rollback()

cursor.execute(create_query3)
mydb.commit()

for index, row in map_tran.iterrows():
    insert_query3 = '''
        INSERT INTO map_transaction (States, Years, Quarter, districts, Transaction_count, Transaction_amount)
        VALUES (%s, %s, %s, %s, %s, %s)'''

    values = (
        row['States'],
        row['Years'],
        row['Quarter'],
        row['Districts'], 
        row['Transaction_count'],
        row['Transaction_amount'])
      
    cursor.execute(insert_query3, values)
    mydb.commit()
# Print the DataFrame
print(map_tran)

#map_user_table
create_query4 = '''CREATE TABLE if not exists map_users (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(50),
                                                        Registeredusers int,
                                                        AppOpens bigint)'''
cursor.execute(create_query4)
mydb.commit()

for index,row in map_user.iterrows():
    insert_query4 = '''INSERT INTO map_users (States, Years, Quarter, Districts, RegisteredUsers, AppOpens)
                       VALUES (%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Districts"],
              row["RegisteredUsers"],
              row["AppOpens"])
    cursor.execute(insert_query4,values)
    mydb.commit()
    
#top_transaction_table
create_query5 = '''CREATE TABLE if not exists top_transaction (States varchar(50),
                                                                Years int,
                                                                Quarter int,
                                                                pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
cursor.execute(create_query5)
mydb.commit()

for index,row in top_transaction.iterrows():
    insert_query5 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
    cursor.execute(insert_query5,values)
    mydb.commit()
    
#top_user_table
create_query6 = '''CREATE TABLE if not exists top_user (States varchar(50),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                        )'''
cursor.execute(create_query6)
mydb.commit()

for index,row in top_user.iterrows():
    insert_query6 = '''INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser)
                                            values(%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["RegisteredUser"])
    cursor.execute(insert_query6,values)
    mydb.commit()
    
#CREATE DATAFRAMES FROM SQL
#sql connection
mydb = psycopg2.connect(host = "localhost",
                        user = "postgres",
                        password = "atchayaA@10_02",
                        database = "phonepe_data",
                        port = "5432"
                        )
cursor = mydb.cursor()

#Aggregated_transsaction
cursor.execute("select * from aggregated_transaction;")
mydb.commit()
table1 = cursor.fetchall()
Aggre_trans = pd.DataFrame(table1,columns = ("States", "Years", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"))

#Aggregated_user
cursor.execute("select * from aggregated_user")
mydb.commit()
table2 = cursor.fetchall()
Aggre_user = pd.DataFrame(table2,columns = ("States", "Years", "Quarter", "Brands", "Transaction_count", "Percentage"))

#Map_transaction
cursor.execute("select * from map_transaction")
mydb.commit()
table3 = cursor.fetchall()
Map_trans = pd.DataFrame(table3,columns = ("States", "Years", "Quarter", "Districts", "Transaction_count", "Transaction_amount"))

#Map_user
# Rollback the transaction
mydb.rollback()
cursor.execute("SELECT * FROM map_users")
table4 = cursor.fetchall()
# Continue with the rest of my code
Map_user = pd.DataFrame(table4, columns=("States", "Years", "Quarter", "Districts", "RegiseredUser", "AppOpens"))
 
#Top_transaction
cursor.execute("select * from top_transaction")
mydb.commit()
table5 = cursor.fetchall()
Top_trans = pd.DataFrame(table5,columns = ("States", "Years", "Quarter", "Pincodes", "Transaction_count", "Transaction_amount"))  

#Top_user
cursor.execute("select * from top_user")
mydb.commit()
table6 = cursor.fetchall()
Top_user = pd.DataFrame(table6, columns = ("States", "Years", "Quarter", "Pincodes", "RegisteredUser"))

def animate_all_amount():
    # Define the URL for the geojson data
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

    # Send a GET request to the URL to fetch the geojson data
    response = requests.get(url)

    # Parse the content of the response as JSON
    data1 = json.loads(response.content)
    
    # Extract state names from the geojson data
    state_names_tra = [feature["properties"]["ST_NM"] for feature in data1["features"]]

    # Sort the state names
    state_names_tra.sort()

    # (Optional) Print or return the sorted state names
    print("Sorted State Names:", state_names_tra)

    # Return the state_names_tra list
    return data1, state_names_tra

# Call the function to execute the code and get the state_names_tra list
data1, state_names_tra = animate_all_amount()

# Create DataFrame using the returned list
df_state_names_tra = pd.DataFrame({"States": state_names_tra})
# Initialize an empty list to store data frames
frames = []
#Outer Loop (Years)
for year in Map_user["Years"].unique():
#Inner Loop (Quarters)
        for quarter in Aggre_trans["Quarter"].unique():
#Data Filtering
            at1 = Aggre_trans[(Aggre_trans["Years"]==year)&(Aggre_trans["Quarter"]==quarter)]
#Column Selection
            atf1 = at1[["States","Transaction_amount"]]
#Sorting
            atf1 = atf1.sort_values(by="States")
#Adding Year and Quarter Columns
            atf1["Years"]=year
            atf1["Quarter"]=quarter
#Appending to List
            frames.append(atf1)
            
# Combine DataFrames in the frames list into a single DataFrame
merged_df = pd.concat(frames)  # In this case, it concatenates the DataFrames in the frames list.
#This is a function from Plotly Express used to create a choropleth map.
fig_tra = px.choropleth(merged_df, geojson= data1, locations= "States", featureidkey= "properties.ST_NM", color= "Transaction_amount",
                        color_continuous_scale= "Sunsetdark", range_color= (0,4000000000), hover_name= "States", title = "TRANSACTION AMOUNT",
                        animation_frame="Years", animation_group="Quarter")
#Plotly Figure Updates
fig_tra.update_geos(fitbounds= "locations", visible= False)
fig_tra.update_layout(width= 600, height= 700)
fig_tra.update_layout(title_font={"size":25})
st.plotly_chart(fig_tra)  
  

def payment_count():
    # Select relevant columns "Transaction_type" and "Transaction_count" from Aggre_trans
    attype= Aggre_trans[["Transaction_type", "Transaction_count"]]
     # Group the data by "Transaction_type" and calculate the sum of "Transaction_count" for each group
    att1= attype.groupby("Transaction_type")["Transaction_count"].sum()
     # Convert the grouped data to a DataFrame and reset the index
    df_att1= pd.DataFrame(att1).reset_index()
    # Create a bar chart using Plotly Express
    fig_pc= px.bar(df_att1,x= "Transaction_type",y= "Transaction_count",title= "TRANSACTION TYPE and TRANSACTION COUNT",
                color_discrete_sequence=px.colors.sequential.Redor_r)
    # Update the layout of the chart (setting width and height)
    fig_pc.update_layout(width=600, height= 500)
    return st.plotly_chart(fig_pc)

def animate_all_count():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    #Fetch GeoJSON Data
    response= requests.get(url)
    data1= json.loads(response.content)
    #Extract State Names
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()
    ## Create DataFrame using the sorted state names
    df_state_names_tra= pd.DataFrame({"States":state_names_tra})
    
frames= []

# Iterate through unique years in the "Years" column of Aggre_trans
for year in Aggre_trans["Years"].unique():
    for quarter in Aggre_trans["Quarter"].unique():
        
        # Filter Aggre_trans for the current year and quarter
        at1= Aggre_trans[(Aggre_trans["Years"]==year)&(Aggre_trans["Quarter"]==quarter)]
        atf1= at1[["States", "Transaction_count"]]
        atf1=atf1.sort_values(by="States")
        atf1["Years"]=year
        atf1["Quarter"]=quarter
        frames.append(atf1)

merged_df = pd.concat(frames)
fig_tra= px.choropleth(merged_df, geojson= data1, locations= "States",featureidkey= "properties.ST_NM",
                        color= "Transaction_count", color_continuous_scale="Sunsetdark", range_color= (0,3000000),
                        title="TRANSACTION COUNT", hover_name= "States", animation_frame= "Years", animation_group= "Quarter")

fig_tra.update_geos(fitbounds= "locations", visible= False)
fig_tra.update_layout(width= 600, height= 700)
fig_tra.update_layout(title_font={"size":25})
st.plotly_chart(fig_tra)

def payment_amount():
    # Extract relevant columns from Aggre_trans DataFrame
    attype= Aggre_trans[["Transaction_type","Transaction_amount"]]
    # Group by transaction type and sum the transaction amounts
    att1= attype.groupby("Transaction_type")["Transaction_amount"].sum()
    # Create a DataFrame from the grouped data
    df_att1= pd.DataFrame(att1).reset_index()
    # Create a bar chart using Plotly Express
    fig_tra_pa= px.bar(df_att1, x= "Transaction_type", y= "Transaction_amount", title= "TRANSACTION TYPE and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Blues_r)
    #Layout Update
    fig_tra_pa.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_tra_pa)

def reg_all_states(state):
    # Filter Map_user data for the specified state
    mu = Map_user[["States", "Districts", "RegiseredUser"]]
    mu1 = mu.loc[(mu["States"] == state)]
    mu2 = mu1[["Districts", "RegiseredUser"]]
    mu3 = mu2.groupby("Districts")["RegiseredUser"].sum()
    mu4 = pd.DataFrame(mu3).reset_index()

    # Create a bar chart using Plotly Express
    fig_mu = px.bar(mu4, x="Districts", y="RegiseredUser", title="DISTRICTS and REGISTERED USER",
                    color_discrete_sequence=px.colors.sequential.Bluered_r)

    fig_mu.update_layout(width=1000, height=500)

    return st.plotly_chart(fig_mu)

def transaction_amount_year(sel_year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)
    
    # Extract and sort state names from the GeoJSON data
    state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
    state_names_tra.sort()
    
    # Get user input for the year
    year= int(sel_year)
    # Filter Aggregated Transaction data for the specified year
    atay= Aggre_trans[["States","Years","Transaction_amount"]]
    atay1= atay.loc[(Aggre_trans["Years"]==year)]
    atay2= atay1.groupby("States")["Transaction_amount"].sum()
    atay3= pd.DataFrame(atay2).reset_index()
    
    # Create choropleth map using Plotly Express
    fig_atay= px.choropleth(atay3, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_amount", color_continuous_scale="rainbow", range_color=(0,800000000000),
                            title="TRANSACTION AMOUNT and STATES", hover_name= "States")
    
    # Update choropleth map layout
    fig_atay.update_geos(fitbounds= "locations", visible= False)
    fig_atay.update_layout(width=600,height=700)
    fig_atay.update_layout(title_font= {"size":25})
    
    return st.plotly_chart(fig_atay)

def payment_count_year(sel_year):
    year= int(sel_year)
    # Filter Aggregated Transaction data for the specified year
    apc= Aggre_trans[["Transaction_type", "Years", "Transaction_count"]]
    apc1= apc.loc[(Aggre_trans["Years"]==year)]
    apc2= apc1.groupby("Transaction_type")["Transaction_count"].sum()
    apc3= pd.DataFrame(apc2).reset_index()
    # Create a bar chart using Plotly Express
    fig_apc= px.bar(apc3,x= "Transaction_type", y= "Transaction_count", title= "PAYMENT COUNT and PAYMENT TYPE",
                    color_discrete_sequence=px.colors.sequential.Brwnyl_r)
    fig_apc.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apc)

def transaction_count_year(sel_year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1=json.loads(response.content)
    
    # Extract and sort state names from the GeoJSON data
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()
    
    year= int(sel_year)
    
    # Filter Aggregated Transaction data for the specified year
    atcy= Aggre_trans[["States", "Years", "Transaction_count"]]
    atcy1= atcy.loc[(Aggre_trans["Years"]==year)]
    atcy2= atcy1.groupby("States")["Transaction_count"].sum()
    atcy3= pd.DataFrame(atcy2).reset_index()
    
    # Create a choropleth map using Plotly Express
    fig_atcy= px.choropleth(atcy3, geojson=data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_count", color_continuous_scale= "rainbow",range_color=(0,3000000000),
                            title= "TRANSACTION COUNT and STATES",hover_name= "States")
    fig_atcy.update_geos(fitbounds= "locations", visible= False)
    fig_atcy.update_layout(width=600, height= 700)
    fig_atcy.update_layout(title_font={"size":25})
    return st.plotly_chart(fig_atcy)

def payment_amount_year(sel_year):
    year= int(sel_year)
    # Filter Aggregated Transaction data for the specified year
    apay = Aggre_trans[["Years", "Transaction_type", "Transaction_amount"]]
    apay1= apay.loc[(Aggre_trans["Years"]==year)]
    apay2= apay1.groupby("Transaction_type")["Transaction_amount"].sum()
    apay3= pd.DataFrame(apay2).reset_index()
    # Create a bar chart using Plotly Express
    fig_apay= px.bar(apay3, x="Transaction_type", y= "Transaction_amount", title= "PAYMENT TYPE and PAYMENT AMOUNT",
                     color_discrete_sequence=px.colors.sequential.Burg_r)
    fig_apay.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apay)

def reg_state_all_RU(sel_year,state):
    year= int(sel_year)
    #Data Extraction
    mus= Map_user[["States", "Years", "Districts", "RegisteredUser"]]
    #Data Filtering
    mus1= mus.loc[(Map_user["States"]==state)&(Map_user["Years"]==year)]
    #Grouping and Aggregation:
    mus2= mus1.groupby("Districts")["RegisteredUser"].sum()
    #DataFrame Creation
    mus3= pd.DataFrame(mus2).reset_index()
    #Bar Chart Creation:
    fig_mus= px.bar(mus3, x= "Districts", y="RegisteredUser", title="DISTRICTS and REGISTERED USER",
                    color_discrete_sequence=px.colors.sequential.Cividis_r)
    fig_mus.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_mus)

def reg_state_all_TA(sel_year,state):
    year= int(sel_year)
    # Filter Map_user data for the specified year and state
    mts= Map_trans[["States", "Years","Districts", "Transaction_amount"]]
    mts1= mts.loc[(Map_trans["States"]==state)&(Map_trans["Years"]==year)]
    mts2= mts1.groupby("Districts")["Transaction_amount"].sum()
    mts3= pd.DataFrame(mts2).reset_index()
    # Create a bar chart using Plotly Express
    fig_mts= px.bar(mts3, x= "Districts", y= "Transaction_amount", title= "DISTRICT and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Darkmint_r)
    
    
    fig_mts.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_mts)

def ques1():
    # Extract relevant columns from Aggre_user data
    brand= Aggre_user[["Brands","Transaction_count"]]
    
    # Group and sum transaction counts by brand, then sort in descending order
    brand1= brand.groupby("Brands")["Transaction_count"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index()
    
    fig_brands= px.pie(brand2, values= "Transaction_count", names= "Brands", color_discrete_sequence=px.colors.sequential.dense_r,
                       title= "Top Mobile Brands of Transaction_count")
    return st.plotly_chart(fig_brands)

def ques2():
    lt= Aggre_trans[["States", "Transaction_amount"]]
    lt1= lt.groupby("States")["Transaction_amount"].sum().sort_values(ascending= True)
    lt2= pd.DataFrame(lt1).reset_index().head(10)

    fig_lts= px.bar(lt2, x= "States", y= "Transaction_amount",title= "LOWEST TRANSACTION AMOUNT and STATES",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

def ques3():
    htd= Map_trans[["Districts", "Transaction_amount"]]
    htd1= htd.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=False)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "Districts", title="TOP 10 DISTRICTS OF HIGHEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Emrld_r)
    return st.plotly_chart(fig_htd)

def ques4():
    htd= Map_trans[["Districts", "Transaction_amount"]]
    htd1= htd.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "Districts", title="TOP 10 DISTRICTS OF LOWEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Greens_r)
    return st.plotly_chart(fig_htd)

def ques5():
    sa= Map_user[["States", "AppOpens"]]
    sa1= sa.groupby("States")["AppOpens"].sum().sort_values(ascending=False)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "States", y= "AppOpens", title="Top 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.deep_r)
    return st.plotly_chart(fig_sa)

def ques6():
    sa= Map_user[["States", "AppOpens"]]
    sa1= sa.groupby("States")["AppOpens"].sum().sort_values(ascending=True)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "States", y= "AppOpens", title="lowest 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.dense_r)
    return st.plotly_chart(fig_sa)

def ques7():
    stc= Aggre_trans[["States", "Transaction_count"]]
    stc1= stc.groupby("States")["Transaction_count"].sum().sort_values(ascending=True)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "States", y= "Transaction_count", title= "STATES WITH LOWEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Jet_r)
    return st.plotly_chart(fig_stc)

def ques8():
    stc= Aggre_trans[["States", "Transaction_count"]]
    stc1= stc.groupby("States")["Transaction_count"].sum().sort_values(ascending=False)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "States", y= "Transaction_count", title= "STATES WITH HIGHEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Magenta_r)
    return st.plotly_chart(fig_stc)

def ques9():
    ht= Aggre_trans[["States", "Transaction_amount"]]
    ht1= ht.groupby("States")["Transaction_amount"].sum().sort_values(ascending= False)
    ht2= pd.DataFrame(ht1).reset_index().head(10)

    fig_lts= px.bar(ht2, x= "States", y= "Transaction_amount",title= "HIGHEST TRANSACTION AMOUNT and STATES",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

def ques10():
    dt= Map_trans[["Districts", "Transaction_amount"]]
    dt1= dt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    dt2= pd.DataFrame(dt1).reset_index().head(50)

    fig_dt= px.bar(dt2, x= "Districts", y= "Transaction_amount", title= "DISTRICTS WITH LOWEST TRANSACTION AMOUNT",
                color_discrete_sequence= px.colors.sequential.Mint_r)
    return st.plotly_chart(fig_dt)


#streamlit part   
st.title("PHONEPE DATA VISUALIZATION AND EXPLORATION")
tab1, tab2, tab3 = st.tabs(["***HOME***","***EXPLORE DATA***","***TOP CHARTS***"])

with tab1:
    col1,col2= st.columns(2)
    
    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("   **-> Credit & Debit card linking**")
        st.write("   **-> Bank Balance check**")
        st.write("   **->Money Storage**")
        st.write("   **->PIN Authorization**")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video(r"C:/Users/ELCOT/Desktop/phonepe/video/phonepe_add.mp4")
        
    col3,col4= st.columns(2)
    
    with col3:
        st.video(r"C:\Users\ELCOT\Desktop\phonepe\video\PhonePe_Motion_Graphics.mp4")
        
    with col4:
        st.write("**-> Easy Transactions**")
        st.write("**-> One App For All Your Payments**")
        st.write("**-> Your Bank Account Is All You Need**")
        st.write("**-> Multiple Payment Modes**")
        st.write("**-> PhonePe Merchants**")
        st.write("**-> Multiple Ways To Pay**")
        st.write("**-> 1.Direct Transfer & More**")
        st.write("**-> 2.QR Code**")
        st.write("**-> Earn Great Rewards**")
        
    col5,col6= st.columns(2)
    
    with col5:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("**->No Wallet Top-Up Required**")
        st.write("**->Pay Directly From Any Bank To Any Bank A/C**")
        st.write("**->Instantly & Free**")
        
    with col6:
        st.video(r"C:/Users/ELCOT/Desktop/phonepe/video/PhonePe_Motion_Graphics2.mp4")
        
        
with tab2:
    sel_year = st.selectbox("select the Year",("All", "2018", "2019", "2020", "2021", "2022", "2023"))
    if sel_year == "All" :
        col1, col2 = st.columns(2)
        with col1:
            animate_all_amount()
            payment_count()
            
        with col2:
            animate_all_count()
            payment_amount()
            
        state=st.selectbox("selecet the state",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                                'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                'Uttarakhand', 'West Bengal'))
        
        reg_all_states(state)
        
    else:
        col1,col2= st.columns(2)
        
        with col1:
            transaction_amount_year(sel_year)
            payment_count_year(sel_year)
            
        with col2:
            transaction_count_year(sel_year)
            payment_amount_year(sel_year)
            state= st.selectbox("selecet the state",('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                                'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                'Uttarakhand', 'West Bengal'))
            reg_state_all_RU(sel_year,state)
            reg_state_all_TA(sel_year,state)
            
    with tab3:
        ques= st.selectbox("select the question",('Top Brands Of Mobiles Used','States With Lowest Trasaction Amount',
                                  'Districts With Highest Transaction Amount','Top 10 Districts With Lowest Transaction Amount',
                                  'Top 10 States With AppOpens','Least 10 States With AppOpens','States With Lowest Trasaction Count',
                                 'States With Highest Trasaction Count','States With Highest Trasaction Amount',
                                 'Top 50 Districts With Lowest Transaction Amount'))
        
        if ques=="Top Brands Of Mobiles Used":
            ques1()
            
        elif ques=="States With Lowest Trasaction Amount":
            ques2()
            
        elif ques=="Districts With Highest Transaction Amount":
            ques3()
            
        elif ques=="Top 10 Districts With Lowest Transaction Amount":
            ques4()
            
        elif ques=="Top 10 States With AppOpens":
            ques5()
            
        elif ques=="Least 10 States With AppOpens":
            ques6()
            
        elif ques=="States With Lowest Trasaction Count":
            ques7()
            
        elif ques=="States With Highest Trasaction Count":
            ques8()
            
        elif ques=="States With Highest Trasaction Amount":
            ques9()
            
        elif ques=="Top 50 Districts With Lowest Transaction Amount":
            ques10()




      

