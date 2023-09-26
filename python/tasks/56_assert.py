from typing import Callable

def invert(func: Callable) -> None:
      def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                  result = list(map(lambda item: item * (-1), result))
            else:
                  raise RuntimeError()
            return result
      return wrapper
            

@invert
def foo(lenght: int = 10) -> list:
    if lenght == 0:
          return [0]
    is_minus = lenght < 0
    # result = []
    # for i in range(abs(lenght)):
    #     if not i % 2:
    #         result.append(i if not is_minus else i * (-1))
    # return result
    return [ i if not is_minus else -i for i in range(abs(lenght)) if i % 2 == 0 ]
    
def test() -> None:
      # assert foo(10) == [0, 2, 4, 6, 8]
      assert foo(-4) == [0, 2]
      # print(foo(-2))
      assert foo(-2) == [0]
      assert foo(4) == [0, -2]


test()