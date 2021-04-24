from notebook import Note
from notebook import NoteBook


sentence1 = "hi"
note1 = Note(sentence1)

sentence1 = "hello"
note2 = Note(sentence1)

sentenct1 = "how are you?"
note3 = Note(sentence1)

print(note1)
note1.remove()
print(note1)

sentence2 = NoteBook("대화")
sentence2.add_note(note1)
sentence2.add_note(note2)
print(sentence2.get_number_of_pages())

sentence2.add_note(note1, 100)
for i in range(300):
    sentence2.add_note(note1, i)

print(sentence2.get_number_of_pages())
