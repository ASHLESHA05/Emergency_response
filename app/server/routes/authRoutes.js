import express from 'express';
const router = express.Router();
import userModel from '../models/Model.js';

router.post('/:Name', async (req, res) => {
  const { latitude, longitude } = req.body;
  const locationName = req.params.Name;

 
  if (!isValidCoordinate(latitude) || !isValidCoordinate(longitude)) {
    return res.status(400).json({ error: 'Invalid latitude or longitude values' });
  }   

  try {
    let locationToUpdate = await location.findOne({ Name: locationName });

    if (!locationToUpdate) {
      locationToUpdate = new location({ Name: locationName });
    }

    await userModel.findByIdAndUpdate(locationToUpdate._id,{latitude:latitude,longitude:longitude})
    res.status(200).send({
       success:true,
       message:"Success",
    })
  } catch (error) {
    console.error(`Error updating location status for ${locationName}:`, error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

function isValidCoordinate(value) {
  return typeof value === 'number' && !isNaN(value) && value >= -90 && value <= 90;
}

export default router;
