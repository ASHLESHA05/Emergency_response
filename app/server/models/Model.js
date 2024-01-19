import mongoose from "mongoose"
const userSchema=new mongoose.Schema({
    name:{
        type:String,
        required:true,
    },
    latitude:{
        type:String

    },
    longitude:{
        type:String
    }
},{timestamps:true})
export default mongoose.model('location',userSchema)

