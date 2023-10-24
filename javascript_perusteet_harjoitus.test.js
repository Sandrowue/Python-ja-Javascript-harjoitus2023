// Load libraries and modules

const stats = require('./javascript_perusteet_harjoitus');

// Define array and number of decimals for tests

const testArray = [1, 2, 3, 6];


// Create an object for statistical calculations
const statToTest = new stats.Programmer('Sandro', 'Fullstack', ['Python', 'Javascript'], 'Student', testArray);

test('Average should be 3.0', () => {
    expect(statToTest.mean()).toBeCloseTo(3.000);
}); 