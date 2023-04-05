# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 03:10:02 2023

@author:Pooja Veliyilparambu Sunilkumar
"""

# import modules pandas mat plot and csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
# Function for plotting plots


class plotting:
    def _init_(self) -> None:
        self.list_countries = ['India', 'United States', 'China',
                               'Canada', 'Japan']
        self.list_years = ['2005', '2006', '2007', '2008', '2009']
# Function for plotting bar plot
# Setting labels

    def bar_plot(self, df, labelx, labely, plt_title, imgfile):
        df.columns.name = None
        df = df.reset_index().rename(columns={'index': 'Year'})
        df = df[['Year', 'India', 'United States',
                 'China', 'Canada', 'Japan']]
        df = df[(df["Year"] == "2005") | (df["Year"] == "2006") |
                (df["Year"] == "2007") | (df["Year"] == "2008") |
                (df["Year"] == "2009")]
        plt.figure(figsize=(28, 20))
        bp = plt.subplot(1, 1, 1)
        np_tot = np.arange(len(self.list_countries))
        width = 0.1
        wd1 = np_tot
        wd2 = [x + width for x in wd1]
        wd3 = [x + width for x in wd2]
        wd4 = [x + width for x in wd3]
        wd5 = [x + width for x in wd4]
        bar_plt1 = bp.bar(wd1, df["India"], width, label=2005,
                         color="lightcoral")
        bar_plt2 = bp.bar(wd2, df["United States"], width,
                          label=2006, color="slateblue")
        bar_plt3 = bp.bar(wd3, df["China"], width,
                          label=2007, color="limegreen")
        bar_plt4 = bp.bar(wd4, df["Canada"], width,
                          label=2008, color="olive")
        bar_plt5=bp.bar(wd5, df["Japan"], width,
                        label=2009, color="plum")
   
        bp.set_xticks([r + width for r in range(len(self.list_countries))],
                      ['India', 'USA', 'China', 'Canada', 'Japan'],
                      fontsize=30, rotation=90)

        # plotting labels, title and legend
        plt.xlabel(labelx, fontweight='bold', fontsize=30)
        plt.ylabel(labely, fontweight='bold', fontsize=30)
        bp.set_title(plt_title, fontsize=40)
        plt.legend(fontsize=20)
        plt.savefig("plots/"+imgfile, dpi=300)
        plt.grid()
        # plt.show()
    # Function for plotting line graph

    def plot_line(self, df, labelx, labely, plt_title, imgfile):
        df = df[['Country Name', '2005', '2006', '2007', '2008', '2009']]
        df = df[(df["Country Name"] == "India") |
                (df["Country Name"] == "United States") |
                (df["Country Name"] == "China") |
                (df["Country Name"] == "Canada") |
                (df["Country Name"] == "Japan")]
        plt.figure(figsize=(25, 15))
        si_cn = df.set_index('Country Name')
        tra_cn = si_cn.transpose()
        tra_cn.head()
        for i in range(len(self.list_countries)):
            plt.plot(tra_cn.index, tra_cn[self.list_countries[i]],
                     label=self.list_countries[i])

        # plotting title,label and legend
        plt.title(plt_title, size=30)
        plt.xlabel(labelx, size=30)
        plt.ylabel(labely, size=30)
        plt.xticks(rotation=90, fontsize=20)
        plt.yticks(fontsize=20)
        plt.legend(fontsize=20)
        plt.grid()

        # save figure
        plt.savefig("plots/"+imgfile, dpi=300)

    def co_mean(self, df):
   # The statiscal function to plot and save Mean of CO Emission
        plt.figure(figsize=(28, 20))
        plt.title("CO2 Emisson across Countries", size=30)
        plt.xlabel("Years", size=30)
        plt.ylabel("Mean CO2 Emission ", size=30)
        plt.xticks(range(0, 30), df.columns.values[1:31], rotation = 90)
        plt.grid()
        plt.plot(df[df.columns[1:31]].mean().index, df[df.columns[1:31]]
                 .mean(), "-.r", linewidth=5)
        df[df.columns[1:31]].mean().to_csv("data\mean.csv")
        # Writing Mean Values into Csv file
        new_header = ['year', 'Mean']
        with open("data\yearsmean.csv", 'w') as f_op:
            with open("data\mean.csv", 'r') as file:
                csvreader = csv.reader(file)
                write = csv.writer(f_op, lineterminator='\n')
                write.writerow(new_header)
                next(csvreader)
                for row in csvreader:
                    write.writerow(row)
   
        plt.savefig("plots/co_mean.png", dpi=300)


# Program Starts here
def data_prep(filename):
    # reading csv file
    df = pd.read_csv(filename, skiprows=4)
    # Data Cleaning
    # removing unwanted colums
    df = df.drop('Indicator Name', axis=1)
    df = df.drop('Indicator Code', axis=1)
    df = df.drop('Country Code', axis=1)
    # removing columns with no row data
    df = df.dropna(axis=1, how='all')
    df1 = df[pd.notnull(df.mean(axis=1))]
    print("Data Cleaning Done..")
    # Transposing data
    df2 = df1.set_index('Country Name').transpose()
    # df1 dataframe with years as columns
    # df2 dataframe with countries as columns
    return df1, df2


try:
    # Processing Electric Power Consumption dataset
    df_years, df_countries = data_prep(r"C:\Users\demon\Desktop\ClimateChange\ClimateChange\data\epc_data.csv")
    # Creating Instance for the  Class : Electric Power Consumption  Data Bar Graph PLotting
    epc = plotting()
    epc.bar_plot(df_countries, 'Countries',
                 'Electic Power Consumption (kWh)per capita',
                 'Electic Power Consumption', 'epc_barplot.png')
    # Processing Population  dataset
    df_years, df_countries = data_prep(r"C:\Users\demon\Desktop\
                                       ClimateChange\ClimateChange\
                                           data\population_data.csv")
    # Creating  Instance for the  Class : Population Data Bar Graph PLotting
    pop = plotting()
    pop.bar_plot(df_countries, 'Countries', 'Population',
                 'Total Population',
                 'pop_barplot.png')
    # Processing CO2  dataset
    df_years, df_countries = data_prep(r"C:\Users\demon\Desktop\ClimateChange\
                                       ClimateChange\data\
                                           co2_emission_data.csv")
    # Creating Instance for the  Class : Co2 Data Line Graph PLotting
    co2 = plotting()
    co2.plot_line(df_years, "Years", "Co2 Emission", "Co2 Emission",
                  "co2_lineplot.png")
    # MEAN Calculation , PLotting and saving in CSV file
    co2.co_mean(df_years)
    # Processing Energy use  dataset
    df_years, df_countries = data_prep(r"C:\Users\demon\Desktop\
                                       ClimateChange\ClimateChange\
                                           data\energy_data.csv")
    # Creating Instance for the  Class : Energy Use Data Line Graph PLotting
    eu = plotting()
    eu.plot_line(df_years, "Years",
                 "Energy use (kg of oil equivalent per capita)",
                 "Energy Use", "eu_lineplot.png")

except FileNotFoundError as e:
    print(f"FileNotFoundError "f"{e}")
