# Blake Mann
# PSID: 1832387
# 14.11

# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        small_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[small_index]:
                small_index = j
        temp = numbers[i]
        numbers[i] = numbers[small_index]
        numbers[small_index] = temp
        for x in numbers:
            print(x, end=" ")
        print()
        #print(' '.join([str(x) for x in numbers]))

    return numbers



if __name__ == "__main__":
    num_list = [int(value) for value in input().split()]
    selection_sort_descend_trace(num_list)
    numbers = []







