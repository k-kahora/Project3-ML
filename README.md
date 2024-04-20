# README
How to run our program

``` python
python3 program.py <input.csv> <output_tree.txt>
```

For example 

``` python
python3 program.py PlayTennisSampleDataFormat.txt out.txt
cat out.txt
```

To run all three at once

``` python
./runner.sh
```

To observe the output 

``` python
cat D2
cat D3
cat D4
```


# Files

__D2__, __D3__, __D4__ are all the output decision trees from running the algorithm on the three data sets.  __PlayTennisCustom.txt__ is the data set for __D4__, __D3__ is the tree for __PlayTennisSampleDataFormat.txt__, and __D1__ is the tree for __EnjoySport.txt__.  __D3-answer.txt__ is the answer for the question on Task3.  __program.py__ is the main program that runs ID3, __runner.sh__ runs all three datasets at once and overwrites __D1__, __D2__, and __D3__. __D5__ is the written deliverable D5.
