from fajlkezeles import make_list, list_to_str, print_to_file, read_from_file
from feladatok import num_of_negatives, largest_in_list, get_even_numbers_as_list, sum_of_nums_devisible_by_five, index_of_smallest_num

mylist:list = make_list()
listText = list_to_str(mylist)
print_to_file(listText)

mylist2:list = read_from_file()

print(f"Feladat 1:\n\tA listában {num_of_negatives(mylist2)} negatív sszám található")

print(f"\nFeladat 2:\n\tA listában {largest_in_list(mylist2)} a legnagyobb szám")

print(f"\nFeladat 3:\n\tA listában ezk a páros számok találhatók: {get_even_numbers_as_list(mylist2)}")

print(f"\nFeladat 4:\n\tA listában az öttel osztható számok összege: {sum_of_nums_devisible_by_five(mylist2)}")

print(f"\nFeladat 5:\n\tA listában a legkisebb szám a(z) {index_of_smallest_num(mylist2)} index-en áll")

#print("debug:")
#print(mylist2)
#print(f"debug:{mylist2[index_of_smallest_num(mylist2)]}")
