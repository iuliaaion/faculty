from typing import List, Tuple
from collections import Counter

from entities.rental_entity import Rental
from entities.movie_entity import Movie


class RentalRepository:
    """object that manages Rental entities."""


    def __init__(self):
        self.__rentals = {}
        self.__movie_stats_days = Counter()
        self.__movie_stats_times = Counter()
        self.__count = 0


    def insert(self, r: Rental) -> id:
        """Inserts rental.

         If added for the first time, an id will be assigned.
         """

        if not hasattr(r, 'id'):
            r.id = self.__count
            self.__count += 1
            self.update_stats_times(r.movie, 1)

        else:
            # Update op, i.e. movie was returned
            self.update_stats_days(r.movie, self.calc_rental_days(r))

        self.__rentals[r.id] = r


    def get(self, id: int):
        """"Get rental by id."""

        return self.__rentals[id]


    def get_all(self) -> List[Rental]:
        """Return all entities."""

        return list(self.__rentals.values())


    def get_stats_days(self) -> List[Tuple[Movie, int]]:
        """Return rental stats by number days rented."""

        return list(self.__movie_stats_days.items())


    def get_stats_times(self) -> List[Tuple[Movie, int]]:
        """Return rental stats by number times rented."""

        return list(self.__movie_stats_times.items())


    def calc_rental_days(self, r: Rental) -> int:
        """Calculate how many days a rental was made for."""

        assert r.returned_date is not None

        return (r.returned_date - r.rented_date).days


    def update_stats_times(self, movie: Movie, times: int):
        """Method used to update times stats for a movie.

        A method approach was used in order to allow the undo/ redo observer
        to modify stats values.
        """

        self.__movie_stats_times[movie] += times


    def update_stats_days(self, movie: Movie, days: int):
        """Method used to update times stats for a movie.

        A method approach was used in order to allow the undo/ redo observer
        to modify stats values.
        """

        self.__movie_stats_days[movie] += days
