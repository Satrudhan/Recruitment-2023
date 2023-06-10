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

 - Line 5: Use of cat to open the users.txt file along with the piping, matching the userid using and grep and print it and finally use of wc -l to count the each line containing the matching userid. And store in count.
 ```
 count=$(cat users.txt | grep "$i" | wc -l)
 ```
- Line 6: Print the count of userid.
```
echo "Count of userid $i: $count"
```


### Full code 
```
#!/bin/bash
userid=(553 828 723 698)
for i in "${userid[@]}"
do 
    count=$(cat users.txt | grep "$i" | wc -l)
    echo "Count of userid $i: $count"
done

count=$(cat users.txt | grep -E '553|828|723|698' | wc -l)
echo "Count of userid : $count"
```
### Output:
```
$ ./script.sh 
Count of userid 553: 2
Count of userid 828: 1
Count of userid 723: 1
Count of userid 698: 3
Count of userid : 7

```