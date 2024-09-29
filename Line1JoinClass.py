import typing

class Joiner:
    def __init__(self, obj: object) -> None:
        self.obj = obj
        self.Returns = {}
        self.safe_builtins = {
    'abs': abs,
    'all': all,
    'any': any,
    'ascii': ascii,
    'bin': bin,
    'bool': bool,
    'bytearray': bytearray,
    'bytes': bytes,
    'chr': chr,
    'classmethod': classmethod,
    'compile': compile,
    'complex': complex,
    'copyright': copyright,
    'credits': credits,
    'delattr': delattr,
    'dict': dict,
    'dir': dir,
    'divmod': divmod,
    'enumerate': enumerate,
    'filter': filter,
    'float': float,
    'format': format,
    'frozenset': frozenset,
    'getattr': getattr,
    'globals': globals,
    'hasattr': hasattr,
    'hash': hash,
    'help': help,
    'hex': hex,
    'id': id,
    'input': input,  # 注意: inputは使用には注意が必要
    'int': int,
    'isinstance': isinstance,
    'issubclass': issubclass,
    'iter': iter,
    'len': len,
    'list': list,
    'map': map,
    'max': max,
    'min': min,
    'next': next,
    'object': object,
    'oct': oct,
    'ord': ord,
    'pow': pow,
    'print': print,
    'property': property,
    'range': range,
    'repr': repr,
    'reversed': reversed,
    'round': round,
    'set': set,
    'setattr': setattr,
    'slice': slice,
    'sorted': sorted,
    'str': str,
    'sum': sum,
    'tuple': tuple,
    'type': type,
    'vars': vars,
    'zip': zip,
        }

    def SetItem(self, ItemName: str, Value: typing.Any) -> 'Joiner':
        setattr(self.obj, ItemName, Value)

        return self
    
    def GetItem(self, ItemName: str, ReturnID: str = None) -> 'Joiner':
        if ReturnID is None:
            return self
        self.Returns[ReturnID] = getattr(self.obj, ItemName)

        return self
    
    def HasItem(self, ItemName: str, ReturnID: str = None) -> 'Joiner':
        if ReturnID is None:
            return self
        self.Returns[ReturnID] = hasattr(self.obj, ItemName)

        return self
    
    def RetVal(self) -> dict:
        return self.Returns
    
    def Eval(self, code: str, ReturnID: str = None) -> 'Joiner':
        if ReturnID is None:
            exec(code, {"self": self, "__builtins__": self.safe_builtins}, {})
            return self
        self.Returns[ReturnID] = eval(code, {"self": self, "__builtins__": self.safe_builtins}, {})

        return self
    
    def Call(self, ReturnID: str = None, args: tuple = ()) -> 'Joiner':
        if ReturnID is None:
            self.obj(*args)
            return self
        
        self.Returns[ReturnID] = self.obj(*args)
        return self
    
    def CallMethod(self, ReturnID: str = None, FunctionName: str = "__call__", args: tuple = ()) -> 'Joiner':
        if ReturnID is None:
            getattr(self.obj, FunctionName)(*args)
            return self

        self.Returns[ReturnID] = getattr(self.obj, FunctionName)(*args)

        return self
    
    def SVWGOL(self, VarName: str, Type: typing.Union[globals, locals]) -> 'Joiner':
        """Variable Save With Globals or Locals"""
        Type()[VarName] = self.RetVal()

        return self
