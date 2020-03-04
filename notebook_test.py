from notebook import Note, Notebook

n = Notebook()
n.new_note('hello world')
n.new_note('hello again')
print(isinstance(n, object))
print(isinstance(n, Notebook))
print(isinstance(n.notes, list))
print('methods:', dir(n.notes))
print(isinstance(n.notes[0].id, int))
print(n.notes[0].memo)
n.modify_memo(1, 'hi world')
print(n.notes[0].memo)