class Movie:
 def __init__(self, title, showtimes):
    self.title = title
    self.showtimes = showtimes

class Ticket:
 def __init__(self, movie, showtime):
    self.movie = movie
    self.showtime = showtime

class Customer:
 def __init__(self, name):
    self.name = name
    self.bookings = []

 def book_ticket(self, movie, showtime):
    ticket = Ticket(movie, showtime)
    self.bookings.append(ticket)
    return f"Booked ticket for {movie.title} at {showtime}."

class Cinema:
 def __init__(self):
    self.movies = []
    self.customers = []

 def add_movie(self, movie):
    self.movies.append(movie)

 def add_customer(self, customer):
    self.customers.append(customer)

 def view_showtimes(self, title):
    for movie in self.movies:
        if movie.title == title:
            return movie.showtimes
    return "Movie not found."

movie1 = Movie("Movie1", ["10:00", "14:00"])
movie2 = Movie("Movie2", ["11:00", "15:00"])

cinema = Cinema()
cinema.add_movie(movie1)
cinema.add_movie(movie2)

customer = Customer("Alice")

print(cinema.view_showtimes("Movie1"))

print(customer.book_ticket(movie1, "10:00"))