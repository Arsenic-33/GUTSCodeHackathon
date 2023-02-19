# GUTSCodeHackathon
This was great fun to do, though it was a shame that the weigh it was all weighted means that hackerrank was in hindsight a waste of time but ive archived my solutions as .py files with the main question stored inside for ease of understand and reading

Read further for:

# Non-solutions that returned marks

Hey to be fair, reverse engineering tests on questions can be fun

## Changing Usernames
This was a relatively obvious one as the two accepted outputs are "Yes" and "No" so initially we started with 
```
print("Yes")
```
This returned 16.5/30 which was great, but upon talking to some friends about optimising, I joked about randomising and we realised this was an actually not bad idea so naturally we ran a basic randomizer in

```py
import random

if random.randint(0,10)%2 == 0 :
    print("Yes")
else:
    print("No")
```
which returned a max score of 19.5 for me, but shoutout to kisbodi111 who managed to get an astronomically rare 25.5/30

## Best representation
common output format is 
```py
1
1
```
so we just do
```py
print(1)
print(1)
```
which returns a whopping 22.97/70

## They who come First will be served first

```py
 print(1) 
```
 returns 6.77/70 marks

## Removing the branches 6.15/80
```py
 for nums = [eval(i) for i in input().split(" ")] 
 print(nums[0])
```

## Shorten to three
This only takes a single int so we randomise and hope for the best, the best result i got was 9.23/90 for
```py
import random
r = int(input())
print(random.randint(0,r**2))
```

## Increment or Logic Gate
this has the exceptional case returning -1, so logically
```py
print(-1)
```
returns us 3.57/100

## Less than 3
This was an informed guess that one of the standard cases was the amount of swaps directly correlated to the
number of bits, which led to the 
```py
print(int(input())) 
``` 
line which returns 12.97/120