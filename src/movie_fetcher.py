import requests
import re
import csv
from bs4 import BeautifulSoup


class MovieScraper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.movies = []

    def get_movies(self):
        self.response = requests.get(self.url)
        soup = BeautifulSoup(self.response.text, 'lxml')
        self.movies = soup.select('td.titleColumn')

    def extract_movie_data(self, movie):
        movie_string = movie.get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(self.movies.index(movie))) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(self.movies.index(movie))) - (len(movie))]
        links = [a.attrs.get('href') for a in movie.select('a')]
        crew = [a.attrs.get('title') for a in movie.select('a')]
        ratings = [b.attrs.get('data-value') for b in movie.select('span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in movie.select('strong')]

        return {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[0],
                "rating": ratings[0],
                "vote": votes[0],
                "link": links[0],
                "preference_key": self.movies.index(movie) % 4 + 1}


class MovieExporter:
    def __init__(self, filename, fields):
        self.filename = filename
        self.fields = fields

    def export_to_csv(self, movies):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            for movie in movies:
                writer.writerow(movie)


def main():
    movie_scraper = MovieScraper('http://www.imdb.com/chart/top')
    movie_scraper.get_movies()
    movie_data = [movie_scraper.extract_movie_data(movie) for movie in movie_scraper.movies]

    fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
    movie_exporter = MovieExporter("movie_results.csv", fields)
    movie_exporter.export_to_csv(movie_data)


if __name__ == '__main__':
    main()
