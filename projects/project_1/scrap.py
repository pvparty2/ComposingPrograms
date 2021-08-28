def make_averaged(fn, num_samples=1000):
    def averaged(*args):
        s = [fn(*args) for _ in range(num_samples)]
        for i in s:
            print(i)
        return sum(s)/num_samples
    return averaged