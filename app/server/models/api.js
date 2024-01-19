// api.js
const updateTaskCoordinates = async (name, latitude, longitude) => {
    try {
      const response = await fetch(`/tasks/${name}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          latitude: latitude,
          longitude: longitude,
        }),
      });
  
      if (!response.ok) {
        throw new Error('Failed to update task coordinates');
      }
  
      const updatedTask = await response.json();
      return updatedTask;
    } catch (error) {
      console.error('Error updating task coordinates:', error);
      throw error;
    }
  };
  
  export { updateTaskCoordinates };
  