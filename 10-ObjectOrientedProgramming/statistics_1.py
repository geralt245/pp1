class Statistics:

    def __init__(self):
        self.numbers = []

    def add(self):
        number = int(input("Enter a number: "))
        self.numbers.append(number)

    def display_numbers(self):
        for i in range(0, len(self.numbers)):
            if i == len(self.numbers) - 1:
                print(self.numbers[i], end="")
            else:
                print(self.numbers[i], end=", ")

    def greatest_number(self):
        return max(self.numbers)

    def smallest_number(self):
        return min(self.numbers)

    def mean(self):
        sum = 0
        for i in self.numbers:
            sum += i
        return sum / len(self.numbers)

    def median(self):
        n = len(self.numbers)
        index = n // 2

        if n % 2:
            return sorted(self.numbers)[index]

        return sum(sorted(self.numbers)[index - 1:index + 1]) / 2

    def __str__(self):
        print()
        return f"Minimum: {str(self.smallest_number())}\nMaximum: {str(self.greatest_number())}\nMean: {str(self.mean())}\nMedian: {str(self.median())}"
