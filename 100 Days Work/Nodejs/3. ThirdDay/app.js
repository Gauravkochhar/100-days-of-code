//importing modules
var express=require('express')
var mongoose=require('mongoose')
var bodyparser=require('body-parser')
var cors=require('cors')
var path=require('path')

var app=express();

var route=require('./routes/route')

mongoose.connect('mongodb://localhost:27017/contactlist', { useNewUrlParser: true });
mongoose.connection.on('connected',()=>{
    console.log("Connected to the database.");
})
mongoose.connection.on('error',(err)=>{
    if(err){
        console.log("Error in database connection is:"+err);
    }
});
//add middleware.
app.use(cors());

//add bodyparser.
app.use(bodyparser.json());

//for static files. you have to give address.
app.use(express.static(path.join(__dirname,'public')));

app.use('/api',route);

//port no
const port= 3000;

//Testing of server.
app.get('/',(req,res)=>{
    res.send('footbar.');
});


//bind port to the server.
app.listen(3000,()=>{
    console.log("Server is running on the port 3000.");
});
