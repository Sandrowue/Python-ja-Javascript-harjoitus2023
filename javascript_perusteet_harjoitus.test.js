// Load libraries and modules

const stats = require('./javascript_perusteet_harjoitus');

// Define array and number of decimals for tests

const testArray = [1, 2, 3, 6];
const numberOfDecimals = 1;

// Create an object for statistical calculations
const statToTest = new stats.Programmer(testArray, numberOfDecimals);

test('Average should be ', () => {
    expect(statToTest.mean()).toBeCloseTo(3.0);
}); 