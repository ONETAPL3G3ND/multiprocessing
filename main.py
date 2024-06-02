import multiprocessing

def calculate(number):
    for num in range(1, 178):
        number = number / num
    print(number)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    print("Building process")
    for number in numbers:
        process = multiprocessing.Process(target=calculate, args=(number,))
        processes.append(process)

    print("Starting process")
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("All processes complete")
