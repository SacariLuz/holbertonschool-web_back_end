import listOfStudents, { StudentHolberton, HolbertonClass } from './9-hoisting.js';

test('initialization works correctly', () => {
  expect(listOfStudents.length).toBe(5);
});
