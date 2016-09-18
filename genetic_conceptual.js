
var GA = (function() {

  var TARGET = "George Seed is seriously cool";
  var ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ";
  var MUT_PROB = 100;

  var generateGenome = function()
      {
      var genome = [];
          for(var i = 0; i<TARGET.length;++i){
              genome[i]=ALPHABET[Math.floor(Math.random()*ALPHABET.length)];
              }
      return genome.join("");

      };

    var getFitness = function(genome)
          {
          var fitness = 0;

              for(var i = 0; i<TARGET.length;++i){

                  if (genome[i] === TARGET[i]){

                      fitness++;

                  }

              }
          return fitness
    };

    var getGenePool = function(genome)
          {
              var genePool = [];
              for(var i = 0; i<50;++i){
                  genePool[i] = genome;
                  }
          return genePool;

    };

    var evaluateFitness = function(genePool)
        {
        var highest = 0;
        var index = 0;
            for(var i = 0; i<genePool.length;++i){
                var fitness = getFitness(genePool[i]);

                    if (fitness>highest){
                    var highest = fitness;
                    var index = i;
                    }

                }

        return genePool[index];
    };

    var mutateGenome = function(genome,locking)

        {
        var newGenome = "";
            for(var i = 0; i<genome.length;++i){

                    //math.floor gives closest int equal to or small than value
                    //math.random gives random value 0-1
                    //below gives value 1 in MUT_PROB value (i.e. 10)

                if (Math.floor(Math.random()*MUT_PROB)===1){
                  if(locking==true){
                    if(genome[i]!=TARGET[i]){
                    newGenome+= ALPHABET[Math.floor(Math.random()*ALPHABET.length)]
                    }
                    else{
                    newGenome+= genome[i];
                    }
                  }
                  else(
                  newGenome+= ALPHABET[Math.floor(Math.random()*ALPHABET.length)]
                  )
                }
                else{
                newGenome+= genome[i];
                }
            }
        return newGenome;
    };

    var evolve = function(locking)
        {
            var numGens = 0;
            var locking = locking;
            var fittest = GA.generateGenome();
            console.log(fittest + " (initial seed Gene created)");
                while(GA.getFitness(fittest)!=TARGET.length)
                    {
                    numGens++;
                    // only fittest genome lives to next generation, becomes seed of new genepool
                    var pool = GA.getGenePool(fittest);
                    var pool2 = [];
                        for (var i=0;i<pool.length;++i){
                        pool2[i]=GA.mutateGenome(pool[i],locking);
                        }
                    fittest = GA.evaluateFitness(pool2);
                    if(numGens%10===0){
                        console.log(numGens);
                        console.log(fittest);
                    }
                    if(numGens>5000){
                      return console.log("failed to find match");
                    }
                }
            console.log(numGens);
            return console.log(fittest);
    };

  return {
    //command list
      mutateGenome : mutateGenome,
      evaluateFitness : evaluateFitness,
      getGenePool : getGenePool,
      getFitness : getFitness,
      generateGenome : generateGenome,
      evolve : evolve
  };
})();


GA.evolve(true);
