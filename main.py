import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb 
import numpy as np



class SalesDataAnalyzer:
    def __init__(self):
        self.ld_data=None
        self.a=None
    def load_data(self):
        try:
            print("="*3,"Load Dataset","="*3)
            self.ld_data=input("Enter the path of the dataset (CSV file): ")
            self.ld_data=pd.read_csv(f'{self.ld_data}')
            print('Dataset Loaded Sucessfully !')
            return self.ld_data

        except:
            print("Please Enter Valid Address")
    def explore_data(self):
            try:
                print("="*3,"Explore Data","="*3)
                print("1. Display the First 5 Rows ")
                print("2. Display the Last 5 Rows ")
                print("3. Display column names ")
                print("4. Display Data Types ")
                print("5. Display Basic info ")
                choice=int(input("Enter your Chocie : "))
                if choice==1:
                    head=self.ld_data.head()
                    print(head)
                elif choice==2:
                    tail=self.ld_data.tail()
                    print(tail)
                elif choice==3:
                    cols=self.ld_data.columns
                    print(cols)
                elif choice==4:
                    dt=self.ld_data.dtypes
                    print(dt)
                elif choice==5:
                    info=self.ld_data.info()
                    print(info)
                else:
                    print("Invalid Choice !!")
            except:
                print("Please Load the Dataset First !!")
        
    def clean_data(self):
        try:
            print("="*3," Handle Missing Data ","="*3)
            print("Please select an option:")
            print("1. Display rows With Missing Values ")
            print("2. Fill missing Values with mean")
            print("3. Drop rows with Missing Values")
            print("4. Replace Missing Values with a Specific Value ")
            
            choice=int(input("Enter your Chocie : "))
            if choice==1:
                if  self.ld_data.isnull().empty:
                    print("No Missing Values Found in the Dataset !")
                else:
                    null=self.ld_data.isnull()
                    print(null)
            
            elif choice==2:
                df=self.ld_data.fillna(self.ld_data.mean())
                print(df.head())
            elif choice==3:
                print("=== Before Cleaning ===")
                print(df.isnull().sum())
                df=self.ld_data.dropna()
                print("=== After Cleaning ===")
                print(df.isnull().sum())
            elif choice==4:
                replace=input("Enter a Value to Replace it with Missing Value : ")
                dt=self.ld_data.fillna(replace)
                print(f"Missing Values Replaced with {replace} Sucessfully ! ")

            else:
                print("Invalid Choice !!")
        except:
            print("Please Check missing Values in the Dataset First !!")

    def math_op(self):
        try:
            print()
            print("="*3," DataFrame Operations  ","="*3)
            print("1. Sum of Sales")
            print("2. Top 5 Products  With Most Sales")
            print("3. Top 5 Products With Lowest Sales")
            print("4. Most Sales in a Region ")
            print("5. Most Quantity Sold of Every Product")
            
            choice=int(input("Enter your Choice : "))
            if choice == 1:
                print("=== Sum of Sales ===")
                print(self.ld_data['Sales'].sum())

            elif choice == 2:
                print("=== Top 5 Products With Most Sales ===")
                print(self.ld_data.nlargest(5, 'Sales')[['Product_Category', 'Sales']])

            elif choice == 3:
                print("=== Top 5 Products With Lowest Sales ===")
                print(self.ld_data.nsmallest(5, 'Sales')[['Product_Category', 'Sales']])

            elif choice == 4:
                print("=== Region With Most Sales ===")
                print(self.ld_data.groupby('Region')['Sales'].sum().nlargest(1))

            elif choice == 5:
                print("=== Region With Most Profit ===")
                print(
                    self.ld_data.groupby('Region')['Profit'].sum().nlargest(1))

            else:
                print("Invalid Choice (1-5)!!")
        except:
            print("Something went wrong !!")
    
        
     
    def visualize_data(self):
        try:
            print()
            print("="*3," Data Visualization  ","="*3)
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart ")
            print("5. Histogram ")
            print("6. Stack Plot ")
            choice=int(input("Enter your Choice : "))
            if choice==1:
                print("="*3," Bar Plot  ","="*3)
                title=input("Enter Title Of Bar Plot :")
                x_axis=input("Enter x-axis Column Name : ").capitalize()
                self.a=self.ld_data[f'{x_axis}'].plot(
                    kind="bar"
                )
                print("Generating a Bar Plot......")
                plt.title(title)
                plt.show()
                print("Bar Plot Displayed Sucessfully !")
                return self.a
            
            elif choice==2:

                print("="*3," Line Plot  ","="*3)
                title=input("Enter Title Of Line Plot :")
                x_axis=input("Enter x-axis Column Name : ")
                self.a=self.ld_data[f'{x_axis}'].plot(
                    kind="line",
                    marker="o"
                )
                print("Generating a Line Plot......")
                plt.title(title)
                plt.show()
                print("Line Plot Displayed Sucessfully !")
                return self.a
                
            elif choice==3:

                print("="*3," Scatter Plot  ","="*3)
                title=input("Enter Title Of Scatter Plot :")
                x_axis=input("Enter x-axis Column Name : ")
                y_axis=input("Enter y-axis Column Name : ")
                self.a=self.ld_data.plot(
                    kind="scatter",
                    x=f"{x_axis}",
                    y=f"{y_axis}"
                )
                print("Generating a Scatter Plot......")
                plt.title(title)
                plt.show()
                print("Scatter Plot Displayed Sucessfully !")
                return self.a
                
            elif choice==4:
                print("="*3," Pie Chart  ","="*3)
                title=input("Enter Title Of Pie Chart:")
                x_axis=input("Enter a Column Name : ")
                self.a=self.ld_data.set_index('Product')[f'{x_axis}'].plot(
                    kind="pie",
                    pcs="%1.2f%%",
                    shadow=0.9,
                    legend=True
                )
                plt.plot(x="Product",y="price")
                print("Generating a Pie Chart......")
                plt.title(title)
                plt.show()
                print("Pie Chart Displayed Sucessfully !")
                return self.a

                
            elif choice==5:

                print("="*3," Histogram Plot  ","="*3)
                title=input("Enter Title Of Histogram Plot :")
                x_axis=input("Enter x-axis Column Name : ")
                y_axis=input("Enter y-axis Column Name : ")
                self.a=self.ld_data.plot(
                    kind="hist",
                    x=f"{x_axis}",
                    y=f"{y_axis}"
                )
                print("Generating a Histogram Plot......")
                plt.title(title)
                plt.show()
                print("Histogram Plot Displayed Sucessfully !")
                return self.a

                
            elif choice==6:
                
                print("="*3," Histogram Plot  ","="*3)
                title=input("Enter Title Of Histogram Plot :")
                x_axis=input("Enter x-axis Column Name : ")
                y_axis=input("Enter y-axis Column Name : ")
                self.a=self.ld_data.plot(
                    kind="",
                    x=f"{x_axis}",
                    y=f"{y_axis}"
                )
                print("Generating a Histogram Plot......")
                plt.title(title)
                plt.show()
                print("Histogram Plot Displayed Sucessfully !")
                return self.a
            else:
                print("Invalid Choice (1-6) ")
        except:
            print("Something went wrong !!")
            
    def save_data(self):

        name = input("Enter File Name (e.g. sales.png): ")

        try:
            self.a.figure.savefig(name)
            print(f"Visualization saved as {name} successfully!")
        except:
            print(f"Error saving visualization: {name}")


    def stat_analysis(self):
        try:
            print()
            print("=== Statical Analysis ===")
            print("1. Minimum Sales ")
            print("2. Maximum Sales ")
            print("3. Average of Sales ")
            print("4. Median of Sales ")
            print("5. Standard Deviation of Sales ")
            choice=int(input("Enter your Choice : "))
            if choice==1:
                print("=== Minimum Sales ===")
                print(self.ld_data['Sales'].min())
            elif choice==2:
                print("=== Maximum Sales ===")
                print(self.ld_data['Sales'].max())
            elif choice==3:
                print("=== Average of Sales ===")
                print(self.ld_data['Sales'].mean())
            elif choice==4:
                print("=== Median of Sales ===")
                print(self.ld_data['Sales'].median())
            elif choice==5:
                print("=== Standard Deviantion of Sales ===")
                print(self.ld_data['Sales'].std())
            else:
                print("Invalid Choice (1-5) !!")
        except:
            print("Something went wrong !!")
            
        
    def main_menu(self):
        try:
            while True:
                print()
                print("="*10,"Data Analysis & Visualization Program ","="*10)
                print("Please select an option:")
                print("1. Load Dataset")
                print("2. Explore Data")
                print("3. Perform DataFrame Operations ")
                print("4. Handle Missing Data")
                print("5. Generate Descriptive Statistics ")
                print("6. Data Visualization ")
                print("7. Save Visualization ")
                print("8. Exit ")
                print("="*20)

                choice=int(input("Enter your Choice : "))
                if choice==1:
                    self.load_data()
                elif choice==2:
                    self.explore_data()
                elif choice==3:
                    self.math_op()
                elif choice==4:
                    self.clean_data()
                elif choice==5:
                    self.stat_analysis()
                elif choice==6:
                    self.visualize_data()
                elif choice==7:
                    self.save_data()
                elif choice==8:
                    print("Exiting The Program GoodBye !")
                    break
                else:
                    print("Invalid Choice !")
        except:
            print("Something went wrong !!")


    def __del__(self):
        pass




obj=SalesDataAnalyzer()
obj.main_menu()
