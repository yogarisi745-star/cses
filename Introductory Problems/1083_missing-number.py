
def solve() -> None:
    n=int(input())
    input_data = list(map(int, input().split()))
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(input_data)
    print(expected_sum - actual_sum)
if __name__ == "__main__":
    solve()


# to find missing no -subtract the sum of the given numbers from the sum of first n natural numbers.
