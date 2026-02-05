#1 example
stack = ["task1", "task2"]
stack.append("task3")
first = stack.pop(0)
print(f"Осталось задач: {len(stack)}") # 2
print(f"Текущий порядок: {stack}")    # ['task2', 'task3']
