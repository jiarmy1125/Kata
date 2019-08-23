# likes([]), 'no one likes this'
# likes(['Peter']), 'Peter likes this'
# likes(['Jacob', 'Alex']), 'Jacob and Alex like this'
# likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'
# likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this'

def likes(names):
    if len(names) == 0:
        return ('no one likes this')

    elif len(names) == 1:
        return (names[0] + ' likes this')

    elif len(names) == 2:
        return (names[0] + ' and ' + names[1] + ' like this')

    elif len(names) == 3:
        return (names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')

    elif len(names) > 3:
        a=len(names)-2
        return (names[0] + ', ' + names[1] + ' and ' + str(a) + ' others like this')




likes([]), 'no one likes this'
likes(['Peter']), 'Peter likes this'
likes(['Jacob', 'Alex']), 'Jacob and Alex like this'
likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this'
likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this'