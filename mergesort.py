#!/usr/bin/python3.6

# Author : Wael Bahloul
# This is the mergesort algorithm, implemented as one class
# the algorithm is tested from the manin function with different
# test data (small set, large set, sorted , partially sorted ... etc)

import random

class MergeSort:

  def mergesort0(self, num):
    self.mergesort(num, 0, len(num)-1)
    return (num)

  def mergesort(self, num, low, high):
    if low < high:
      mid = (low + high) // 2
      self.mergesort(num, low, mid)
      self.mergesort(num, mid+1, high)
      self.merge(num, low, mid, mid+1, high)

  def merge(self, a, l1, u1, l2, u2):
    temp = [0]*len(a)
    i = l1
    j = l2
    k = l1
    while (i <= u1 and j <= u2):
        if (a[i] <= a[j]):
            temp[k] = a[i]
            i = i + 1
        else:
            temp[k] = a[j]
            j = j + 1

        k = k + 1
    while ( i <= u1 ):
        temp[k] = a[i]
        k = k + 1
        i = i + 1
    while ( j <= u2 ):
        temp[k] = a[j]
        k = k + 1
        j = j + 1

    h = l1

    while ( h <= u2 ):
        a[h] = temp[h]
        h = h + 1


def main():
   #create instance
   mg = MergeSort()
   array = [2, 98, 3, 14, 5, 65, 1]
   print ("\nOriginal Array is:")
   print ("\n",array)
   print("\nThe Sorted Array is:")
   h = mg.mergesort0(array)
   print(" ", h)

   #large set
   mg = MergeSort()
   array = list(reversed(range(1, 100)))
   print ("\nOriginal Array is:")
   print ("\n",array)
   print("\nThe Sorted Array is:")
   h = mg.mergesort0(array)
   print(" ", h)


   #Sorted set
   mg = MergeSort()
   array = list(range(1, 10))
   print ("\nOriginal Array is:")
   print ("\n",array)
   print("\nThe Sorted Array is:")
   h = mg.mergesort0(array)
   print(" ", h)


   #Random List
   mg = MergeSort()
   array = random.sample(range(1,21), 20)
   print ("\nOriginal Array is:")
   print ("\n",array)
   print("\nThe Sorted Array is:")
   h = mg.mergesort0(array)
   print(" ", h)

   #Partially Sorted
   mg = MergeSort()
   array1 = random.sample(range(51,100), 49)
   array2 = list(range(1, 51))
   array = array2 + array1
   print ("\nOriginal Array is:")
   print ("\n",array)
   print("\nThe Sorted Array is:")
   h = mg.mergesort0(array)
   print(" ", h)


if __name__ == "__main__":
  main()

