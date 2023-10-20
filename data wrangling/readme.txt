#Loading and Inspecting the Data:
	#Load the dataset into a Pandas DataFrame.
	#Show df summary information.
	#Show stats info on numerical columns.
	#Display the first few rows of the DataFrame.
	#Check the data types of each column.



#Handling Missing Values:
	#Identify missing values in the dataset.
		#Count the number of missing values in each column.
	
	#Show rows with missing values on a specific column name.

	#Replace empty values with NaN in all rows.

	#Replace NaN values in any column with the previous value.

	#Replace NaN values in two or more columns (df.isna({"Key": value, "Key2" : value2, "Key3" : value3})

	#Delete rows 
		#with all columns empty values.
		#with empty values in any column.

	#Impute missing numerical values.
		#Mean Imputation: Replace missing values with the mean (average) value of the non-missing values in the same column. 
		#This is a simple and often effective method.

		#Median Imputation: Replace missing values with the median value of the non-missing values in the same column. 
		#This is less sensitive to outliers compared to mean imputation.
		
		#Mode Imputation: For discrete or categorical data, 
		#you can replace missing values with the mode (most frequent) value in the same column.

		#Backward / Forward imputation: 

		#Interpolation: For time-series data, you can use interpolation methods to estimate missing values based on the values 
		#before and after the missing point in time.
		
		#IterativeImputer: Trains a regression model using high correlated features as predictors and targets the feature of missing values
		#   impute_it = IterativeImputer() #Create object
		#   impute_it.fit_transform(X) #X es el dataframe con los features que se correlacionan mas altos
		
		#K-Nearest Neighbors (KNN) Imputation: Replace missing values with the average of values from the k-nearest 2 neighbors 
		#in a multi-dimensional space.
		#   inpute_knn = KNNImputer(n_neighbors = 2)
		#   inpute_knn.fit_transform(X) #X es el dataframe con los features que se correlacionan mas altos
		
		

	#Impute missing categorical values. (revisar)

	#Drop rows and columns with NaN values
		#Drop rows
			#Where all elements are missing
			#keep only rows with at least 2 non-NA values
		#Drop all columns with missing values
		#with more than 15% percentage of missing values. 
			#For one specific column
			#For all columns


#Handling Duplicates:
	#Detect and remove all duplicated rows for all columns.
	#Detect and remove all duplicated rows for a group of columns.
	#Detect and remove all duplicated rows for a group of columns. Drop all except first occurrence


#Data Type Conversion:
	#Convert all numerical columns to string
	#Convert one numerical column to string
	#Convert column string format to datetime
	#Convert any yes/no column to categorical data


#Renaming Columns:
	#Rename column by name
	#Rename a list of columns
	#Rename all columns to lowercase
	

#Standardizing Text Data:
	#Standardize text data in any column converting strings to lowercase 