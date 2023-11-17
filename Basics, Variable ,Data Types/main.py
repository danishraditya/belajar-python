fruits = ["Apple", "Banana", "Cherry"]

# tambahkan buah "Melon"
fruits_list = list(fruits)
fruits_list.append("melon")
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# ubah buah "Apple" menjadi "Grape"
fruits_list = list(fruits_tuple)
fruits_list[2] = "Grape"
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# hapus buah cherry dari list
fruits.remove("Cherry")

