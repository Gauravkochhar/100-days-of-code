var question= [
  "What is your name:>"  ,
  "What is your hobby:>",
  "What is your Percentage:>"
];
var answer=[];
function ask(i)
{
    process.stdout.write(question[i]); 
    
}
process.stdin.on('data',function(data)
                {
   answer.push(data.toString().trim()); 
   if(answer.length<question.length)
        {
           ask(answer.length);
        }
    else
        {
            process.exit();
        }
});
process.on('exit',function()
          {
   process.stdout.write(`\n\n\n\n`+`${answer[0]}`+`you can do `+`${answer[1]}`+` because your percentage is:`+`${answer[2]}`) 
});
ask(0);
