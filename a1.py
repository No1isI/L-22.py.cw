set1={1,3,76,67,89,45,6,2}
set2={65,76,43,5,6,3,6,47}
print('set1=', set1)
print('set2=', set2)

set3={32,64,46,'sakura is trash',106,67}
print('set3=', set3)
union=set1.union(set2)
print('Union=', union)

intersection= set1.intersection(set2)
print('intersection=', intersection)

difference=set1.difference(set2)
print('Difference=', difference)

#symetric_differenceunion_intersection
symmetric=set1.symmetric_difference(set2)
print('Symetric Difference=', symmetric)