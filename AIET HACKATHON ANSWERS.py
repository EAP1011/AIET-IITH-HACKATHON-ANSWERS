1ST QUESTION:
import pandas as pd
df=pd.read_csv("Total orders.csv")
regord=df["Region"].unique().tolist()
regdata=df.groupby("Region")
tredord=[regdata.get_group(x)["Units Sold"].sum() for x in regord]
avgp=[(regdata.get_group(x)["Unit Price"].sum())/((regdata.get_group(x)).shape[0]) for x in regord]
print(regord)
print(tredord)
print(avgp)

2ND QUESTION:
import pandas as pd
df=pd.read_csv("Total orders.csv")
df["Ship Date"]=pd.to_datetime(df["Ship Date"]).dt.strftime("%d/%b/%Y")
df["Order Date"]=pd.to_datetime(df["Ship Date"]).dt.strftime("%d/%b/%Y")
df["Duration"]=(df["Ship Date"]-df["Order Date"]).dt.days
op=df.groupby("Order Priority")
ordp=df["Order Priority"].unique().tolist()
print(df["Duration"].max())
avgp=[(op.get_group(x)["Duration"].sum())/((op.get_group(x)).shape[0]) for x in op]
print(avgp)

3RD QUESTION:
import pandas as pd
df=pd.read_csv("Total orders.csv")
regord=df["Item Type"].unique().tolist()
reg1ord=df["Sales Channel"].unique().tolist()
regdata=df.groupby("Item Type")
reg1data=df.groupby("Sales Channel")
tredord=[regdata.get_group(x)["Units Sold"].sum() for x in regord]
salesord=[reg1data.get_group(x)["Units Sold"].sum() for x in reg1ord]
print(tredord)
print(salesord)

4TH QUESTION:
import pandas as pd
df1=pd.read_csv("Total orders.csv")
df2=pd.read_csv("costfile.csv")
joineg=df1.join(df2,lsuffix="_",rsuffix="__")
print(joineg)
joineg["Total Cost"]=joineg["Units Sold"]*joineg["Unit Cost"]
joineg["Total Profit"]=(joineg["Unit Price"]*joineg["Units Sold"])-joineg["Total Cost"]

5TH QUESTION:
import pandas as pd
df1=pd.read_csv("Total orders.csv")
df2=pd.read_csv("costfile.csv")
joineg=df1.join(df2,lsuffix="_",rsuffix="__")
joineg["Total Cost"]=joineg["Units Sold"]*joineg["Unit Cost"]
joineg["Total Profit"]=(joineg["Unit Price"]*joineg["Units Sold"])-joineg["Total Cost"]
print(joineg["Total Profit"].max())
print()
