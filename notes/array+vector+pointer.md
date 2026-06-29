Array 1D and 2D
1D standard [0, 0, 0, 0]

2D images I think

All in CONTIGUOUS MEMORY - Where data occupies a continuous set of blocks

Vectors
Automatically updating arrays which double in size

Capacity = 4

Current size = 3

if size is increased by one then capacity is * 2

Pointers store the address of another variable, not the variable

| Operator | Meaning                                  | Example |
| -------- | ---------------------------------------- | ------- |
| `&`      | Get the address of a variable            | `&x`    |
| `*`      | Go to an address and get the value there | `*ptr`  |

int x = 42;
int *ptr = &x;

