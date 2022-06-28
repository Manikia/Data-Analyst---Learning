## Data Analyst Lesson

### NumPy
NumPy gives you an enormous range of fast and efficient ways of creating arrays and manipulating numerical data inside them
[Documentation](https://numpy.org/devdocs/user/absolute_beginners.html)

- To create a variable array we do:
    ```py
        array = np.array([4,5,6,7,10])
    ```
- To create a 2x2 array we do:
```py
    array = np.array([[4,5],[7,10]])
```
- To get the mean value of the array we do:
```py
    np.mean(array)
```
- To find the axis mean for all the rows of array:
```py
    np.mean(array, axis = 1)
```
- To find the axis mean for the columns of array:
```py
    np.mean(array, axis = 0)
```
### Pandas Library
- Series is a one dimensional array holding data of any type
```py
    series.dtype # this shows the type of the array series
    series.size #shows the amount of elements in the object
```
- Type 'O' means its a non numeric type
- We can assign a name to an object so we can reference it later on
```py
    product_categories.name = "Product Categories"
    #now when we print it will show the new name
    print(product_categories.name)
```
- The attributes related to a certain python object allow us to extract information about it but arent meant to alter or modify its content
- Series have index values that point to the integer values
- Series should be treated as its own index and if we call it it will show it as its own indexes
```py
    prices_per_category.index
```
## Label Based vs Position Based Indexing
- The numbers on the left refer to the posiotion within the order sequence on the right which means that it will be a rangeIndex which is Position Indexing
![Position Index](images\positionIndex.jpg)
- This is also known as a Zero based index
- To not get confused people look at the index position instead of the actual position of a variable
- To know if we are working with a range indesx object we can check its type by doing
```py
    type(series_a.index)
    #to show what index it has we do
    list(series_a.index)
```
- Label based index is where you label your index based on what it is instead of a numeric position
- Basically there are two types of Indexing: Explicit and Implicit
- Explicit indexing:
    - Explicit are created explicitly and have the use of the index in queries which are the same
    - Explicit indexing also means that we set the dictionary to a variable
    Ex:
    ```py
        prices_per_category = pd.series({'Product A': 22250,'Product B': 22250, 'Product C': 22250})
    ```
- Implicit indexing:
    - Used to refer to indexes that are created by operations other than 'create index'. It usually occurs when using primary keys or using unique constants
- If an index is not defined then a zero based index will be set
- Implicit is used with the first example concerning the index positions instead of a label and explicit is shown in the second example with the dictionaries name instead of a position name
- To set an index number instead of the default 0 we can do:
```py
    series_b = pd.series([10,20,30,40,50], index = [1,2,3,4,5])
    #in the above it will set the index numbers starting from 1 and going up to 5 for each other series which means it treats it as an index label
```
- When we use strings though we can do zero indexing and it wont return an error likr the second to previous would
### Using Methods
- 