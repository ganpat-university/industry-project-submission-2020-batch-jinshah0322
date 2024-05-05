class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = {
            1: "Movie 1",
            2: "Movie 2",
            3: "Movie 3",
        }
        self.booked_tickets = {movie_id: 0 for movie_id in self.movies}

    def display_movies(self):
        print("Available Movies:")
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def book_tickets(self, movie_id, num_tickets):
        if movie_id in self.movies:
            available_tickets = 10 - self.booked_tickets[movie_id]
            if num_tickets <= available_tickets:
                self.booked_tickets[movie_id] += num_tickets
                print(f"Booking successful! {num_tickets} tickets booked for {self.movies[movie_id]}.")
            else:
                print("Sorry, not enough tickets available.")
        else:
            print("Invalid movie ID.")

booking_system = MovieTicketBookingSystem()

while True:
    print("\nMovie Ticket Booking System")
    print("1. Display Available Movies")
    print("2. Book Tickets")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        booking_system.display_movies()
    elif choice == '2':
        movie_id = int(input("Enter the movie ID to book tickets: "))
        num_tickets = int(input("Enter the number of tickets to book: "))
        booking_system.book_tickets(movie_id, num_tickets)
    elif choice == '3':
        print("Exiting the Movie Ticket Booking System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")