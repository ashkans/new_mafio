from base.managers import QuerySet


class GameQuerySet(QuerySet):

    def search(self, query):
        """
        Search Game objects by name
        """
        if query:
            # TODO implement this method, since this is an example
            return self.filter(
                name__unaccent__icontains=query
            )
