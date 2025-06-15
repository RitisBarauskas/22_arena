class Person:

    def __init__(self, name, hit_points, base_attack, protection_percentage):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = base_attack
        self.base_protection = protection_percentage
        self.things = []


    def set_things(self, things):
        """
        Устанавливает список предметов, которые носит персонаж.
        """
        pass

    def get_final_protection(self):
        """
        Вычисляет общий процент защиты.
        """
        pass

    def calculate_damage(self):
      """Вычитания урона"""
       pass


    def subtract_life(self, damage):
        """
        Вычитает урон из текущего количества жизней.
        """
        pass
