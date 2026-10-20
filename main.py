
from bs4 import BeautifulSoup
import requests
import csv

# URL of the IMDb Top 250 Movies page
url = "https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.prettify())
    movies = soup.select(selector="table a")
    year_span = soup.select(selector= "table .meta-year")
    years = [year.getText().replace("(", "").replace(")", "") for year in year_span]
    with open('movies.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Title", "Year", "URL"])
        for index, movie in enumerate(movies):
            movie_href = movie.get("href")
            movie_title = movie.getText()
            csv_writer.writerow([movie_title, years[index], movie_href])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")