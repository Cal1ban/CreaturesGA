from py2neo import Node, Relationship, Graph
from random import randrange

g = Graph()

g.run("""MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r""")

people = ["Jake", "Emily", "Alex"]
people_two = ["Emily", "Alex", "Jake"]
pairs = zip(people, people_two)

for pair in pairs:
    tx = g.begin()
    a = Node("Person", name=pair[0])
    b = Node("Person", name=pair[1])
    ab = Relationship(a, "KNOWS", b, weight=randrange(0, 1))
    tx.create(a)
    tx.create(b)
    tx.create(ab)
    tx.commit()

print(g.run("""
    MATCH (a:Person {name :'Jake'})-[relab:KNOWS]->(b:Person), -[]->()
    RETURN a.name, b.name
""").data())
