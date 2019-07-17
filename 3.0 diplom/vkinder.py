from victim import Victim

if __name__ == '__main__':
    check_pairs = []
    victim = Victim('418095195')
    list_pairs = victim.search(35, 45)
    for item in list_pairs:
        check_pairs.append(item)
    for group_id in victim.victim_groups:
        list_pairs = victim.search(35, 45, group_id)
        for item in list_pairs:
            check_pairs.append(item)
    i = 1
    for check_item in check_pairs:
        check_item['photo'] = victim.photo_super_star(check_item['id'])
        print(check_item)




