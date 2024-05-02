import ClassRoom from './0-classroom.js';

export default function createClassrooms() {
  const capacities = [19, 20, 34];
  const classrooms = capacities.map(capacity => {
    const room = new ClassRoom(capacity);
    return room;
  });
  return classrooms;
}
