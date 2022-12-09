import random


class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    @staticmethod
    def print_comas(array):
        output = ""
        for i in range(0, len(array)):
            if i == len(array) - 1:
                output += str(array[i])
            else:
                output += str(array[i]) + ", "

        print(output)

    @staticmethod
    def create_array(number_of_array_elements, value_of_array_elements):
        arr = []
        for i in range(0, number_of_array_elements):
            arr.append(value_of_array_elements)
        return arr

    @staticmethod
    def create_array2(number_of_array_elements, value_from, value_to):
        arr = []
        for i in range(0, number_of_array_elements):
            arr.append(random.randint(value_from, value_to))

        return arr

    @staticmethod
    def values_in_range(array, value_from, value_to):
        amount = 0
        for i in array:
            if i >= value_from and i <= value_to:
                amount += 1

        print(amount)


arr1 = Arrays.create_array(10, 4)
arr2 = Arrays.create_array2(20, -7, 8)
Arrays.print_comas(arr1)
Arrays.print_comas(arr2)
Arrays.values_in_range(arr2, -1, 1)
