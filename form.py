class New_client():
    country = "Russia"

    def __init__(self, first_name, second_name, city, index, address):
        self.first_name, self.second_name, self.city, self.index, self.address = (
            first_name, second_name, city, index, address)

    def get_client_info(self):

        client_info = {'first_name': self.first_name,
                       'second_name': self.second_name,
                       'country': New_client.country,
                       'city': self.city,
                       'index': self.index,
                       'address': self.address}

        return client_info
    @property
    def sh_name(self):
        return (self.second_name + ' ' + self.first_name[0] + '.')

    @property
    def addr(self):
      return (New_client.country + ', ' + self.city + ', ' + self.address + ', Postcode: '+ self.index)
    
    def print_client_card(self):
        print('{}: {}, {}: {}, {}: {}, {}: {}, {}: {}, {}: {}'.format("Name", self.first_name, "Last Name", self.last_name, "Country", New_client.country,
                                                              "City", self.city, "Index/Postcode", self.index, "Address", self.address))


test_client = New_client('Konstatin', 'Konstantinopolskiy',
                         'Petropavlovsk-Kamchatsky', 683000,
                         'Vladivostokskaya, 35')

test_client.get_client_info()
print(test_client.sh_name)
print(test_client.addr)