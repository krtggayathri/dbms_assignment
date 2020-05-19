class PokeMon:
    sound = ""
    def __init__(self,name = None,level = 1,master = None):
        self._name = name
        self._level = level
        self._master = None
    
        if len(self._name) == 0:
            raise ValueError("name cannot be empty")
            
        if self._level <= 0:
            raise ValueError("level should be > 0")
            
    def __str__(self):
        return f"{self._name} - Level {self._level}"

            
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
    
    @property     
    def master(self):
        if self._master == None:
            print("No Master")
        else:
            return self._master
        
class running:
    by_run = ""
    @classmethod
    def run(cls):
        print(f"{cls.by_run} running...")
    

class swimming:
    by_swim = ""
    @classmethod
    def swim(cls):
        print(f"{cls.by_swim} swimming...")
        
        
class flying:
    by_fly = ""
    @classmethod
    def fly(cls):
        print(f"{cls.by_fly} flying...")


class Pikachu(PokeMon,running):
    sound = "Pika Pika"
    by_run = "Pikachu"
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        
    
class Squirtle(PokeMon,running,swimming):
    sound = "Squirtle...Squirtle"
    by_run = "Squirtle"
    by_swim = "Squirtle"
    
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        
        
class Pidgey(PokeMon,flying):
    sound = "Pidgey...Pidgey"
    by_fly = "Pidgey"
    
    
    def attack(self):
        print(f"Air attack with {self.level*5} damage")
    
    
class Swanna(PokeMon,flying,swimming):
    sound = "Swanna...Swanna"
    by_fly = "Swanna"
    by_swim = "Swanna"
    
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        print(f"Air attack with {self.level*5} damage")
   
    
class Zapdos(PokeMon,flying):
    sound = "Zap...Zap"
    by_fly = "Zapdos"
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        print(f"Air attack with {self.level*5} damage")
   


class Island:
    pokemon_list = []
    def __init__(self,name=None, max_no_of_pokemon=0, total_food_available_in_kgs=0):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_list.append(self)
        
    @property    
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f"{self._name} - {self.pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food"

        
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch  == self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
            
        else:
            self._pokemon_left_to_catch += 1
            
            
    @classmethod     
    def get_all_islands(cls):
       return Island.pokemon_list
       
       
class Trainer(PokeMon,Island):
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10*self._experience
        self._current_island = None 
        self._food_in_bag = 0
        self.list_pokemon = []
        
        
    def __str__(self):
        return f"{self._name}"
        
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    @property
    def current_island(self):
        if(self._current_island==None):
            print("You are not on any island")
        else:
            return self._current_island
    
    def move_to_island(self,island):
        self._current_island = island
            
    def collect_food(self):
        if self._current_island != None:
            if self.current_island._total_food_available_in_kgs > self._max_food_in_bag:
                if self._food_in_bag < self._max_food_in_bag:
                    self._food_in_bag += self._max_food_in_bag
                    self.current_island._total_food_available_in_kgs -= self._food_in_bag
                else:
                    self._food_in_bag = self._max_food_in_bag
            else:
                self._food_in_bag = self.current_island._total_food_available_in_kgs
                self.current_island._total_food_available_in_kgs = 0
                
        else:
            print("Move to an island to collect food")
            
  
    def catch(self,pokemon):
        pokemon._master = self
        self.list_pokemon.append(pokemon)
        if self._experience < pokemon.level*100:
            print(f"You need more experience to catch {pokemon.name}")
        else:
            print(f"You caught {pokemon.name}")
            self._experience += pokemon.level*20
            
      
    def get_my_pokemon(self):
        return self.list_pokemon
        
