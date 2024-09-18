def bubble_sort(numbers):
    """Сортирует список чисел по возрастанию с помощью алгоритма сортировки пузырьком."""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    # Пример использования
    n = int(input("Введите количество чисел: "))
    numbers = []
    for _ in range(n):
        num = int(input("Введите число: "))
        numbers.append(num)

    sorted_numbers = bubble_sort(numbers)
    print(f"Отсортированные числа: {sorted_numbers}")
