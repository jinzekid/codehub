import tempfile, os, cProfile, pstats

def profile(column='time', list=5):
    def _profile(function):
        def __profile(*args, **kw):
            s = tempfile.mktemp()
            profiler - cProfile.Profile()
            profiler.runcall(function, *args, **kw)
            profiler.dump_stats(s)
