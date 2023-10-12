import time

from django.db import connection


class Benchmark:
    def __init__(self, description=None, logger=None, benchmark_queries=False):
        self._initial_time = time.perf_counter()
        self.benchmark_queries = benchmark_queries
        if self.benchmark_queries:
            self._initial_queries = len(connection.queries)
        self._logger = logger if logger else print
        self.description = "Did stuff" if description is None else description

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        if self.benchmark_queries:
            _queries_end = len(connection.queries)
            total_query_time = sum(float(q["time"]) for q in connection.queries[self._initial_queries :])
        _end = time.perf_counter()
        total_time = _end - self._initial_time
        if self.benchmark_queries:
            self._logger(
                f"{self.description} in {total_time:.3f} seconds "
                f"and {_queries_end - self._initial_queries} queries "
                f"({total_query_time:.3f} seconds total query time)"
            )
        else:
            self._logger(f"{self.description} in {total_time:.3f} seconds ")