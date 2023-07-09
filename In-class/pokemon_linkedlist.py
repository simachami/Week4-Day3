from requests import get

from LinkedList_hw import LinkedList

class Pokemon:
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.weight = None
        self.types = []
        self.image = ''
        self.evo_chain = []
        self.pokemon_api_call()
        
    def pokemon_api_call(self):
        response_object = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response_object.ok:
            poke_info = response_object.json()
            self.name = poke_info['name']
            self.abilities = poke_info['abilities']
            self.weight = poke_info['weight']
            self.types = poke_info['types']
            self.image = poke_info['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = poke_info['sprites']['front_default']
            setattr(self, 'species_url', poke_info['species']['url'])
        else:
            print(f'Error: status code {response_object.status_code}')
            
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def display_pokemon_info(self):
        print(f'{self.name} Weight: {self.weight}')
        print('Types:', end=' ')
        for poke_type in self.types:
            print(poke_type['type']['name'], end= ' ')
        print('\nAbilities:', end=' ')
        for ability in self.abilities:
            print(ability['ability']['name'],end=' ')
        # self.display_image()
        
    # def display_image(self, width=150):
    #     display(Image(self.image,width=width))

    def get_evolution_chain(self):
        res = get(self.species_url)
        if res.ok:
            data = res.json()
            res = get(data['evolution_chain']['url'])
            if res.ok:
              print('success')
              data = res.json()
              self.store_evo_chain(data['chain'])
            
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

charmander = Pokemon('charmander')
charmander.get_evolution_chain()
print(charmander.evo_chain)


              