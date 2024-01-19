import mongoose from 'mongoose'
import colors from 'colors';
const connectDB = async()=>{   //asynchronous connection to mongo db
   try{
      const conn=await mongoose.connect("mongodb+srv://Ashlesha:ashubhai05@cluster0.bqd3cm9.mongodb.net/TripAdviser")
      console.log(`Connected To Mongodb Database ${conn.connection.host}`.bgMagenta.white);
   }catch(error){
    console.log(`Errro in Mongodb ${error}`.bgRed.white)
   }
};
export default connectDB;