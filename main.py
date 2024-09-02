import pygame, sys,random
import neat
import pickle 

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))
images={}
images["bg1"] = pygame.image.load("bg1.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
gen=0


class Bird:
    bird=pygame.Rect(100,250,30,30)
    speed=0
    gravity=0.5
    y = 0
    def moveup(self):
        self.speed=0
        self.speed=-10
    def movedown(self):
        global speed
        self.speed+=self.gravity
        self.bird.y +=self.speed
        self.y = self.bird.y
    def colliderect(self, obj):
        if self.bird.colliderect(obj.bpipe) or self.bird.colliderect(obj.tpipe):
            return True 
        return False
    def display(self):
        screen.blit(images["bird"],self.bird)
    

class Pipe:
    def __init__(self,x):
        self.height=random.randint(150, 400)
        self.tpipe=pygame.Rect(x,self.height-400,40,300)
        self.bpipe=pygame.Rect(x,self.height+100,40,300)
    def move(self):
        self.tpipe.x-=4
        self.bpipe.x-=4
        if self.tpipe.x<-40:
            self.tpipe.x=450
            self.bpipe.x=450
            self.height=random.randint(150, 400)
            self.tpipe.y=self.height-400
            self.bpipe.y=self.height+100
    def display(self):
        screen.blit(images["pipe"],self.bpipe)
        screen.blit(images["invertedpipe"],self.tpipe)


def save(winner):
    file_name = 'std1.pkl'
    with open(file_name, 'wb') as file:
        pickle.dump(winner, file)
        print(f'Object successfully saved to "{file_name}"')


def eval_fitness(generation, config):
    global gen
    genomeCount=0
    gen = gen+1

    for gid, genome in generation: 
        genome.fitness = 0 

        # Create the neural network using genome and config
        neuralNetwork = neat.nn.FeedForwardNetwork.create(genome,config) 
        
        pipe = Pipe(250)
        bird = Bird() 
        
        score_font=pygame.font.Font('freesansbold.ttf', 20)       
        groundx=0
        state="play"
        bird.bird.y=200 
        
        while True:
            screen.fill((50,150,255))
            screen.blit(images["bg1"],[0,0])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.moveup()
                        
            genome.fitness += 0.1         
            pipe.display()
            bird.movedown()
            bird.display()
            
            # Check if bird.y become greater then 600 or less then 0. Also stop if bird collides with pipe use bird.colliderect(pipe) to check collision
            if bird.y>600 or bird.y<0 or bird.colliderect(pipe) :
            
                # Increment the genomeCount
                genomeCount+=1
                # Add break statement to stop the game for current genome
                break

            if groundx < -330:
                groundx=0

            groundx-=5
            pipe.move()
                  
            
            screen.blit(images["base"],[groundx,550])
            score_text=score_font.render("Gen:"+str(gen)+" Genome:"+str(genomeCount), True, (0,0,255)) 
            screen.blit(score_text,[10,10])
           
            pygame.display.update()
            clock.tick(30)

    
# Load configuration file in variable config
config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,'config-feedforward.txt')
# Create a population "p"
p = neat.Population(config)
# Run the genetic algorithm for population "p" and pass "eval_fitness" function
winner=p.run(eval_fitness,5)

  

  
    
