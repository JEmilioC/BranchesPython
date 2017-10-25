book={}
book['emilio']={
    'name':'emilio',
    'address':'31 418 la loma',
    'phone':'2461251867'
}
book['jose']={
    'name':'jose',
    'address':'31 418 la loma',
    'phone':'2461251867'
}


import json
s=json.dumps(book)
# print(s)
with open("c://users/book.txt","w") as f:
    f.write(s)
