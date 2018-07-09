import numpy as np 
import pandas as pd

moviedf = pd.read_csv("IMDB-Movie-Data.csv",header=0,index_col=None)
moviedf.drop(['Rank','Metascore'],axis=1,inplace=True)


hashtable = [[] for x in range(100)]

def hash_function(x):
	return x%10

def insert(hashtable,input,value):
	hashtable[hash_function(input)].append((input,value))

for i in range(1000):
	insert(hashtable,i,moviedf['Title'][i])

#print(hashtable)

print("Choose Movie based :")
print("1.Title       2.Genre       3.Actor/Actress       4.Director       5.Highest Ratings       6.Revenue")
Displaydata = ["Title","Genre","Description","Director","Actors","Year","Runtime (Minutes)","Rating","Votes","Revenue (Millions)"]
choice = int(input())

if choice == 1:
	print("Enter title of the Movie you wish to watch :")
	name = input()
	bolvalue = moviedf['Title'].str.contains(name)
	Titlelist = moviedf[bolvalue].values
	if len(Titlelist) == 0:
	 	print("Sorry, Movie",name," not present in our Database !")
	 	quit()
	else:
		print("\n")
		for tit in Titlelist:
			for i in range(len(Displaydata)):
				print(Displaydata[i],":   ",tit[i]) 
			print("\n")

elif choice == 2:
	print("Enter Genre of the Movie you wish to watch :")
	individual_genres = ['Action','Adventure','Animation','Biography','Comedy','Crime','Drama','Family','Fantasy','History','Horror','Music','Musical','Mystery','Romance','Sci-Fi','Sport','Thriller','War','Western']
	for i in range(len(individual_genres)):
		print(i+1,". ",individual_genres[i],sep='')
	
	name = input()
	bolvalue = moviedf['Genre'].str.contains(name)
	Genrelist = moviedf[bolvalue].values
	Filelist = []
	print("\n")
	for gen in Genrelist:
		for i in range(len(Displaydata)):
			print(Displaydata[i],":   ",gen[i]) 
		print("\n")
	
	moviedf[bolvalue].to_csv('Movie_Based_on_Genre.csv')

	print("Display Statistics Based on Genre :[Yes/NO]")
	inp = input()
	if inp == "Yes":
		print("\nPercent of total entries are attributed to each genre:\n")
		genre_pcts = np.zeros(len(individual_genres))
		i = 0
		for genre in individual_genres:
			current_genre = moviedf['Genre'].str.contains(genre).fillna(False)
			pct = len(moviedf[current_genre]) / 1000 * 100
			genre_pcts[i] = pct
			i += 1
			print(genre," : ",pct)

		print("\nPercent of Revenue attributed to each genre:\n")
		genre_revenue_pcts = np.zeros(len(individual_genres))
		i = 0
		for genre in individual_genres:
			current_genre = moviedf['Genre'].str.contains(genre).fillna(False)
			revenue_pct = moviedf[current_genre].xs('Revenue (Millions)', axis=1).sum() / moviedf['Revenue (Millions)'].sum() * 100
			genre_revenue_pcts[i] = revenue_pct
			i += 1
			print(genre, revenue_pct)

	else:
		pass


elif choice == 3:
	print("Enter Actor/Actress name who acted in the Movie you wish to watch :")
	name = input()
	bolvalue = moviedf['Actors'].str.contains(name)
	Actorslist = moviedf[bolvalue].values
	if len(Actorslist) == 0:
	 	print("Sorry, Movie acted by",name," not present in our Database !")
	 	quit()
	else:
		print("\n")
		for act in Actorslist:
			for i in range(len(Displaydata)):
				print(Displaydata[i],":   ",act[i]) 
			print("\n")
	
	moviedf[bolvalue].to_csv('Movie_Based_on_Actors.csv')


elif choice == 4:
	print("Enter Director's name who directed the Movie you wish to watch :")
	name = input()
	bolvalue = moviedf['Director'].str.contains(name)
	Directorlist = moviedf[bolvalue].values
	print("\n")
	if len(Directorlist) == 0:
	 	print("Sorry, Movie Directed by",name," not present in our Database !")
	 	quit()
	else:
		for dirr in Directorlist:
			for i in range(len(Displaydata)):
				print(Displaydata[i],":   ",dirr[i])
			print("\n")
	
	moviedf[bolvalue].to_csv('Movie_Based_on_Director.csv')

	print("Display Statistics Based on Director\'s :[Yes/NO]")
	inp = input()
	if inp == "Yes":

		print("\nThe most active directors, 'most active' being defined as number of films with their name on it\n")
		most_active_directors = moviedf['Director'].value_counts().head(10)
		print(most_active_directors.index.values)
		
		print("\nRevenue each of these top 10 directors films brought in as a sum in millions :\n")
		director_revenue_totals = np.zeros(len(most_active_directors))
		i = 0
		for director in most_active_directors.index:
			current_director = moviedf['Director'].str.contains(director).fillna(False)
			director_film_revenue = moviedf[current_director].xs('Revenue (Millions)', axis=1).sum()
			director_revenue_totals[i] = director_film_revenue
			i += 1
			print(director," : ",director_film_revenue)
	else:
		pass


elif choice == 5:
	print("Enter the Ratings(Out of 10) above which you want to watch the movie :")
	val = float(input())
	bolvalue = moviedf['Rating']>val
	Ratinglist = moviedf[bolvalue].values
	print("\n")
	for rat in Ratinglist:
		for i in range(len(Displaydata)):
			print(Displaydata[i],":   ",rat[i]) 
		print("\n")
	
	moviedf[bolvalue].to_csv('Movie_Based_on_Ratings.csv')


elif choice == 6:
	print("Enter the Revenue (Millions) above which you want to watch the movie :")
	val = float(input())
	bolvalue = moviedf['Revenue (Millions)']>val
	Revenuelist = moviedf[bolvalue].values
	print("\n")
	for rev in Revenuelist:
		for i in range(len(Displaydata)):
			print(Displaydata[i],":   ",rev[i]) 
		print("\n")
	
	moviedf[bolvalue].to_csv('Movie_Based_on_Revenue.csv')

