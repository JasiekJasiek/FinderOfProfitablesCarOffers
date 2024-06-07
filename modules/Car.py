class Car:

    def __init__(self, atributes):
        self.accident_free = atributes[ 0 ]
        self.brand = atributes[ 1 ]
        self.course = atributes[ 2 ]
        self.exploitation = atributes[ 3 ]
        self.model = atributes[ 4 ]
        self.horse_power = atributes[ 5 ]
        self.price = atributes[ 6 ]
        self.production_year = atributes[ 7 ]

    def to_list(self):
        return [
            self.accident_free,
            self.brand,
            self.course,
            self.exploitation,
            self.horse_power,
            self.model,
            self.price,
            self.production_year
        ]
