from queue import Queue


def main():
    person_id = 1
    user_in = -1
    queues = []
    num = int(input('How many queues? '))
    for i in range(num):
        prompt = 'What is the max size of queue ' + str(i + 1) + '? '
        size = int(input(prompt))
        queues.append(Queue(size))

    while user_in != 0:
        print('-' * 20)
        print("Welcome to QMS")
        print("1 - Add to queue")
        print("2 - Remove from queue")
        print("3 - Print queue")
        while user_in < 0 or user_in > 2:
            user_in = int(input("Select an option "))

        if user_in == 1:  # adding
            print("Insert a queue number to add person to queue.")
            queue_num = get_number(1, len(queues)) - 1
            queues[queue_num].insert("Person " + str(person_id))
            person_id += 1
        elif user_in == 2:  # removing
            print("Insert a queue to ")
        elif user_in == 3:  # printing
            print("Insert a queue number to print queue")
            queue_num = get_number(1, len(queues)) - 1
            print(queues[queue_num])

        user_in = -1  # reset user input


def get_number(minimum, maximum):
    number = minimum - 1
    while number < minimum or number > maximum:
        number = int(input("Enter number between {} and {}: ".format(minimum, maximum)))
        if number < minimum or number > maximum:
            print("That is an invalid number")
        return number


if __name__ == '__main__':
    main()
