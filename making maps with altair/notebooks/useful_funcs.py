## Useful functions for this project

# from Real Python's blog post on the pathlib module
### https://realpython.com/python-pathlib/#display-a-directory-tree
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')