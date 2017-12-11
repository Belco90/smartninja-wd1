print "Welcome to the TODO task management program."

todo = {}

while True:
    new_task = raw_input("Please enter a TODO task: ")
    done = raw_input("Is that task done? (yes/no)")

    todo[new_task] = done == 'yes'

    new = raw_input("Would you like to enter new task? (yes/no) ")

    if new == "no":
        break


print "All tasks:"

print "Completed:"
for task in todo:
    if todo[task]:
        print task

print "Incompleted:"
for task in todo:
    if not todo[task]:
        print task

print "END"


