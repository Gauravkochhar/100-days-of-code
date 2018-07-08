
 
 var readline=require('readline');
 var fs,sd,temp;
 var prompts=readline.createInterface(process.stdin,process.stdout);
 prompts.question('Enter the first value:',function(n1){
	 
prompts.question('Enter second value:',function(n2){
	
	fs=n1;
	sd=n2;
		while(b!=0)
		{
			temp=sd;
			sd=fs%sd;
			fs=temp;
		}
console.log('Hcf of these number is:'+fs);
console.log('Lcm of these number is:'+(n1*n2)/fs);	
	process.exit();
  });	 
});
