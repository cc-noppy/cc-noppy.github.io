
def my_pow(x, n):
    def fast_pow(base, exp):
        if exp == 0:
            return 1
        half = fast_pow(base, exp // 2)
        return half * half if exp % 2 == 0 else half * half * base

    return fast_pow(x, n) if n >= 0 else 1 / fast_pow(x, -n)
