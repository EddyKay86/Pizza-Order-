print("Welcome to pizza hub")
print("Proceed to order")
size=input("Enter pizza size:'s','m,'l':") 
add_peperonni=input("like peperonni?:")
add_cheese=input("like cheese?:")
small=20
medium=25
large=30
peperonnismall=4
peperonniml=6
cheese=2
bill=0
if size=="s":
    bill=small
    if add_peperonni=="y":
        bill=bill+peperonnismall
    if add_cheese=="y":
        bill=bill+cheese
    print(f"Your bill is ${bill}")
elif size=="m":
    bill=medium
    if add_peperonni=="y":
        bill=bill+peperonniml
    if add_cheese=="y":
        bill=bill+cheese
    print(f"Your bill is ${bill}")
elif size=="l":
    bill=large
    if add_peperonni=="y":
        bill=bill+peperonniml
    if add_cheese=="y":
        bill=bill+cheese
    print(f"Your bill is ${bill}")
else:
    print("Enter a valid size")
