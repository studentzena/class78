Flappy Bird
============

In this activity, you will load the NEAT configuration file and stop the bird on collision with pipe.


<img src= "https://media.slid.es/uploads/1525749/images/10589900/C78PCP.gif" width = "480" height = "220">


Follow the given steps to complete this activity:


1. Load and configure the network


* Open the main.py file.

* Create the neural network using genome and config.

    `net = neat.nn.FeedForwardNetwork.create(genome, config)`

* Check if `bird.y` become greater then `600` or less then `0`.

* Stop if bird collides with pipe by using `bird.colliderect(pipe)` to check collision.

    `if bird.colliderect(pipe) or bird.y > 600 or bird.y < 0:`

* Increment the `genomeCount` by `1`.

    `genomeCount =genomeCount + 1`

* Add `break` statement to stop the game for current genome.

    `break`


* Declare a variable `config` and load the configuration file.

    `config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,'config-feedforward.txt')`

* Declare a variable `p` and set the population to it.

    `p = neat.Population(config)`

* Run the genetic algorithm for population "p" and pass "eval_fitness" function.

    `winner = p.run(eval_fitness,7)`
         
* Save and run the code to check the output.