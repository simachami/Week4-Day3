from requests import get
from IPython.display import Image
from IPython.display import display
from LinkedList_hw import LinkedList
class Pokemon:
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.weight = None
        self.types = []
        self.image = ''
        self.poke_info = ''
        self.evo_chain = []
        self.pokemon_api_call()
        
    def pokemon_api_call(self):
        response_object = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response_object.ok:
            self.poke_info = response_object.json()
            self.name = self.poke_info['name']
            self.abilities = self.poke_info['abilities']
            self.weight = self.poke_info['weight']
            self.types = self.poke_info['types']
            self.image = self.poke_info['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = self.poke_info['sprites']['front_default']
        else:
            print(f'Error: status code {response_object.status_code}')
            
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def display_pokemon_info(self):
        print(f'Name: {self.name} \nWeight: {self.weight}')
        print('Types:', end=' ')
        for poke_type in self.types:
            print(poke_type['type']['name'], end= ' ')
        print('\nAbilities:', end=' ')
        for ability in self.abilities:
            print(ability['ability']['name'],end=' ')
        self.display_image()
        
    def display_image(self, width=150):
        display(Image(self.image,width=width))
            
#pokemon= Pokemon('charizard')


    #pokemon.display_pokemon_info()
    def get_evolution_chain(self, pokemon):
        species_url = pokemon.poke_info['species']['url']
        species_response_object = get(species_url)
        
        #Get Evolution Chain URL from the species_response_object
        pokemon_info = species_response_object.json()
        evolution_chain_url = pokemon_info['evolution_chain']['url']
        evolution_response_object = get(evolution_chain_url)
        
        #Get the base level pokemon name for the evolution chain
        evolution_pokemon_info = evolution_response_object.json()
        base_level_pokemon_name = evolution_pokemon_info['chain']['species']['name']
        self.store_evo_chain(evolution_pokemon_info['chain'])

    #Create Method evolve_pokemon
    #pass in a pokemon object
    def evolve_pokemon(self, pokemon):
        
        #Create a variable to hold the confirmed evolution pokemon name
        confirmed_evolution_name = ''
        
        #Get Pokemon Species for the passed in pokemon object
        #Pokemon species is a variable in the pokemon JSON object
        #Get species URL from the pokemon info
        species_url = pokemon.poke_info['species']['url']
        species_response_object = get(species_url)
        
        #Get Evolution Chain URL from the species_response_object
        pokemon_info = species_response_object.json()
        evolution_chain_url = pokemon_info['evolution_chain']['url']
        evolution_response_object = get(evolution_chain_url)
        
        #Get the base level pokemon name for the evolution chain
        evolution_pokemon_info = evolution_response_object.json()
        base_level_pokemon_name = evolution_pokemon_info['chain']['species']['name']
        #Check if the pokemon has a first evolution
        evolves_to_list = evolution_pokemon_info['chain']['evolves_to']
        first_evolution_name = ''
        for evolution in evolves_to_list:
            first_evolution_name = evolution['species']['name']
            #print(evolution['species']['name'])
        
        #Check if the pokemon hasn't evolved yet
        if pokemon.name == base_level_pokemon_name:
            #If true, the first evolved_to is our new pokemon
            #use first_evolution_name
            confirmed_evolution_name = first_evolution_name
        else:
            #Check if pokemon has evolved once
            if pokemon.name == first_evolution_name:
                #checking to see if second_evolution does not exist, then throw an error. 
                if len(evolves_to_list[0]['evolves_to']) != 0:
                    second_evolution_name = evolves_to_list[0]['evolves_to'][0]['species']['name']
                    #second_evolution_name = evolves_to_list[0]['evolves_to'][0]['species']['name']
                    confirmed_evolution_name = second_evolution_name
                else:
                    print("Cannot evolve anymore!!!")
            else:
                print("Cannot evolve anymore!!!")
        
        
        if confirmed_evolution_name != '':
            #Create new pokemon object for the evolved pokemon. 
            evolved_pokemon_object = Pokemon(confirmed_evolution_name)
            #Call display_pokemon_info on the evolved pokemon object
            evolved_pokemon_object.display_pokemon_info()


    def store_evo_chain(self, evo_chain_dic):
        self.evo_chain.append(evo_chain_dic['species']['name'])
        if evo_chain_dic['evolves_to']:
            self.store_evo_chain(evo_chain_dic['evolves_to'][0])
        else:
            self.create_evo_linked_list()

    def create_evo_linked_list(self):
            lst = LinkedList(self.evo_chain[0])
            for i, poke in enumerate(self.evo_chain):
                if i != 0:
                    lst.append_node(poke)
            setattr(self, 'evo_chain', lst)

    
# Calling our new method
charmander = Pokemon('charmander')
charmander.get_evolution_chain(charmander)
print(charmander.evo_chain)





# class Move_Tutor:
#     def __init__(self):
#         self.move_list = []
        
    
#     def teach_move(self):
#         while True:
#             teach_move_input = input("What move would you like to teach? or would you like to quit?").lower()
#             print(f'{pokemon.name} learned {teach_move_input}!')
#             if teach_move_input == "quit" or teach_move_input == "q":
#                 break
                
#             if teach_move_input in self.move_list:
#                 print(f' {teach_move_input} is already in the list' )
#                 #checking the length of the list. if more than 4, ask to replace a move
#             elif len(self.move_list) == 4:
#                 print("The move list is full. Would you like to replace an existing move? ")
#                 #give them the option to choose if they want to replace a move
#                 replace_move_input = input("Yes or No? ").lower()
#                 #if they say yes, ask which move to replace
#                 if replace_move_input == "yes" or replace_move_input == 'y':
#                     print(self.move_list)
#                     move_forward_to_replace = input("Which move would you like to replace? ")
#                     #check to see if the requested move input is already in the list, print a message
#                     if replace_move_input in self.move_list:
#                         print(f' {replace_move_input} is already in the list' )
#                         continue
#                         #replace the move in the list
#                     if move_forward_to_replace in self.move_list:
#                         index = self.move_list.index(move_forward_to_replace)
#                         self.move_list[index] = teach_move_input
#                         print(self.move_list)
#                 elif replace_move_input == "no" or replace_move_input == "n":
#                     continue
#                 else:
#                     print("Invalid input")
#                     continue
#             else:
#                 self.move_list.append(teach_move_input)

    
# class Pokemon(Move_Tutor):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
        


# pokemon = Pokemon("charizard")

# pokemon.teach_move()
# print(f' {pokemon.name}\'s Move List: {pokemon.move_list}')
    

