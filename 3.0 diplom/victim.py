from vkapi import VkAPI

class Victim(VkAPI):

    def __init__(self, victim_id):
        super().__init__()
        self.data = self.user_info(victim_id)
        self.group_ids = self.groups(victim_id)

    def search(self, age_from, age_to, group_id=0):
        return self.search_victims(age_from, age_to, self, group_id)

    @property
    def first_name(self):
        return self.data['first_name']

    @property
    def last_name(self):
        return self.data['last_name']

    @property
    def sex(self):
        return self.data['sex']

    @property
    def sex_search(self):
        sex_search_var = 0
        if self.data['sex'] == 2:
            sex_search_var = 1
        if self.data['sex'] == 1:
            sex_search_var = 2
        return sex_search_var

    @property
    def city(self):
        return self.data['city']['id']

    @property
    def country(self):
        return self.data['country']['id']

    @property
    def interests(self):
        return self.data['interests']

    @property
    def music(self):
        return self.data['music']

    @property
    def victim_groups(self):
        return self.group_ids

    def photo_super_star(self, owner_id):
        return self.photo(owner_id)


