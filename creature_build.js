//seed script
!function(a,b,c,d,e,f,g,h,i){function j(a){var b,c=a.length,e=this,f=0,g=e.i=e.j=0,h=e.S=[];for(c||(a=[c++]);d>f;)h[f]=f++;for(f=0;d>f;f++)h[f]=h[g=s&g+a[f%c]+(b=h[f])],h[g]=b;(e.g=function(a){for(var b,c=0,f=e.i,g=e.j,h=e.S;a--;)b=h[f=s&f+1],c=c*d+h[s&(h[f]=h[g=s&g+b])+(h[g]=b)];return e.i=f,e.j=g,c})(d)}function k(a,b){var c,d=[],e=typeof a;if(b&&"object"==e)for(c in a)try{d.push(k(a[c],b-1))}catch(f){}return d.length?d:"string"==e?a:a+"\0"}function l(a,b){for(var c,d=a+"",e=0;e<d.length;)b[s&e]=s&(c^=19*b[s&e])+d.charCodeAt(e++);return n(b)}function m(c){try{return o?n(o.randomBytes(d)):(a.crypto.getRandomValues(c=new Uint8Array(d)),n(c))}catch(e){return[+new Date,a,(c=a.navigator)&&c.plugins,a.screen,n(b)]}}function n(a){return String.fromCharCode.apply(0,a)}var o,p=c.pow(d,e),q=c.pow(2,f),r=2*q,s=d-1,t=c["seed"+i]=function(a,f,g){var h=[];f=1==f?{entropy:!0}:f||{};var o=l(k(f.entropy?[a,n(b)]:null==a?m():a,3),h),s=new j(h);return l(n(s.S),b),(f.pass||g||function(a,b,d){return d?(c[i]=a,b):a})(function(){for(var a=s.g(e),b=p,c=0;q>a;)a=(a+c)*d,b*=d,c=s.g(1);for(;a>=r;)a/=2,b/=2,c>>>=1;return(a+c)/b},o,"global"in f?f.global:this==c)};if(l(c[i](),b),g&&g.exports){g.exports=t;try{o=require("crypto")}catch(u){}}else h&&h.amd&&h(function(){return t})}(this,[],Math,256,6,52,"object"==typeof module&&module,"function"==typeof define&&define,"random");


//creature creation
var Creature = {
  init(name, age, location, seed){
    this.name = name;
    this.age = age;
    this.location = location;
    this.seed = seed;
    this.traitArray = [];
    this.type = "creature";
  },

  traits(){
    Math.seedrandom(this.seed);
    for(let i=0;i<10;++i){
    this.traitArray[i] = Math.floor(Math.random()*10)
    }

  return this.traitArray;
},
  announce(){
    console.log('A '+this.name+' appeared!');
  }
};

//location creation
var Location = {
  init(desc, biome){
    this.name = desc;
    this.biome = biome;
    this.traitArray = [];
    this.type = "location";
  },
  traits(){
    Math.seedrandom(this.biome);
    for(let i=0;i<10;++i){
    this.traitArray[i] = Math.floor(Math.random()*10)
    }

    return this.traitArray;
  }
};

//define functions
var GA = (function() {

  var generateGenome = function(name)
      {
        if (name.type == "creature"){
      var genome = [];
      traits = name.traits();
          for(let i = 0; i<traits.length;++i){
              genome[i]=traits[i];
              }
      return genome.join("");
      }

      else{
        var target = [];
        traits = name.traits();
            for(let i = 0; i<traits.length;++i){
                target[i]=traits[i];
                }
        return target.join("");
      }
    };

      var getFitness = function(genome,target)
            {
            var fitness = 0;

                for(let i = 0; i<target.length;++i){
                  x=genome[i];
                  y=target[i]
                  fitness = fitness + +x + +y;

                }
            return fitness
      };


return {
  //define methods
  generateGenome : generateGenome,
  getFitness : getFitness
};
})();



//tests below please

var creature1 = Object.create(Creature)
creature1.init('creature1',200,'iceland',"apples");


var location1 = Object.create(Location)
location1.init("land1","hot");



creature1.announce();
console.log(creature1.traits());
var genome1 = GA.generateGenome(creature1);
console.log(genome1);


console.log(location1.name);
console.log(location1.traits());
var target = GA.generateGenome(location1);
console.log(target);

console.log(GA.getFitness(genome1,target));


//Usage below

/*
var creature1 = Object.create(Creature)

creature1.init('creature1',200,'iceland','legs');

creature1.announce();

*/
