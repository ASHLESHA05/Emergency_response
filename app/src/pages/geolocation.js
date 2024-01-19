import React from 'react';

const Geolocation = () => {
  const setLocation = async () => {
    try {
      if (navigator.geolocation) {
        const position = await new Promise((resolve, reject) => {
          navigator.geolocation.getCurrentPosition(resolve, reject);
        });

        const locationInfo = `Location is ${position.coords.latitude} ${position.coords.longitude}`;
        document.getElementById("loc").innerHTML = locationInfo;

        const name = document.getElementById('name').value;
        const latitudee = position.coords.latitude;
        const longitudee = position.coords.longitude;
        console.log(latitudee+" "+longitudee)




        const response = await fetch(`/api/v1/auth/${name}`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            latitude: latitudee,
            longitude: longitudee,
          }),
        });

        // Check response.ok if needed
        if (response.ok) {
          console.log('Location updated successfully.');
        } else {
          console.error('Failed to update location:', response.statusText);
        }
      } else {
        showError("Geolocation is not supported by this browser.");
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const showError = (error) => {
    document.getElementById("loc").innerHTML = error;
  };

  return (
    <div>
      <input type='text' id='name' placeholder='Your name' />
      <button onClick={setLocation}>Click Here</button>
      <p id="loc"></p>
    </div>
  );
};

export default Geolocation;
