# Recursive Python function to solve the tower of hanoi
import tower


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        tower.move(source, destination)
        tower.print_towers(disks)
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from", source, "to", destination)
    tower.move(source, destination)
    tower.print_towers(disks)
    tower_of_hanoi(n - 1, auxiliary, destination, source)


n = disks = int(input("Enter the Number of Disks: "))
tower.init_tower_a(disks)

tower.print_towers(disks)
tower_of_hanoi(n, 'Source', 'Destination', 'Auxiliary')
