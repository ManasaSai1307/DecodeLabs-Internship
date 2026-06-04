
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# LOAD DATASET
df = pd.read_excel("Cleaned_Data.xlsx")

print("DATASET OVERVIEW")

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.info())


# MISSING VALUES
print("\nMISSING VALUES\n")
print(df.isnull().sum())


# DUPLICATES
print("\nDUPLICATE RECORDS\n")
print("Total Duplicates:", df.duplicated().sum())


# DESCRIPTIVE STATISTICS
print("\nDESCRIPTIVE STATISTICS\n")
print(df.describe())
numeric_cols = df.select_dtypes(include=np.number).columns

print("\nMean:")
print(df[numeric_cols].mean())

print("\nMedian:")
print(df[numeric_cols].median())

print("\nMinimum:")
print(df[numeric_cols].min())

print("\nMaximum:")
print(df[numeric_cols].max())



# PRODUCT-WISE REVENUE ANALYSIS
if 'Product' in df.columns and 'TotalPrice' in df.columns:
    revenue = (
        df.groupby('Product')['TotalPrice']
        .sum()
        .sort_values(ascending=False)
    )
    print("\nPRODUCT-WISE REVENUE ANALYSIS\n")
    print(revenue)


# ORDER STATUS ANALYSIS

if 'OrderStatus' in df.columns:
    status = df['OrderStatus'].value_counts()
    print("\nORDER STATUS DISTRIBUTION ANALYSIS\n")
    print(status)

# PAYMENT METHOD ANALYSIS

if 'PaymentMethod' in df.columns:
    payment = df['PaymentMethod'].value_counts()
    print("\nPAYMENT METHOD USAGE ANALYSIS\n")
    print(payment)

# REFERRAL SOURCE ANALYSIS

if 'ReferralSource' in df.columns:
    referral = df['ReferralSource'].value_counts()
    print("\nREFERRAL SOURCE PERFORMANCE ANALYSIS\n")
    print(referral)

# COUPON CODE ANALYSIS

if 'CouponCode' in df.columns:
    coupon = df['CouponCode'].value_counts()
    print("\nCOUPON CODE UTILIZATION ANALYSIS\n")
    print(coupon)
    
# HISTOGRAMS
plt.figure(figsize=(8,5))
df["TotalPrice"].hist(bins=20)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.show()


# BOXPLOTS (OUTLIERS)
plt.figure(figsize=(8,5))
sns.boxplot(x=df["UnitPrice"])
plt.title("Outlier Detection - Unit Price")
plt.xlabel("Unit Price")
plt.show()

# CORRELATION HEATMAP
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()


# SCATTER PLOTS
plt.figure(figsize=(8,5))
sns.scatterplot(x="Quantity", y="TotalPrice", data=df)
plt.title("Quantity vs Total Price")
plt.show()


# KEY INSIGHTS
print("\nEDA COMPLETED SUCCESSFULLY\n")

