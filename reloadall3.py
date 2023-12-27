import types
from chapter25.reloadall import status, tryreload, tester


def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()
        if (type(next) == types.ModuleType and next not in visited):
            status(next)
            tryreload(next)
            visited.add(next)
            modules.extend(next.__dict__.values())


def reload_all(*modules):
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
