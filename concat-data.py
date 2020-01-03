import pandas as pd
import glob

sPath = 'data'
oAllFiles = glob.glob(sPath + "/*.csv")
df = pd.concat((pd.read_csv(oFile) for oFile in oAllFiles))

df = df.dropna(how='any') # lots of N/As from the CSV conversion
df.columns = ['identifier', 'municipality','location','feature','owner','year_built_replaced','last_inspection','sd_fo_status','rating'] # give proper columns

# save the concatenated data to CSV (dont write index column, keep header names)
df.to_csv('./all-bridge-data.csv', index = None, header=True)

# Get a bool series representing which row satisfies the condition i.e. True for
# row in which value of 'Age' column is more than 30
# oSeries = df.apply(lambda x: True if float(x['rating']) < 5 else False , axis=1)

iIndeterminateCount = 0
iBadBridgesCount = 0
iGoodBridgesCount = 0
iPerfectBridgesCount = 0

for i in df.index:
    try:
        fRating = df['rating'].iloc[i]
        float(fRating)
        if float(fRating) > 5:
            iGoodBridgesCount = iGoodBridgesCount + 1
        if float(fRating) < 5:
            iBadBridgesCount = iBadBridgesCount + 1
        if float(fRating) == 7:
            iPerfectBridgesCount = iPerfectBridgesCount + 1
    except ValueError:
        print "Not a float"
        iIndeterminateCount = iIndeterminateCount + 1
 
 
print 'Number of Rows in dataframe in which rating < 5 (bad bridges) : ', iBadBridgesCount
print 'Number of Rows in dataframe in which rating > 5 (good bridges) : ', iGoodBridgesCount
print 'Number of Rows in dataframe in which rating = 7 (perfect bridges) : ', iPerfectBridgesCount
print iIndeterminateCount, ' bridge statuses could not be determined'
print '(Thats out of ', len(df.index), ' bridges!)'