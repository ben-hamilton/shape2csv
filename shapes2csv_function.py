
#Import the packages that will be used
import geopandas as gpd
import pandas as pd
import os


# In[9]:
def shapes2csv(directory, full, columns):

    file_paths = []

    for subdir, dirs, files in os.walk(directory):#insert your directory here. 
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".shp"):
                filename = os.path.splitext(filepath)[0]#this takes the extension off of the file name. This sets us up to save the file with an altered name and different extension more easily. 
                file_paths.append(filename)
    
    for p in range(len(file_paths)):
        path = file_paths[p]
        print(path)
        gdf = gpd.read_file(f'{path}.shp')#imports shapefile as a geodatabase
        df = pd.DataFrame(gdf)#converts shapefile to a regular boring old database
        fname = f'{file_paths[p]}_full.csv'#makes a new file name with extension
        if full == True:
            df.to_csv(fname)#save full csv
        
            if columns != None:
                cols = [col for col in df.columns if col in columns]
                df = df[df.columns[df.columns.isin(cols)]]
    #if you don't know the names of all the fields, you can also use numbers. This can also save you some time typing out a long list. 
    #for example:
    #df = df[df.columns[0:7]]
                fname = f'{file_paths[p]}_reduced.csv'#again, make a new file name
                df.to_csv(fname)#save reduced csv
            else:
                pass
        else:
            pass



