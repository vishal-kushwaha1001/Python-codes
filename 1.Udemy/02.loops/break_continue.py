# break is used to completely stop the loop.
# continue skips the current iteration and moves to the next iteration.


# pass is a null statement. It means:
    # "Do nothing for now."

# It is useful when Python requires a statement, but you don't want to execute any code yet.

for i in range(1, 10):
    if i == 2:
        continue      # skip 2
    if i == 7:
        break         # stop at 7
    print(i)