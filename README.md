# Scripts to invoke/show and test how the system can be used 


```python

```


```python
# allows for 3 files and 1 gorup name to be sent
# the codebase statically sets file_path
```


```python
import sqlite3

def check_db():
    conn=sqlite3.connect('db.sqlite3')
    query="SELECT * FROM IO_GROUP_DATA_ASSOC igda inner join IO_DATA_REGISTRY ida on ida.IO_DATA_ID = igda.IO_DATA_ID inner join IO_GROUP_REGISTRY igr on igr.IO_GROUP_ID=igda.IO_GROUP_ID"
    
    for row in conn.execute(query):
        print (row)
    conn.close()
```


```python
check_db()
```


```python
!curl "http://localhost:8000/orm-insert/?file1=1.parquet&file2=2.parquet&file3=3.parquet&group_name=input_group"
```

    {"message":"inserted Group name as input_group with 3 files"}


```python
check_db()
```

    (163, 163, 23, 163, '1.parquet', 'maprfs:///some/predefined/file/location', 23, 'input_group')
    (164, 164, 23, 164, '2.parquet', 'maprfs:///some/predefined/file/location', 23, 'input_group')
    (165, 165, 23, 165, '3.parquet', 'maprfs:///some/predefined/file/location', 23, 'input_group')



```python

```
