file_content = open('p4132.txt', 'r').read()
file_lines = file_content.split('\n')
disk_volume, disk_number, _ = file_lines[0].split()

archives = [int(x) for x in file_lines[1:] if x]
archives.sort(reverse=True)
print(archives[:5])

disks = [int(disk_volume) for _ in range(int(disk_number))]
disk_to_write = 0
not_packed = []


def change_disk():
    global disk_to_write
    disk_to_write += 1
    if disk_to_write >= len(disks):
        disk_to_write = 0


for archive in archives:
    start_disk = disk_to_write
    while disks[disk_to_write] < archive:
        change_disk()
        if disk_to_write == start_disk:
            break

    if disks[disk_to_write] >= archive:
        disks[disk_to_write] -= archive
        change_disk()
    else:
        not_packed.append(archive)

print(sum(not_packed), len(not_packed))