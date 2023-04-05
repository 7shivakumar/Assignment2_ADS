import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_csv(file):
    '''
    This function will take parameter from the main function.
    and reads the file from the local disk with help of pandas
    module.
    '''
    df = pd.read_csv(file)
    df.set_index('Country Name', inplace=True)
    countries = ["United Kingdom","Italy","Norway","Finland","Germany","Mexico"]
    df = df.loc[countries,["2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    #mask = df['Country Name'].str.contains('united kingdom|italy|norway|finland|germany|mexico', case=False)
    #df = df[mask]
    df_t = df.transpose()
    
    return df,df_t


# passing the filenames to read_Csv function and considering specific contries and respected years
df_co2,df_co2_t = read_csv("co2emission.csv")
df_energy,df_energy_t = read_csv("energyconsumption.csv")

# showing the informationa and describing the dataframes
df_co2_t.info()
df_co2_t.describe()

df_energy.info()
df_energy_t.describe()

# Ploting the line chart for CO2 Emission
df_co2_t.plot(kind="line", figsize=(10, 5))

# Set the chart title and axis labels
plt.title("CO2 Emissions from Liquid Fuel Consumption")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")
plt.legend()

# Show the chart
plt.show()

# ploting stacked bargraph for every 4 year interval from 2003 to 2015
years = ["2003","2007","2011","2015"]
df_co2_ = df_co2.loc[:,years]
df_co2_.plot(kind="bar", figsize=(10, 5))
# Set the chart title and axis labels
plt.title("CO2 Emissions from Liquid Fuel Consumption")
plt.xlabel("Year")
plt.ylabel("CO2 Emissions")
plt.legend()
# Show the chart
plt.show()


# Ploting the line chart for Electricity production from coal sources
df_energy_t.plot(kind="line", figsize=(10, 5))

# Set the chart title and axis labels
plt.title("Electricity Production from Coal Sources")
plt.xlabel("Year")
plt.ylabel("Electricity production from Coal sources")
plt.legend()

# Show the chart
plt.show()

#ploting stacked bargraph for every 4 year interval from 2003 to 2015
years = ["2003","2007","2011","2015"]
df_energy_ = df_energy.loc[:,years]
df_energy_.plot(kind="bar", figsize=(10, 5))
plt.title("Electricity Production from Coal Sources")
plt.xlabel("Countries")
plt.ylabel("Electricity Production from Coal Sources")
plt.legend()
plt.show()

def Germany_heatmap():
    # Selecting the indicators which could be the corelation to one other
    country = 'Germany'
    indicators = ['EN.ATM.CO2E.KT','EG.ELC.COAL.ZS','EN.ATM.METH.KT.CE','SP.POP.GROW','EN.ATM.NOXE.KT.CE']
    
    # get the data from World Bank dataset
    data = pd.read_excel("API_19_DS2_en_excel_v2_5360124.xls",skiprows=(3))

    # clean and format the data and considering for the country Germany and with required indicators
    data=data.loc[data['Country Name']=='Germany']
    data = data.loc[data['Indicator Code'].isin(indicators)]
    data = data.loc[:,["Country Name","Indicator Name","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    
    # creating Pivot table for dataframe
    
    df_g = data.pivot_table(data,columns= data['Indicator Name'])

    
    # ploting the heatmap with the correlation between the mentioned indicators
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_g.corr(), annot=True, fmt='.2f', cmap='YlGnBu')
    
    # add title and axis labels
    plt.title(f'{country} Indicators Heatmap')
    plt.xlabel('Year')
    plt.ylabel('Indicator')
    
    # show the plot
    plt.show()
    
    
def UK_heatmap():
    # Selecting the indicators which could be the corelation to one other
    country = 'United Kingdom'
    indicators = ['EN.ATM.CO2E.KT','EG.ELC.COAL.ZS','EN.ATM.METH.KT.CE','SP.POP.GROW','EN.ATM.NOXE.KT.CE']
    
    # get the data from World Bank dataset
    data = pd.read_excel("API_19_DS2_en_excel_v2_5360124.xls",skiprows=(3))

    # clean and format the data and considering for the country United Kingdom and with required indicators
    data=data.loc[data['Country Name']=='United Kingdom']
    data = data.loc[data['Indicator Code'].isin(indicators)]
    data = data.loc[:,["Country Name","Indicator Name","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]]
    
    # creating Pivot table for dataframe
    
    df_g = data.pivot_table(data,columns= data['Indicator Name'])

    
    # ploting the heatmap with the correlation between the mentioned indicators
    plt.figure(figsize=(10, 6))
    sns.heatmap(df_g.corr(), annot=True, fmt='.2f', cmap='Greens',linecolor='black', cbar=True, vmin=0, vmax=100000, linewidths=0.5)
    
    # add title and axis labels
    plt.title(f'{country} Indicators Heatmap')
    plt.xlabel('Year')
    plt.ylabel('Indicator')
    
    # show the plot
    plt.show()

# generating heatmaps for countries Germany and United Kingdom
Germany_heatmap()
UK_heatmap()








