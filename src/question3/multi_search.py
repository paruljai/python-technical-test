from .search import Search


class MultiSearch(Search):
    """Base class for combining the results of multiple Search objects."""

    searches = []

    def get_searches(self) -> list:
        """:return the Searches set on this MultiSearch."""
        return self.searches

    def set_searches(self, searches: list):
        """Sets the Search objects to be called for a MultiSearch.

        :param searches all Search implementations to be called for a search.
        """
        self.searches = searches

    def search(self, query: str) -> list:
        """Perform an multi Search against all set Searches, and returned the aggregated result set.

        :param query Search string.
        :return A combined List of search results from querying all Searches. Sort order is implementation-specific.
        """
        pass
