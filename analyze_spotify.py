import ast
import csv
import itertools
#
rows = []
with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)

summ = 0
count = 0

liv_summ = 0
liv_count = 0
explicit_count = 0

artists = {}
years = {}
genres = {}

for row in rows:
    if row[2] == "True":
        explicit_count += 1
    count += 1
    summ += float(row[5])
    energy = float(row[7])
    if energy > 0.5:
        liv_count += 1
        liv_summ += float(row[11])

    if row[0] not in artists:
        artists[row[0]] = 0
    else:
        artists[row[0]] += 1

    year = int(row[3][0:4])
    if year not in years:
        years[year] = 0
    else:
        years[year] += 1

    cur_genres = ast.literal_eval(row[4])
    for cur in cur_genres:
        itertools.count()
        if cur not in genres:
            genres[cur] = 0
        else:
            genres[cur] += 1



artists = sorted(artists.items(), key=lambda x: x[1], reverse=True)
years = sorted(years.items(), key=lambda x: x[1], reverse=True)
genres = sorted(genres.items(), key=lambda x: x[1], reverse=True)

print(f"Average danceability: {summ/count}")
print(f"Average liveliness with energy > 0.5f: {liv_summ/liv_count}")
print(f"Explicit count: {explicit_count}")
print(f"Top artist: {artists[0]}")
print(f"Top year: {years[0]}")
print(f"Top genre 1: {genres[0]}")
print(f"Top genre 2: {genres[1]}")
print(f"Top genre 3: {genres[2]}")



