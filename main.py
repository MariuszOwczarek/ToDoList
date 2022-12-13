from todo_cls import Todolist, Status

if __name__ == "__main__":
    program_status = True

    while program_status:
        operation = input(f'Please choose operation (Create/Read/Update/Delete or Exit): ')
        if operation.lower() == Status.Create.value:
            # Getting User Input for NEW task
            user_input = input(f'Create NEW Task, add it to the list (Number, Subject, Date, Status): ')
            user_input = user_input.split(",")
            # Creating an Instance
            Todolist(int(user_input[0].lstrip().rstrip()), user_input[1].lstrip().rstrip(),
                     user_input[2].lstrip().rstrip(),
                     user_input[3].lstrip().rstrip())
            Todolist.save()
        elif operation.lower() == Status.Read.value:
            Todolist.read()
        elif operation.lower() == Status.Update.value:
            user_input = input(f'Update Task from the list (Number, Subject, Date, Status): ')
            user_input = user_input.split(",")

            # Creating an Instance
            number = user_input[0]
            Todolist.update(int(number),
                            user_input[1].lstrip().rstrip(),
                            user_input[2].lstrip().rstrip(),
                            user_input[3].lstrip().rstrip())

        elif operation.lower() == Status.Delete.value:
            user_input = input(f'Delete Task from the list (Number): ')
            Todolist.delete(int(user_input))
        elif operation.lower() == Status.Exit.value:
            program_status = False
