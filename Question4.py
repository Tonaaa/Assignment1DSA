class Node(object):

    def __init__(self, my_list, item):
        self.my_list = my_list
        self.item = item

    def __call__(self):
        return

    def undo(self):
        return


class New_node(Node):
    def __call__(self):
        self.my_list.append(self.item)
        self.my_list.sort()

    def undo(self):
        self.my_list.remove(self.item)
        self.my_list.sort()


class Delete_node(Node):
    def __call__(self):
        self.deleted = False
        if self.item in self.my_list:
            self.my_list.remove(self.item)
            self.my_list.sort()
            self.deleted = True

    def undo(self):
        if self.deleted:
            self.my_list.append(self.item)
            self.my_list.sort()


class UndoableList(object):
    def __init__(self):
        self.undo_operation = []
        self.redo_operation = []

    def undo_insert(self, task):
        self.undo_operation.append(task)

    def undo_delete(self):
        try:
            final_undo_operation = self.undo_operation.pop()
        except IndexError:
            return "Nothing to undo"
        return final_undo_operation

    def redo_insert(self, task):
        self.redo_operation.append(task)

    def redo_delete(self):
        try:
            final_redo_operation = self.redo_operation.pop()
        except IndexError:
            return "Nothing to redo"

        return final_redo_operation

    def do(self, task):
        task()
        self.undo_insert(task)
        self.redo_operation[:] = []

    def undo(self):
        if len(self.undo_operation) != 0:
            task = self.undo_delete()
            task.undo()
            self.redo_insert(task)
        else:
            print('Nothing to undo')

    def redo(self):
        if len(self.redo_operation) != 0:
            task = self.redo_delete()
            task()
            self.undo_insert(task)
        else:
            print('Nothing to redo')


the_list = [2, 5, 7]
print(f'\nList: {the_list}')
driver_list = UndoableList()

driver_list.do(New_node(the_list, 6))
print(f'Insert(6): {the_list}')

driver_list.do(Delete_node(the_list, 5))
print(f'Delete(5): {the_list}')

driver_list.undo()
print(f'Undo: {the_list}')

driver_list.redo()
print(f'Redo: {the_list}')

driver_list.undo()
print(f'Undo: {the_list}')

driver_list.undo()
print(f'Undo: {the_list}')

driver_list.undo()
print(f'Undo: {the_list}')
