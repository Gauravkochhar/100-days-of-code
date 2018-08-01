var readline=require('readline');
var rl=readline.createInterface(process.stdin,process.stdout);
rl.question("what is the name of your friend:",function(answer)
           {
   console.log(answer); 
    rl.close();
});
