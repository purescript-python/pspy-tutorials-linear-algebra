from typing import TypeVar, Callable, List, Dict, TYPE_CHECKING
from typing_extensions import Protocol
from typing import Optional


T = TypeVar("T", covariant=True)
H = TypeVar("H")
G = TypeVar("G")

class Mappable(Protocol[T]):
    def map(self, f: Callable[[T], G]) -> 'Mappable[G]':
        ...

def map_int_elts_to_str(x: Mappable[int]):
    y = x.map(str)
    if TYPE_CHECKING:
        reveal_locals()
    return y

class MyList(List[H]):
    def map(self, f: Callable[[H], G]) -> MyList[G]:
        ret = MyList[G]()
        append = MyList.append
        for each in self:
            append(ret, f(each))
        return ret

def test() -> None:
    z = map_int_elts_to_str(MyList([1, 2, 3]))
    k = z[0]
    if TYPE_CHECKING:
        reveal_locals()