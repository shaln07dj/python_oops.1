class Animal:
  zoo_dict={}
 
  def __init__(self,name,category,fav_food,noise):
    self.name=name
    self.category=category
    self.fav_food=fav_food
    self.noise=noise

class Loin(Animal):
  def __init__(self, name, category, fav_food, noise):
      super().__init__(name, category, fav_food, noise)

  def update_lion(self):
    
    update_zoo_dict = {self.name:self.category}
    self.zoo_dict.update(update_zoo_dict)
    
   

class Tiger(Animal):
  def __init__(self, name, category, fav_food, noise):
      super().__init__(name, category, fav_food, noise)

  def update_tiger(self):
    
    update_zoo_dict = {self.name:self.category}
    self.zoo_dict.update(update_zoo_dict)
    

class Giraffe(Animal):
  def __init__(self, name, category, fav_food, noise):
      super().__init__(name, category, fav_food, noise)

  def update_giraffe(self):
    
    update_zoo_dict = {self.name:self.category}
    self.zoo_dict.update(update_zoo_dict)


class Elephant(Animal):
  def __init__(self, name, category, fav_food, noise):
      super().__init__(name, category, fav_food, noise)

  def update_elephant(self):
    
    update_zoo_dict = {self.name:self.category}
    self.zoo_dict.update(update_zoo_dict)


class Deer(Animal):
  def __init__(self, name, category, fav_food, noise):
      super().__init__(name, category, fav_food, noise)

  def update_deer(self):
    
    update_zoo_dict = {self.name:self.category}
    self.zoo_dict.update(update_zoo_dict)
   

class Zoo:
  food=[]
  voices=[]

  def __init__(self):
    pass


  no_of__lion=int(input('Enter no of Lions-->\n'))

  for i in range(no_of__lion):
    name=input(f'Enter name of Loin {i+1}: ')
    category=input(f'Enter Category of Loin {i+1}: ')
    noise=input(f'Enter Noise made by Loin {i+1}: ') 
    fav_food=input(f'Enter Food Loved by Loin {i+1}: ')
    

    obj_loin=Loin(name,category,fav_food,noise)
    
    obj_loin.update_lion()
    loin_fav_food=(f'{obj_loin.name}:{obj_loin.fav_food}')
    food.append(loin_fav_food)
    loin_voice=(f'{obj_loin.name}:{obj_loin.fav_food}')
    voices.append(loin_voice)

  no_of_tiger=int(input('Enter no of Tigers-->\n'))

  for i in range(no_of_tiger):
    name=input(f'Enter name of Tiger {i+1}: ')
    category=input(f'Enter Category of Tiger {i+1}: ')
    noise=input(f'Enter Noise made by Tiger {i+1}: ') 
    fav_food=input(f'Enter Food Loved by Tiger {i+1}: ')

    obj_tiger=Tiger(name,category,fav_food,noise)

    obj_tiger.update_tiger()
    tiger_fav_food=(f'{obj_tiger.name}:{obj_tiger.fav_food}')
    food.append(tiger_fav_food)
    tiger_voice=(f'{obj_tiger.name}:{obj_tiger.fav_food}')
    voices.append(tiger_voice)

  no_of_giraffe=int(input('Enter no of Giraffe-->\n'))

  for i in range(no_of_giraffe):
    name=input(f'Enter name of Giraffe {i+1}: ')
    category=input(f'Enter Category of Giraffe {i+1}: ')
    noise=input(f'Enter Noise made by Giraffe {i+1}: ') 
    fav_food=input(f'Enter Food Loved by Giraffe {i+1}: ')

    obj_giraffe=Giraffe(name,category,fav_food,noise)

    obj_giraffe.update_giraffe()
    giraffe_fav_food=(f'{obj_giraffe.name}:{obj_giraffe.fav_food}')
    food.append(giraffe_fav_food)
    giraffe_voice=(f'{obj_giraffe.name}:{obj_giraffe.fav_food}')
    voices.append(giraffe_voice)

  no_of_elephant=int(input('Enter no of Elephants-->\n'))

  for i in range(no_of_elephant):
    name=input(f'Enter name of Elephant {i+1}: ')
    category=input(f'Enter Category of Elephant {i+1}: ')
    noise=input(f'Enter Noise made by Elephant {i+1}: ') 
    fav_food=input(f'Enter Food Loved by E{i+1}: ')

    obj_elephant=Elephant(name,category,fav_food,noise)

    obj_elephant.update_elephant()
    elephant_fav_food=(f'{obj_elephant.name}:{obj_elephant.fav_food}')
    food.append(elephant_fav_food)
    elephant_voice=(f'{obj_loin.name}:{obj_loin.fav_food}')
    voices.append(elephant_voice)

  no_of_deer=int(input('Enter no of Deer-->\n'))

  for i in range(no_of_deer):
    name=input(f'Enter name of Deer {i+1}: ')
    category=input(f'Enter Category of Deer{i+1}: ') 
    noise=input(f'Enter Noise made by Deer {i+1}: ') 
    fav_food=input(f'Enter Food Loved by Deer{i+1}: ')

    obj_deer=Deer(name,category,fav_food,noise)

    obj_deer.update_deer()
    deer_fav_food=(f'{obj_deer.name}:{obj_deer.fav_food}')
    food.append(deer_fav_food)
    deer_voice=(f'{obj_deer.name}:{obj_deer.fav_food}')
    voices.append(deer_voice)

  print(f'Zoo Animals Dictionary:{Animal.zoo_dict}')
  
  
  def feed_food(self):
    #global food
    Food =self.food
    print('Food:')
    for zoofood in Food:
      print(zoofood)
   
    
  def make_noise(self):
    #global voices
    Voices=self.voices
    print('Voices:')
    for voice in Voices:
      print(voice)

obj=Zoo()
obj.feed_food()
obj.make_noise()
  
  



