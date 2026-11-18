class Creature:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp})"

# ===============================
# SwimmingCreature Branch
# ===============================

class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.depth = 0

    def dive_to(self, new_depth):
        self.depth = new_depth
        print(f"{self.name} dives to depth {self.depth} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} attacks from underwater at depth {self.depth}!")
        print(f"It splashes {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")

# ===============================
# FlyingCreature Branch
# ===============================

class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power):
        super().__init__(name, hp, attack_power)
        self.altitude = 0

    def fly_to(self, new_altitude):
        self.altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude} meters.")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        print(f"{self.name} swoops down from altitude {self.altitude}!")
        print(f"{self.name} performs an aerial attack on {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0
        print(f"{target.name} HP is now {target.hp}")

# ===============================
# FireCreature Branch
# ===============================

class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        super().__init__(name, hp, attack_power)
        self.fire_level = max(0, min(100, fire_level))

    def emit_fire(self, new_fire_level):
        # fire_level ต้องอยู่ในช่วง 0-100
        self.fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} emits fire at level {self.fire_level}!")

    def attack(self, target):
        if not self.is_alive():
            print(f"{self.name} cannot attack because it is defeated.")
            return

        # ทุก 10 ระดับของไฟ เพิ่มดาเมจอีก 1
        fire_bonus = self.fire_level // 10
        total_damage = self.attack_power + fire_bonus

        print(f"{self.name} unleashes a blazing attack on {target.name}!")
        print(f"Base damage {self.attack_power} + fire bonus {fire_bonus} = {total_damage} damage!")
        target.hp = max(0, target.hp - total_damage)
        print(f"{target.name} HP is now {target.hp}")

if __name__ == "__main__":
    print("=== Creature Class Tests ===\n")

    # Test 1: Initialization
    goblin = Creature("Goblin", 30, 5)
    print("Test 1: Initialization")
    print(goblin)  # Expected: Goblin (HP: 30)
    print()

    # Test 2: Basic attack
    wolf = Creature("Wolf", 40, 10)
    sheep = Creature("Sheep", 25, 3)
    print("Test 2: Wolf attacks Sheep")
    wolf.attack(sheep)
    print(f"Sheep HP should now be 15 → Actual: {sheep.hp}")
    print()

    # Test 3: HP does not go below zero
    dragon = Creature("Dragonling", 50, 100)
    mouse = Creature("Mouse", 20, 1)
    print("Test 3: Dragonling overkills Mouse")
    dragon.attack(mouse)
    print(f"Mouse HP should now be 0 → Actual: {mouse.hp}")
    print()

    # Test 4: is_alive()
    slime = Creature("Slime", 10, 2)
    print("Test 4: Slime alive?")
    print("Slime should be alive →", slime.is_alive())
    slime.hp = 0
    print("Slime should NOT be alive →", slime.is_alive())
    print()

    # Test 5: Dead creature cannot attack
    ghost = Creature("Ghost", 0, 10)
    knight = Creature("Knight", 50, 7)
    print("Test 5: Ghost tries to attack Knight")
    ghost.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()

    # Test 6: Multiple attacks
    print("Test 6: Goblin attacks Slime twice")
    slime.hp = 10
    goblin.attack(slime)
    goblin.attack(slime)
    print(f"Slime should be at HP 0 → Actual: {slime.hp}")
    print()
    print("=== Tests Completed ===")
    print()

    print("=== SwimmingCreature Tests ===\n")
    serpent = SwimmingCreature("Aqua Serpent", 60, 7)
    serpent.dive_to(30)
    print(f"Depth should be 30 → Actual: {serpent.depth}")

    dummy = Creature("Practice Dummy", 40, 0)
    serpent.attack(dummy)
    print(f"Dummy HP should be 33 → Actual: {dummy.hp}")
    print()    
    print("=== Tests Completed ===")
    print()

    print("=== FlyingCreature Tests ===\n")
    hawk = FlyingCreature("Sky Hawk", 50, 8)
    hawk.fly_to(120)
    print(f"Altitude should be 120 → Actual: {hawk.altitude}")

    dummy = Creature("Practice Dummy", 40, 0)
    hawk.attack(dummy)
    print(f"Dummy HP should be 32 → Actual: {dummy.hp}")
    dummy.attack(hawk)
    print()
    print("=== Tests Completed ===")

    print()
    print("=== FireCreature Tests ===\n")
    drake = FireCreature("Ember Drake", 70, 6)
    print(f"Fire level should start at 0 → Actual: {drake.fire_level}")

    drake.emit_fire(50)
    print(f"Fire level should be 50 → Actual: {drake.fire_level}")

    drake.emit_fire(150)
    print(f"Fire level should be clamped to 100 → Actual: {drake.fire_level}")

    drake.emit_fire(-20)
    print(f"Fire level should be clamped to 0 → Actual: {drake.fire_level}")

    dummy = Creature("Practice Dummy", 40, 0)
    drake.emit_fire(50)
    drake.attack(dummy)
    print(f"Dummy HP should be 29 (6 + 5 = 11 damage) → Actual: {dummy.hp}")

    drake.emit_fire(0)
    drake.attack(dummy)
    print(f"Dummy HP should be 23 (6 damage) → Actual: {dummy.hp}")

    weak = Creature("Weakling", 5, 1)
    drake.emit_fire(100)
    drake.attack(weak)
    print(f"Weakling HP should be 0, not negative → Actual: {weak.hp}")

    drake.hp = 0
    knight = Creature("Knight", 50, 7)
    drake.attack(knight)
    print(f"Knight HP should remain 50 → Actual: {knight.hp}")
    print()
    print("=== Tests Completed ===")