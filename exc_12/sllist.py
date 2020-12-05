from dataclasses import dataclass

@dataclass
class SomeValue:
    v: str

@dataclass
class SingleLinkedListNode:
    value: SomeValue
    nxt : "SingleLinkedListNode" = None



begin = SingleLinkedListNode(SomeValue("hehe"))
two = SingleLinkedListNode(SomeValue("haaaa"))
begin.nxt = two
two.nxt = SingleLinkedListNode(SomeValue("next"))

print(two)

