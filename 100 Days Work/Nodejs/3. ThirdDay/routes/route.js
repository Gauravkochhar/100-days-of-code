const express=require('express');
const router=express.Router();

const Contact=require('../models/contact')

router.get('/contact',(req,res,next)=>{
    Contact.find(function(err,contacts){
        res.json(contacts);
    })
});

router.post('/contact',function(req,res,next){
    //logic for adding contact into db.
    var newContact=new Contact({
        first_name:req.body.first_name,
        last_name:req.body.last_name,
        phone:req.body.phone
    })
    newContact.save((err,contact)=>{
        if(err){
            res.json("Failed to add the contact"+err);
        }
        else{
            res.json("Contact added Succesfully.")
        }
    })
});
router.delete('/contact/id',function(req,res,next){
    //logic for deleting the contacts from the db.
    Contact.remove({id: req.param.id},function(err,result){
        if(err){
            res.json("Contact is not deleted Successfully."+err);
        }
        else{
            res.json("Contact is deleted successfully.");
        }
    })
});
module.exports=router;
