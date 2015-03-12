def main():
    tests = input()

    for i in range(tests):
        power_strips = input()
        numbers = raw_input().split()

        if len(numbers) == power_strips:
            outlets = 1
            for j in numbers:
                outlets += (int(j) - 1)

            print(outlets)

if __name__ == "__main__":
    main()
