def bubble_sort(numbers, ascending=True):
    """Сортирует список чисел по возрастанию или убыванию с помощью алгоритма сортировки пузырьком."""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and numbers[j] > numbers[j + 1]) or (not ascending and numbers[j] < numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


if __name__ == "__main__":
    # Ввод чисел
    n = int(input("Введите количество чисел: "))
    numbers = []
    for _ in range(n):
        num = int(input("Введите число: "))
        numbers.append(num)

    # Выбор направления сортировки
    order = input("Введите направление сортировки (возрастание/убывание): ").strip().lower()
    if order == "возрастание":
        ascending = True
    elif order == "убывание":
        ascending = False
    else:
        print("Некорректный ввод. Будет выполнена сортировка по возрастанию.")
        ascending = True

    # Сортировка и вывод результата
    sorted_numbers = bubble_sort(numbers, ascending)
    print(f"Отсортированные числа: {sorted_numbers}")
