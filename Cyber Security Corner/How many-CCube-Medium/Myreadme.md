##   Task - 05: How many?
 - Line 1: It says that the script should be executed using the Bash shell.
 ```
 #!/bin/bash
 ```


 - Line 2: Storing the userid as list whose count is to be find.
```
userid=(553 828 723 698)
```


 - Line 3: In this for loop, the variable i will take on each value from the userid array, one at a time, and the loop body will be executed for each iteration.
```
for i in "${userid[@]}"
```


- line 4: open the txt file using cat along with piping and use of ``grep -w`` to match the exact pattern and use of ``cut -d`` to get the value at the fifth position.

```
value=$(cat users.txt | grep -w "User ID $i =" | cut -d " " -f5)
```
- finally: Storing the value to sum and printing th result.

### final code:
```
#!/bin/bash
userid=(553 828 723 698)
sum=0
for i in "${userid[@]}"
do 
    value=$(cat users.txt | grep -w "User ID $i =" | cut -d " " -f5)
    sum=$((sum + value))
done

echo "The sum is : $sum"

```
### OUTPUT:
```
$ The sum is : 2649
```